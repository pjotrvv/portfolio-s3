<script setup>
import { ref, computed } from 'vue';

const text = ref('');
const props = defineProps(['isLoading']);
const emit = defineEmits(['analyze']);

const charCount = computed(() => text.value.length);

function handleSubmit() {
  if (!text.value.trim()) return;
  emit('analyze', text.value);
}
</script>

<template>
  <div class="card">
    <div class="card-header">
      <div class="card-icon">📝</div>
      <h2>Input Analysis</h2>
    </div>
    
    <div class="editor-wrapper">
      <textarea 
        v-model="text"
        placeholder="Type or paste content here..."
      ></textarea>
      <div class="editor-footer">
        <span class="count">{{ charCount }} chars</span>
        <button class="btn btn-primary" :disabled="isLoading || !text" @click="handleSubmit">
          {{ isLoading ? 'Analyzing...' : 'Run Scan' }}
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.editor-wrapper {
  background: var(--bg-input);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  padding: 0.5rem;
  transition: border-color 0.2s;
}
.editor-wrapper:focus-within {
  border-color: var(--primary);
  box-shadow: 0 0 0 2px var(--primary-glow);
}
textarea {
  width: 100%;
  min-height: 140px;
  padding: 1rem;
  background: transparent;
  border: none;
  color: var(--text-main);
  font-family: 'Inter', sans-serif;
  font-size: 0.95rem;
  resize: vertical;
}
textarea:focus { outline: none; }
.editor-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 0.5rem 0;
  border-top: 1px solid var(--border-subtle);
}
.count { font-size: 0.8rem; color: var(--text-muted); }
</style>