// =========================
// 🎚️ SIMULATION ENGINE (ABSOLUTE FINAL 🔒)
// =========================

let simTimeout = null;
let lastSimValue = null;

// Pure transform (no mutation)
function simulateData(baseData, percent) {
  const factor = 1 + percent / 100;

  return baseData.map(d => ({
    ...d,
    Score: safeMul(d.Score, factor)
  }));
}

// =========================
// 🎛️ EVENT (DEBOUNCED + SAFE)
// =========================
document.getElementById("adjust")?.addEventListener("input", (e) => {
  clearTimeout(simTimeout);

  simTimeout = setTimeout(() => {
    const val = Number(e.target.value);

    if (!Number.isFinite(val)) return;
    if (val === lastSimValue) return;

    if (!Array.isArray(fullData) || !fullData.length) return;

    lastSimValue = val;

    const safePercent = Math.max(-100, Math.min(100, val));

    const simulated = simulateData(fullData, safePercent);

    renderAll(recomputeRanks(simulated));
  }, 100);
});
