<script setup>
import { computed } from 'vue';

const props = defineProps(['result']);

// Convert raw scores object to sorted array
const sortedScores = computed(() => {
  if (!props.result?.raw_scores) return [];
  return Object.entries(props.result.raw_scores)
    .sort((a, b) => b[1] - a[1]);
});

const getBarClass = (score) => {
  if (score > 0.7) return 'high';
  if (score > 0.4) return 'medium';
  return 'low';
};
</script>

<template>
  <div class="card">
    <div class="card-header">
      <div class="card-icon">📊</div>
      <h2>Results</h2>
    </div>

    <div v-if="!result" class="empty-state">
      Waiting for input...
    </div>

    <div v-else>
      <div :class="['status-pill', result.profanity ? 'danger' : 'success']">
        <span class="status-dot"></span>
        {{ result.profanity ? 'Toxic Content Detected' : 'Content Safe' }}
      </div>

      <div class="bars-container">
        <div v-for="[label, score] in sortedScores" :key="label" class="bar-row">
          <div class="bar-info">
            <span class="bar-label">{{ label }}</span>
            <span class="bar-value">{{ (score * 100).toFixed(0) }}%</span>
          </div>
          <div class="progress-bg">
            <div 
              class="progress-fill" 
              :class="getBarClass(score)"
              :style="{ width: (score * 100) + '%' }"
            ></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
  :root {
      --success: #34d399;
      --danger: #f87171;
  }
.empty-state { text-align: center; color: var(--text-muted); font-size: 0.9rem; padding: 2rem; border: 1px dashed var(--border-subtle); border-radius: 8px; }
.status-pill {
  display: flex; align-items: center; gap: 8px;
  padding: 1rem; border-radius: 8px; font-weight: 600; margin-bottom: 1.5rem;
}
.status-pill.success { background: rgba(52, 211, 153, 0.1); color: #34d399; }
.status-pill.danger { background: rgba(248, 113, 113, 0.1); color: #f87171; }
.status-dot { width: 8px; height: 8px; border-radius: 50%; background: currentColor; }

/* Bars */
.bars-container { display: flex; flex-direction: column; gap: 1rem; }
.bar-info { display: flex; justify-content: space-between; margin-bottom: 0.4rem; font-size: 0.85rem; }
.bar-label { text-transform: capitalize; color: var(--text-muted); }
.bar-value { font-weight: 600; font-variant-numeric: tabular-nums; }
.progress-bg { height: 6px; background: var(--bg-input); border-radius: 10px; overflow: hidden; }
.progress-fill { height: 100%; border-radius: 10px; transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1); }
.progress-fill.low { background: #34d399; }
.progress-fill.medium { background: #fbbf24; }
.progress-fill.high { background: #f87171; }
</style>