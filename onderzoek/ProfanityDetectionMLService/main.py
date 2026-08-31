from fastapi import FastAPI, HTTPException, Query, Depends
from pydantic import BaseModel, Field, field_validator
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel, Field as SQLField, Session, create_engine, select
from datetime import datetime
from typing import Optional
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

classifier = pipeline(
    "text-classification", model="unitary/toxic-bert", return_all_scores=True
)

# Database setup - PostgreSQL
# Default local PostgreSQL URL, can be overridden with DATABASE_URL environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/toxicity_db")
engine = create_engine(DATABASE_URL, echo=False)


class Threshold(SQLModel, table=True):
    """Model to store threshold settings with history"""
    id: Optional[int] = SQLField(default=None, primary_key=True)
    value: float = SQLField(ge=0.0, le=1.0)
    created_at: datetime = SQLField(default_factory=datetime.utcnow)
    is_active: bool = SQLField(default=True)


class ScanResult(SQLModel, table=True):
    """Model to store scan results"""
    id: Optional[int] = SQLField(default=None, primary_key=True)
    text: str = SQLField(max_length=10000)
    is_profane: bool
    toxic_labels: str = SQLField(default="[]")
    raw_scores: str = SQLField(default="{}")
    threshold_used: float
    scanned_at: datetime = SQLField(default_factory=datetime.utcnow)


def get_db():
    """Dependency to get database session"""
    with Session(engine) as session:
        yield session


def init_db():
    """Initialize database tables"""
    SQLModel.metadata.create_all(engine)


# Initialize database on startup
init_db()


class TextInput(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=10000,
        description="Text to analyze for toxicity",
        examples=["Hello, this is a sample text to analyze."]
    )

    @field_validator("text")
    @classmethod
    def text_must_not_be_whitespace(cls, v):
        if v.strip() == "":
            raise ValueError("Text cannot be empty or whitespace only")
        return v.strip()


def get_current_threshold(session: Session) -> float:
    """Get the current active threshold from database"""
    result = session.exec(select(Threshold).where(Threshold.is_active == True).order_by(Threshold.created_at.desc())).first()
    if result:
        return result.value
    return 0.8


@app.post("/detect")
def detect_toxicity(input: TextInput, session: Session = Depends(get_db)):
    """
    Detect toxicity in the provided text.
    Results are saved to database for persistence.
    """
    threshold = get_current_threshold(session)
    
    try:
        result = classifier(input.text)[0]

        toxic_labels = []

        for r in result:
            if r["score"] >= threshold and r["label"].lower() != "non-toxic":
                toxic_labels.append(
                    {"label": r["label"].lower(), "score": round(r["score"], 4)}
                )

        is_profane = len(toxic_labels) > 0
        
        response_data = {
            "profanity": is_profane,
            "toxic_labels": toxic_labels,
            "raw_scores": {r["label"]: round(r["score"], 4) for r in result},
            "threshold_used": threshold
        }
        
        # Save scan result to database
        scan_result = ScanResult(
            text=input.text[:1000] if len(input.text) > 1000 else input.text,
            is_profane=is_profane,
            toxic_labels=json.dumps(toxic_labels),
            raw_scores=json.dumps({r["label"]: round(r["score"], 4) for r in result}),
            threshold_used=threshold
        )
        session.add(scan_result)
        session.commit()
        
        return response_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis error: {str(e)}")

@app.post("/health")
def health_check():
    return {"status": "ok"}


@app.post("/threshold")
def set_threshold(new_threshold: float = Query(..., ge=0.0, le=1.0), session: Session = Depends(get_db)):
    """Set a new threshold for toxicity detection."""
    previous_thresholds = session.exec(select(Threshold).where(Threshold.is_active == True)).all()
    for thresh in previous_thresholds:
        thresh.is_active = False
    
    threshold_record = Threshold(value=new_threshold, is_active=True)
    session.add(threshold_record)
    session.commit()
    
    return {
        "message": "Threshold updated successfully",
        "threshold": new_threshold,
        "threshold_percent": f"{new_threshold * 100:.0f}%"
    }

@app.get("/threshold")
def get_threshold(session: Session = Depends(get_db)):
    threshold = get_current_threshold(session)
    return {"threshold": threshold, "threshold_percent": f"{threshold * 100:.0f}%"}


@app.get("/stats")
def get_stats(session: Session = Depends(get_db)):
    """Get statistics about scans."""
    total_scans = session.query(ScanResult).count()
    profane_scans = session.query(ScanResult).where(ScanResult.is_profane == True).count()
    safe_scans = total_scans - profane_scans
    
    current_threshold = get_current_threshold(session)
    
    # Calculate average scores by category
    all_results = session.exec(select(ScanResult)).all()
    
    category_scores = {}
    for result in all_results:
        raw_scores = json.loads(result.raw_scores)
        for label, score in raw_scores.items():
            if label not in category_scores:
                category_scores[label] = []
            category_scores[label].append(score)
    
    avg_scores = {}
    for label, scores in category_scores.items():
        avg_scores[label] = round(sum(scores) / len(scores), 4)
    
    return {
        "total_scans": total_scans,
        "profane_scans": profane_scans,
        "safe_scans": safe_scans,
        "profane_percentage": round(profane_scans / total_scans * 100, 1) if total_scans > 0 else 0,
        "current_threshold": current_threshold,
        "average_scores": avg_scores
    }


@app.get("/scans/history")
def get_scan_history(session: Session = Depends(get_db), limit: int = Query(default=20, ge=1, le=100)):
    """Get the history of all text scans."""
    results = session.exec(select(ScanResult).order_by(ScanResult.scanned_at.desc()).limit(limit)).all()
    total_count = session.query(ScanResult).count()
    
    return {
        "total": total_count,
        "scans": [
            {
                "id": r.id,
                "text_preview": r.text[:100] + "..." if len(r.text) > 100 else r.text,
                "is_profane": r.is_profane,
                "toxic_labels": json.loads(r.toxic_labels),
                "scanned_at": r.scanned_at.isoformat()
            }
            for r in results
        ]
    }


@app.delete("/scans/clear")
def clear_scan_history(session: Session = Depends(get_db)):
    """Clear all scan history."""
    session.query(ScanResult).delete()
    session.commit()
    return {"message": "Scan history cleared successfully"}
