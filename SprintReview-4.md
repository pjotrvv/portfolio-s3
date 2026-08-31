# Procesreview

## Verdeling van user stories
- User stories moeten in dezelfde sprint staan waarin eraan gewerkt wordt.
- Als er in Sprint 4 al aan een story gewerkt wordt, moet deze ook in Sprint 4 in progress staan, zelfs als deze oorspronkelijk gepland was voor Sprint 5.

## Gezamenlijk opstellen van user stories
- User story moet frontend en backend bevatten en het moet een geheel zijn van alle benodigde functionaliteiten. 
- Splitsen veroorzaakt miscommunicatie over functionaliteit en acceptatiecriteria.

## User story mag niet naar "Done" voor alles af is
- Pas op Done zetten wanneer:
  - alle subtaken afgevinkt zijn,
  - functionaliteit getest en goedgekeurd is,
  - en de feature gedeployed is.

## Geen komma in user stories
- Een komma betekent vaak meerdere functionaliteiten in één user story.
- User stories moeten klein blijven volgens INVEST.

## Bestaande functionaliteit benoemen
- Vermeld altijd wat er al bestaat om de scope en regressierisico’s helder te houden.

## Definition of Done bij Zoek/Filter-story
- DoD was niet volledig afgevinkt.
- Zonder volledige DoD mag een story niet op Done gezet worden.

---

# Klantreview (Dauwe)

- “Goedgekeurd door” is een nice-to-have.
- Sprintdoelen waren mogelijk te groot voor een sprint van twee weken.
- Jammer dat de statusfilter niet werkte.
- Verhaal en presentatie waren professioneel en duidelijk.

---

# Code Review

## Structuur & Architectuur
- Verwijder de `infra` package.
- Controleer of de extra declaratie-DTO-laag nodig is.
- Verwijder `Declaratie.java` als deze niet meer gebruikt wordt.

## Domainlaag
- Domain is te compact; niet alles in `Claim.java` stoppen.
- Overweeg nieuwe domain classes voor betere structuur.
- Pas Single Responsibility Principle toe.
- Gebruik duidelijke class invariants.

## Principes & Best Practices
- Tell Don’t Ask toepassen.
- Information Export Principle respecteren.
- Vermijd magic values → gebruik betekenisvolle constants.

## DTO’s & Pakketten
- `LoggedIn.java` is een DTO en hoort geen domain class te zijn.

## API & REST
- Endpoint `"/image"` is niet RESTful.
- Paden zoals `claims/users/user` zijn onduidelijk.
  - Beter: `users/{id}/claims`
- `getEvidence` volgt geen REST-conventie.
  - Beter: `api/evidence/{claimId}`

