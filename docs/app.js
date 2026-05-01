// ==========================================
// 🌐 QSSI™ FRONTEND ENGINE — FINAL LOCK ∞
// Deterministic | Race-Safe | Audit-Ready
// ==========================================

// =========================
// 🔧 CONFIGURATION (LOCKED)
// =========================
const CONFIG = Object.freeze({
  API_PRIMARY: "https://qvp-global-system-production.up.railway.app",
  API_FALLBACK: "https://qvp-global-system-production.up.railway.app",

  ENDPOINTS: {
    rankings: "/rankings",
    predict: null
  },

  TIMEOUT: 8000,
  RETRIES: 2,
  POLL_INTERVAL: 15000
});

// =========================
// 🌐 GLOBAL STATE (SEALED)
// =========================
const STATE = Object.seal({
  data: [],
  view: [],
  chart: null,
  controller: null,
  polling: false,
  filter: "",
  requestId: 0
});

let pollTimer = null;
let loadingInProgress = false;

// =========================
// 🔢 SAFE UTILITIES
// =========================
const toNum = (v) => {
  const n = Number(v);
  return Number.isFinite(n) ? n : 0;
};

const sleep = (ms) => new Promise(r => setTimeout(r, ms));

// =========================
// 🌐 FETCH ENGINE
// =========================
async function fetchWithTimeout(url, externalSignal) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), CONFIG.TIMEOUT);

  const signal = externalSignal || controller.signal;

  try {
    const res = await fetch(url, {
      cache: "no-store",
      signal
    });

    clearTimeout(timer);

    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();

  } catch (err) {
    clearTimeout(timer);
    throw err;
  }
}

async function safeFetch(url, signal) {
  for (let i = 0; i <= CONFIG.RETRIES; i++) {
    try {
      return await fetchWithTimeout(url, signal);
    } catch (err) {
      if (err.name === "AbortError") throw err;
      if (i === CONFIG.RETRIES) throw err;
      await sleep(400);
    }
  }
}

// =========================
// 🚀 DATA LOADER (ATOMIC)
// =========================
async function loadData() {
  if (loadingInProgress) return;
  loadingInProgress = true;

  const loading = document.getElementById("loading");
  const id = ++STATE.requestId;

  if (STATE.controller) STATE.controller.abort();
  STATE.controller = new AbortController();

  try {
    if (loading) {
      loading.style.display = "flex";
      loading.innerText = "Loading intelligence data...";
      loading.style.color = "#9ca3af";
    }

    let data;

    try {
      data = await safeFetch(
        CONFIG.API_PRIMARY + CONFIG.ENDPOINTS.rankings,
        STATE.controller.signal
      );
    } catch (err) {
      if (err.name === "AbortError") return;

      console.warn("Primary API failed → fallback");

      data = await safeFetch(
        CONFIG.API_FALLBACK + CONFIG.ENDPOINTS.rankings,
        STATE.controller.signal
      );
    }

    if (id !== STATE.requestId) return;

    // Defensive + immutable
    STATE.data = Object.freeze(
      (Array.isArray(data) ? data : []).map(d => ({ ...d }))
    );

    await loadPrediction();

    if (loading) loading.style.display = "none";

    updateUI();

  } catch (err) {
    if (err.name === "AbortError") return;

    console.error("Data load failed:", err);

    if (loading) {
      loading.innerText = "⚠️ Data load failed";
      loading.style.color = "red";
    }
  } finally {
    STATE.controller = null;
    loadingInProgress = false;
  }
}

// =========================
// 🤖 PREDICTION (SAFE)
// =========================
async function loadPrediction() {
  if (!CONFIG.ENDPOINTS.predict) return;

  try {
    const pred = await safeFetch(
      CONFIG.API_PRIMARY + CONFIG.ENDPOINTS.predict
    );

    if (!Array.isArray(pred)) return;

    const map = {};
    pred.forEach(p => {
      map[p.Country] = toNum(p.PredictedScore);
    });

    // 🔒 preserve immutability
    STATE.data = Object.freeze(
      STATE.data.map(d => ({
        ...d,
        predicted: map[d.Country] ?? null
      }))
    );

  } catch {
    console.warn("Prediction skipped");
  }
}

