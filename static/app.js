// =========================
// 🌐 CONFIG (LOCKED)
// =========================
const API_URL = "/rankings";
const PREDICT_URL = "/predict";


// =========================
// 🌐 GLOBAL STATE
// =========================
let controller = null;
let fullData = [];
let currentViewData = [];
let chartInstance = null;
let previousRanks = {};
let geoData = null;

let projection = null;
let path = null;

let requestId = 0;
let polling = false;
let pollTimer = null;
let simTimeout = null;


// =========================
// 🔢 SAFE UTILS
// =========================
const toNum = (v) => {
  const n = Number(v);
  return Number.isFinite(n) ? n : 0;
};

const safeMul = (a, b) =>
  Number((toNum(a) * toNum(b)).toFixed(4));


// =========================
// 🧠 RANK ENGINE (DETERMINISTIC)
// =========================
function recomputeRanks(data) {
  return [...data]
    .sort((a, b) => toNum(b.Score) - toNum(a.Score))
    .map((d, i) => ({ ...d, Rank: i + 1 }));
}


// =========================
// 🌍 GEO DATA (CACHED)
// =========================
async function getGeoData() {
  if (!geoData) {
    try {
      geoData = await d3.json(
        "https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson"
      );
    } catch {
      geoData = { features: [] };
    }
  }
  return geoData;
}


// =========================
// 🔁 SAFE FETCH (FINAL HARDENED)
// =========================
async function safeFetch(url, options = {}, retries = 2) {
  try {
    const { signal, ...rest } = options || {};

    const res = await fetch(url, {
      cache: "no-store",
      ...rest,
      signal
    });

    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();

  } catch (err) {

    // 🔒 CRITICAL: propagate abort (deterministic cancel)
    if (err.name === "AbortError") {
      throw err;
    }

    if (retries > 0) {
      await new Promise(r => setTimeout(r, 400));
      return safeFetch(url, {}, retries - 1);
    }

    console.error("Fetch failed:", url, err);
    throw err;
  }
}


// =========================
// 🚀 LOAD DATA (RACE SAFE)
// =========================
async function loadData() {
  const currentId = ++requestId;
  const loading = document.getElementById("loading");

  if (controller) controller.abort();
  controller = new AbortController();

  try {
    if (loading) {
      loading.style.display = "flex";
      loading.innerText = "Loading intelligence data...";
      loading.style.color = "#9ca3af";
    }

    const json = await safeFetch(API_URL, {
      signal: controller.signal
    });

    if (currentId !== requestId) return;

    fullData = Object.freeze((json?.data || []).map(d => ({ ...d })));

    await loadPrediction(currentId);

    if (loading) loading.style.display = "none";

    renderAll(recomputeRanks(fullData));

  } catch (err) {

    // 🔒 clean abort exit (no UI corruption)
    if (err.name === "AbortError") return;

    if (loading) {
      loading.style.display = "flex";
      loading.innerText = "⚠️ Data load failed";
      loading.style.color = "red";
    }

  } finally {
    controller = null;
  }
}


// =========================
// 🤖 PREDICTION
// =========================
async function loadPrediction(currentId) {
  try {
    const pred = await safeFetch(PREDICT_URL);

    if (!pred || currentId !== requestId) return;

    const map = {};
    pred.forEach(p => {
      map[p.Country] = toNum(p.PredictedScore);
    });

    fullData = fullData.map(d => ({
      ...d,
      predicted: map[d.Country] ?? null
    }));

  } catch {
    console.warn("Prediction skipped");
  }
}


// =========================
// 🔁 POLLING CONTROL (LEAK SAFE)
// =========================
function startPolling() {
  if (polling) return;
  polling = true;

  const loop = async () => {
    if (!polling) return;
    await loadData();
    pollTimer = setTimeout(loop, 15000);
  };

  loop();
}

function stopPolling() {
  polling = false;
  if (pollTimer) clearTimeout(pollTimer);
}


// 🔒 visibility control
document.addEventListener("visibilitychange", () => {
  document.hidden ? stopPolling() : startPolling();
});

// 🔒 HARD CLEANUP
window.addEventListener("beforeunload", () => {
  stopPolling();
  if (controller) controller.abort();
});


// =========================
// 🎯 RENDER PIPELINE
// =========================
function renderAll(data) {
  currentViewData = data;
  renderTable(data);
  renderChart(data);
  renderMap(data);
}


