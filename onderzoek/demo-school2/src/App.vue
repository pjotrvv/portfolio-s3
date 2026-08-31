<script setup>
import { ref, onMounted } from 'vue';
import { useApi } from './composables/useApi';
import AnalyzeInput from './components/AnalyzeInput.vue';
import AnalysisResult from './components/AnalysisResult.vue';
import StatsDashboard from './components/StatsDashboard.vue';
import ScanHistory from './components/ScanHistory.vue';
import ThresholdControl from './components/ThresholdControl.vue';

const api = useApi();
const currentResult = ref(null);
const stats = ref(null);
const history = ref(null);
const isAnalyzing = ref(false);

onMounted(async () => {
  await api.checkHealth();
  refreshData();
  setInterval(api.checkHealth, 5000);
});

async function refreshData() {
  stats.value = await api.getStats();
  history.value = await api.getHistory();
}

async function handleAnalyze(text) {
  isAnalyzing.value = true;
  try {
    currentResult.value = await api.analyzeText(text);
    await refreshData();
  } catch (error) {
    console.error(error);
  } finally {
    isAnalyzing.value = false;
  }
}

// Inside <script setup> in App.vue

async function handleClearHistory() {
  if (confirm('Are you sure you want to clear all scan history?')) {
    try {
      await api.clearHistory(); // Ensure this method exists in useApi.js
      await refreshData();      // Refresh stats and history after clearing
    } catch (error) {
      console.error("Failed to clear history:", error);
    }
  }
}

</script>

<template>
  <div class="layout">
    <header class="app-header">
      <div class="brand">
        <div class="logo-circle">🛡️</div>
        <div>
          <h1>Toxic-BERT</h1>
          <span class="badge" :class="{ active: api.isConnected.value }">
            {{ api.isConnected.value ? 'System Online' : 'Offline' }}
          </span>
        </div>
      </div>
    </header>

    <main class="bento-grid">
      <div class="col-main">
        <AnalyzeInput :is-loading="isAnalyzing" @analyze="handleAnalyze" />
        <AnalysisResult :result="currentResult" />
      </div>

      <div class="col-side">
        <ThresholdControl @update="refreshData" />
        <StatsDashboard :stats="stats" />
      </div>

      <ScanHistory :history="history" @clear="handleClearHistory" />
    </main>
  </div>
</template>

<style scoped>
.layout {
  max-width: 1100px;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}

/* Header Styling */
.app-header {
  margin-bottom: 2.5rem;
}
.brand {
  display: flex;
  align-items: center;
  gap: 1rem;
}
.logo-circle {
  width: 48px;
  height: 48px;
  background: var(--primary-glow);
  color: var(--primary);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
}
h1 {
  font-size: 1.25rem;
  font-weight: 700;
  margin: 0 0 0.25rem 0;
  letter-spacing: -0.02em;
}
.badge {
  font-size: 0.75rem;
  font-weight: 500;
  color: var(--danger);
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.badge::before { content: ''; width: 6px; height: 6px; border-radius: 50%; background: currentColor; }
.badge.active { color: var(--success); }

/* Bento Grid Layout */
.bento-grid {
  display: grid;
  grid-template-columns: 1.4fr 0.8fr; /* Asymmetric grid is more modern */
  gap: 1.5rem;
}
.col-main, .col-side { display: flex; flex-direction: column; gap: 1.5rem; }
/* Make history span full width */
.col-main + .col-side + * { grid-column: 1 / -1; }

@media (max-width: 900px) {
  .bento-grid { grid-template-columns: 1fr; }
}
</style>