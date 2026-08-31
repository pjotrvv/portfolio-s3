import { ref } from 'vue';

const API_BASE = 'http://localhost:8000';

export function useApi() {
  const isConnected = ref(false);

  const checkHealth = async () => {
    try {
      const res = await fetch(`${API_BASE}/health`, { method: 'POST' });
      isConnected.value = res.ok;
    } catch (e) {
      isConnected.value = false;
    }
  };

  const analyzeText = async (text) => {
    const res = await fetch(`${API_BASE}/detect`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });
    if (!res.ok) throw new Error('Analysis failed');
    return await res.json();
  };

  const getStats = async () => {
    const res = await fetch(`${API_BASE}/stats`);
    if (!res.ok) return null;
    return await res.json(); // JUST return the data
  };

  const getHistory = async (limit = 50) => {
    const res = await fetch(`${API_BASE}/scans/history?limit=${limit}`);
    return res.ok ? await res.json() : null;
  };

  const getThreshold = async () => {
    const res = await fetch(`${API_BASE}/threshold`);
    return res.ok ? await res.json() : null;
  };

  const setThreshold = async (val) => {
    await fetch(`${API_BASE}/threshold?new_threshold=${val}`, { method: 'POST' });
  };

  const clearHistory = async () => {
    await fetch(`${API_BASE}/scans/clear`, { method: 'DELETE' });
  };

  return {
    isConnected,
    checkHealth,
    analyzeText,
    getStats,
    getHistory,
    getThreshold,
    setThreshold,
    clearHistory
  };
}