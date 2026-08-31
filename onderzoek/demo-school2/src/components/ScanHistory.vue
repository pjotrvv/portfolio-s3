<script setup>
// 1. Define Inputs (Props)
// We expect a 'history' object passed down from the parent
const props = defineProps({
  history: {
    type: Object,
    default: () => ({ total: 0, scans: [] })
  }
});

// 2. Define Output Events
const emit = defineEmits(['clear']);

function formatTime(isoString) {
  const date = new Date(isoString);
  return date.toLocaleDateString() + ' ' + date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}
</script>

<template>
  <div class="card history-section">
    <div class="history-header">
      <div class="header-left">
        <div class="card-icon">📜</div>
        <h2>Scan History</h2>
      </div>
      <div class="header-right">
        <span class="history-count">{{ history?.total || 0 }} total scans</span>
        <button class="btn btn-danger" @click="$emit('clear')">Clear History</button>
      </div>
    </div>

    <table class="history-table" v-if="history?.scans?.length">
      <thead>
        <tr>
          <th>Text Preview</th>
          <th>Result</th>
          <th>Toxic Labels (%)</th>
          <th>Time</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="scan in history.scans" :key="scan.id || scan.scanned_at">
          <td class="history-text" :title="scan.text_preview">
            {{ scan.text_preview }}
          </td>
          <td>
            <span :class="['history-badge', scan.is_profane ? 'toxic' : 'safe']">
              {{ scan.is_profane ? '⚠️ Toxic' : '✅ Safe' }}
            </span>
          </td>
          <td>
            <div v-if="scan.toxic_labels?.length" class="mini-labels">
              <span v-for="l in scan.toxic_labels" :key="l.label" class="mini-label">
                {{ l.label }}: {{ (l.score * 100).toFixed(0) }}%
              </span>
            </div>
            <span v-else class="text-safe">None</span>
          </td>
          <td class="history-time">{{ formatTime(scan.scanned_at) }}</td>
        </tr>
      </tbody>
    </table>

    <div v-else class="history-empty">
      No scans yet. Start by analyzing some text above!
    </div>
  </div>
</template>

<style scoped>
/* Ensure labels look clean with the percentages */
.mini-labels {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}
.mini-label {
  font-size: 0.7rem;
  background: rgba(239, 68, 68, 0.15);
  color: var(--danger);
  padding: 2px 8px;
  border-radius: 4px;
  border: 1px solid rgba(239, 68, 68, 0.2);
  font-weight: 600;
}
.text-safe {
  color: var(--success);
  font-size: 0.85rem;
}
</style>