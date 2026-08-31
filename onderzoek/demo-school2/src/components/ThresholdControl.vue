<script setup>
import { ref, onMounted } from 'vue';
import { useApi } from '../composables/useApi';

const api = useApi();
const threshold = ref(80);
const isUpdating = ref(false);

const emit = defineEmits(['update']);

onMounted(async () => {
  const data = await api.getThreshold();
  if (data && data.threshold !== undefined) {
    threshold.value = Math.round(data.threshold * 100);
  }
});

async function updateThreshold() {
  isUpdating.value = true;
  const decimalValue = threshold.value / 100;
  try {
    await api.setThreshold(decimalValue);
    emit('update');
    // Simple visual feedback
    setTimeout(() => { isUpdating.value = false; }, 600);
  } catch (error) {
    console.error("Failed to update threshold:", error);
    isUpdating.value = false;
  }
}

async function resetThreshold() {
  threshold.value = 80;
  await updateThreshold();
}
</script>

<template>
  <div class="card threshold-section">
    <div class="card-header">
      <div class="card-icon">⚙️</div>
      <h2>Sensitivity</h2>
    </div>
    
    <div class="threshold-display">
      <div class="big-number">{{ threshold }}%</div>
      <div class="sub-text">Detection Threshold</div>
    </div>

    <div class="slider-container">
      <input 
        type="range" 
        class="threshold-slider" 
        v-model.number="threshold"
        min="0" 
        max="100" 
      >
      <div class="threshold-labels">
        <span>Sensitive</span>
        <span>Strict</span>
      </div>
    </div>

    <div class="button-group">
      <button 
        class="btn btn-primary" 
        @click="updateThreshold"
        :disabled="isUpdating"
      >
        {{ isUpdating ? 'Saving...' : 'Apply Changes' }}
      </button>
      <button class="btn btn-secondary" @click="resetThreshold">Reset</button>
    </div>
  </div>
</template>

<style scoped>
.threshold-section .button-group {
  display: flex;
  gap: 10px;
  margin-top: 1rem;
}
.sub-text { 
  font-size: 0.8rem; 
  color: var(--text-muted); 
  margin-top: 0.5rem; 
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.threshold-display { 
  text-align: center; 
  margin-bottom: 1.5rem; 
  padding: 1.25rem;
  background: var(--bg-input); /* Ensure this variable exists in main.css */
  border-radius: 12px;
}

.big-number { 
  font-size: 2.5rem; 
  font-weight: 700; 
  color: var(--text-main); 
}

/* --- THE SLIDER FIX --- */
input[type=range] {
  -webkit-appearance: none; /* Hides default slider */
  appearance: none;
  width: 100%;
  background: transparent; /* Essential for custom track */
  height: 30px; /* Gives the invisible hit-area a height */
  margin: 10px 0;
}

/* 1. The Track (The line) */
input[type=range]::-webkit-slider-runnable-track {
  width: 100%;
  height: 8px; /* Fixed height */
  cursor: pointer;
  background: #3f3f46; /* Hardcoded color if variable fails */
  background: var(--border-active, #3f3f46); 
  border-radius: 4px;
}

/* 2. The Thumb (The circle) */
input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  height: 20px;
  width: 20px;
  border-radius: 50%;
  background: #ffffff; /* Pure white for visibility */
  cursor: pointer;
  margin-top: -6px; /* (Track Height / 2) - (Thumb Height / 2) */
  box-shadow: 0 0 10px rgba(0,0,0,0.5);
  border: 2px solid var(--primary, #818cf8);
}

/* Firefox Support */
input[type=range]::-moz-range-track {
  width: 100%;
  height: 8px;
  background: var(--border-active, #3f3f46);
  border-radius: 4px;
}
input[type=range]::-moz-range-thumb {
  height: 20px;
  width: 20px;
  border-radius: 50%;
  background: #ffffff;
  border: 2px solid var(--primary, #818cf8);
}

.threshold-labels {
  display: flex;
  justify-content: space-between;
  margin-top: 0.5rem;
  font-size: 0.75rem;
  color: var(--text-muted);
}
</style>