// =========================
// 🧠 RANK ENGINE
// =========================
function recomputeRanks(data) {
  return [...data]
    .sort((a, b) => toNum(b.Score) - toNum(a.Score))
    .map((d, i) => ({ ...d, Rank: i + 1 }));
}

// =========================
// 🔍 FILTER ENGINE
// =========================
function applyFilter(data, query) {
  if (!query) return data;

  query = query.toLowerCase();

  return data.filter(d => {
    const score = toNum(d.Score);
    const country = (d.Country || "").toLowerCase();
    const tier = (d.TierRaw || "").toLowerCase();

    if (query.includes("tier:a") && tier !== "a") return false;
    if (query.includes("tier:b") && tier !== "b") return false;
    if (query.includes("tier:c") && tier !== "c") return false;

    if (query.includes("score>80") && score <= 80) return false;
    if (query.includes("score>50") && score <= 50) return false;

    if (query.includes("country:india") && country !== "india") return false;

    return true;
  });
}

// =========================
// 🎯 UI UPDATE
// =========================
function updateUI() {
  const processed = recomputeRanks(
    applyFilter(STATE.data, STATE.filter)
  );

  STATE.view = processed;

  renderTable(processed);
  renderChart(processed);
}

// =========================
// 📊 TABLE
// =========================
function renderTable(rows) {
  const table = document.getElementById("table");
  const leader = document.getElementById("leader");

  if (!rows.length) {
    if (table) table.innerHTML = "<tr><td colspan='5'>No data</td></tr>";
    if (leader) leader.innerHTML = "No data";
    return;
  }

  const top = rows[0];

  if (leader) {
    leader.innerHTML = `
      <b>${top.Country}</b><br>
      Score: ${toNum(top.Score)}<br>
      Tier: ${top.Tier}
    `;
  }

  if (table) {
    table.innerHTML = rows.map(r => `
      <tr>
        <td>${r.Rank}</td>
        <td>${r.Country}</td>
        <td>${toNum(r.Score)}</td>
        <td>${toNum(r.predicted ?? "-")}</td>
        <td>${r.Tier}</td>
      </tr>
    `).join("");
  }
}

// =========================
// 📈 CHART
// =========================
function renderChart(data) {
  const ctx = document.getElementById("chart");
  if (!ctx || typeof Chart === "undefined") return;

  const top = data.slice(0, 10);

  if (STATE.chart && typeof STATE.chart.destroy === "function") {
    STATE.chart.destroy();
  }

  STATE.chart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: top.map(d => d.Country),
      datasets: [{
        label: "Score",
        data: top.map(d => toNum(d.Score))
      }]
    }
  });
}

// =========================
// 🔁 POLLING
// =========================
function startPolling() {
  if (STATE.polling) return;

  STATE.polling = true;

  const loop = async () => {
    if (!STATE.polling) return;

    await loadData();
    pollTimer = setTimeout(loop, CONFIG.POLL_INTERVAL);
  };

  loop();
}

function stopPolling() {
  STATE.polling = false;

  if (pollTimer) {
    clearTimeout(pollTimer);
    pollTimer = null;
  }
}

// =========================
// 🔎 FILTER INPUT
// =========================
document.getElementById("command")?.addEventListener("input", (e) => {
  STATE.filter = e.target.value;
  updateUI();
});

// =========================
// 🟢 API CHECK
// =========================
async function checkAPI() {
  try {
    await fetch(CONFIG.API_PRIMARY, { method: "HEAD" });
    console.log("API: ONLINE");
  } catch {
    console.warn("API: OFFLINE");
  }
}

// =========================
// 🔒 LIFECYCLE
// =========================
document.addEventListener("visibilitychange", () => {
  document.hidden ? stopPolling() : startPolling();
});

window.addEventListener("beforeunload", () => {
  stopPolling();
  if (STATE.controller) STATE.controller.abort();
});

// =========================
// 🚀 INIT
// =========================
document.addEventListener("DOMContentLoaded", () => {
  checkAPI();
  loadData();
  startPolling();
});