// =========================
// 📊 TABLE
// =========================
function renderTable(rows) {
  const table = document.getElementById("table");
  const leaderEl = document.getElementById("leader");

  if (!rows.length) {
    if (table) table.innerHTML = "";
    if (leaderEl) leaderEl.innerHTML = "No data";
    return;
  }

  const fragment = document.createDocumentFragment();
  const newRanks = {};

  const leader = rows[0];

  if (leaderEl) {
    leaderEl.innerHTML = `
      <div style="font-size:20px;font-weight:bold">${leader.Country}</div>
      <div>Score: ${toNum(leader.Score)}</div>
      <div>Predicted: ${toNum(leader.predicted ?? "-")}</div>
      <div class="${tierClass(leader.Tier)}">${leader.Tier}</div>
    `;
  }

  rows.forEach(r => {
    const prev = previousRanks[r.Country];
    const change = prev ? prev - r.Rank : 0;

    const tr = document.createElement("tr");

    if (change > 0) tr.classList.add("flash-up");
    if (change < 0) tr.classList.add("flash-down");

    tr.innerHTML = `
      <td>${r.Rank}</td>
      <td>${r.Country}</td>
      <td>${toNum(r.Score)}</td>
      <td>${toNum(r.predicted ?? "-")}</td>
      <td class="${tierClass(r.Tier)}">${r.Tier}</td>
    `;

    fragment.appendChild(tr);
    newRanks[r.Country] = r.Rank;
  });

  if (table) {
    table.innerHTML = "";
    table.appendChild(fragment);
  }

  previousRanks = newRanks;
}


// =========================
// 🖱️ ROW CLICK
// =========================
document.getElementById("table")?.addEventListener("click", (e) => {
  const row = e.target.closest("tr");
  if (!row) return;

  const country = row.children[1].innerText;
  const r = currentViewData.find(d => d.Country === country);
  if (!r) return;

  const detail = document.getElementById("countryDetail");
  if (!detail) return;

  detail.innerHTML = `
    <h3>${r.Country}</h3>
    <p>Rank: ${r.Rank}</p>
    <p>Score: ${r.Score}</p>
    <p>Predicted: ${r.predicted ?? "-"}</p>
    <p>Tier: ${r.Tier}</p>
  `;
});


// =========================
// 🎨 TIER CLASS
// =========================
function tierClass(t) {
  if (!t) return "";
  if (t.includes("A")) return "tier-a";
  if (t.includes("B")) return "tier-b";
  if (t.includes("C")) return "tier-c";
  return "tier-d";
}


// =========================
// 📈 CHART
// =========================
function renderChart(data) {
  const ctx = document.getElementById("chart");
  if (!ctx) return;

  const top = data.slice(0, 10);

  if (chartInstance) {
    chartInstance.data.labels = top.map(d => d.Country);

    if (chartInstance.data.datasets[0]) {
      chartInstance.data.datasets[0].data = top.map(d => toNum(d.Score));
    }

    if (chartInstance.data.datasets[1]) {
      chartInstance.data.datasets[1].data = top.map(d => toNum(d.predicted ?? 0));
    }

    chartInstance.update();
    return;
  }

  chartInstance = new Chart(ctx, {
    data: {
      labels: top.map(d => d.Country),
      datasets: [
        { type: "bar", label: "Score", data: top.map(d => toNum(d.Score)) },
        { type: "line", label: "Predicted", data: top.map(d => toNum(d.predicted ?? 0)), borderDash: [5, 5] }
      ]
    }
  });
}


// =========================
// 🌍 MAP
// =========================
async function renderMap(data) {
  const svg = d3.select("#worldMap");
  const geo = await getGeoData();
  if (!geo.features.length) return;

  if (!projection) {
    projection = d3.geoMercator().fitSize([1000, 500], geo);
    path = d3.geoPath().projection(projection);
  }

  const scoreMap = {};
  data.forEach(d => scoreMap[d.Country] = toNum(d.Score));

  const intensity = Number(document.getElementById("intensity")?.value || 1);

  const color = d3.scaleSequential(d3.interpolateYlGnBu)
    .domain([0, 100]);

  svg.selectAll("path")
    .data(geo.features)
    .join("path")
    .attr("d", path)
    .attr("stroke", "#222")
    .attr("fill", d => {
      const s = scoreMap[d.properties.name];
      return s ? color(s * intensity) : "#111";
    });
}


// =========================
// 🎚️ SIMULATION
// =========================
document.getElementById("adjust")?.addEventListener("input", (e) => {
  clearTimeout(simTimeout);

  simTimeout = setTimeout(() => {
    const val = Number(e.target.value);

    const simulated = fullData.map(d => ({
      ...d,
      Score: safeMul(d.Score, (1 + val / 100))
    }));

    renderAll(recomputeRanks(simulated));
  }, 100);
});


// =========================
// ⚖️ POLICY ENGINE
// =========================
document.getElementById("risk")?.addEventListener("input", (e) => {
  const eps = Number(e.target.value);

  const updated = fullData.map(d => ({
    ...d,
    Score: safeMul(d.QSSI_adj ?? d.Score, eps)
  }));

  renderAll(recomputeRanks(updated));
});


// =========================
// 🌡️ MAP INTENSITY
// =========================
document.getElementById("intensity")?.addEventListener("input", () => {
  renderMap(currentViewData);
});


// =========================
// INIT
// =========================
document.addEventListener("DOMContentLoaded", () => {
  loadData();
  startPolling();
});
