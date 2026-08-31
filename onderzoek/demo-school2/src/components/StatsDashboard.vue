<script setup>
import { computed } from 'vue';

const props = defineProps(['stats']);

const chartData = computed(() => {
  if (!props.stats?.average_scores) return [];
  return Object.entries(props.stats.average_scores)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 8);
});
</script>

<template>
  <div class="card stats-section">
    <div class="card-header">
      <div class="card-icon">📈</div>
      <h2>Statistics</h2>
    </div>
    
    <div class="stats-grid" v-if="stats">
      <div class="stat-item">
        <div class="stat-value">{{ stats.total_scans }}</div>
        <div class="stat-label">Total Scans</div>
      </div>
      <div class="stat-item">
        <div class="stat-value">{{ stats.profane_percentage }}%</div>
        <div class="stat-label">Profane %</div>
      </div>
    </div>
  </div>
</template>

<style scoped>

/* Add the grid and chart CSS from original html here */
.stats-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1.25rem; }
.stat-item { padding: 1rem; background: var(--bg-tertiary); border-radius: 10px; text-align: center; }
.stat-value { font-size: 1.5rem; font-weight: 700; color: var(--primary); }
.bar-chart { display: flex; align-items: flex-end; justify-content: space-around; height: 120px; gap: 0.5rem; }
.bar { width: 100%; max-width: 40px; background: var(--primary); border-radius: 4px 4px 0 0; }
.bar-label { font-size: 0.6rem; overflow: hidden; text-overflow: ellipsis; }
.card-header { display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1.25rem; }
.card-icon { background: rgba(139, 92, 246, 0.2); width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; }
</style>