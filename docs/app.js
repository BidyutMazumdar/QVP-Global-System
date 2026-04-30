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

let currentFilter = "";

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
    const tier = (d.TierRaw || "").toLowerCase();
    const score = toNum(d.Score);
    const country = (d.Country || "").toLowerCase();

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
// 🌍 GEO DATA
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
// 🌍 COUNTRY NAME FIX
// =========================
const countryAlias = {
  "United States": "United States of America",
  "Russia": "Russian Federation",
  "South Korea": "Korea, Republic of",
  "North Korea": "Korea, Democratic People's Republic of"
};

// =========================
// 🔁 SAFE FETCH
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
    if (err.name === "AbortError") throw err;

    if (retries > 0) {
      await new Promise(r => setTimeout(r, 400));
      return safeFetch(url, {}, retries - 1);
    }

    console.error("Fetch failed:", url, err);
    throw err;
  }
}

// =========================
// 🚀 LOAD DATA
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

    fullData = Object.freeze((json || []).map(d => ({ ...d })));

    await loadPrediction(currentId);

    if (loading) loading.style.display = "none";

    updateUI();

  } catch (err) {
    if (err.name === "AbortError") return;

    if (loading) {
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
  if (!PREDICT_URL) return;

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
// 🔁 POLLING
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

// =========================
// 🎯 UI UPDATE PIPELINE
// =========================
function updateUI() {
  const processed = recomputeRanks(
    applyFilter(fullData, currentFilter)
  );

  currentViewData = processed;

  renderTable(processed);
  renderChart(processed);
  renderMap(processed);
}

// =========================
// 📊 TABLE
// =========================
function renderTable(rows) {
  const table = document.getElementById("table");
  const leaderEl = document.getElementById("leader");

  if (!rows.length) {
    if (table) table.innerHTML = "<tr><td colspan='5'>No matching data</td></tr>";
    if (leaderEl) leaderEl.innerHTML = "No data";
    return;
  }

  const fragment = document.createDocumentFragment();
  const newRanks = {};

  const leader = rows[0];

  if (leaderEl) {
    leaderEl.innerHTML = `
      <div><b>${leader.Country}</b></div>
      <div>Score: ${toNum(leader.Score)}</div>
      <div>Tier: ${leader.Tier}</div>
    `;
  }

  rows.forEach(r => {
    const tr = document.createElement("tr");

    tr.innerHTML = `
      <td>${r.Rank}</td>
      <td>${r.Country}</td>
      <td>${toNum(r.Score)}</td>
      <td>${toNum(r.predicted ?? "-")}</td>
      <td>${r.Tier}</td>
    `;

    fragment.appendChild(tr);
    newRanks[r.Country] = r.Rank;
  });

  table.innerHTML = "";
  table.appendChild(fragment);

  previousRanks = newRanks;
}

// =========================
// 📈 CHART (SAFE)
// =========================
function renderChart(data) {
  const ctx = document.getElementById("chart");
  if (!ctx) return;

  const top = data.slice(0, 10);

  if (chartInstance) {
    chartInstance.destroy();
  }

  chartInstance = new Chart(ctx, {
    type: "bar",
    data: {
      labels: top.map(d => d.Country),
      datasets: [
        { label: "Score", data: top.map(d => toNum(d.Score)) }
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
  data.forEach(d => {
    const name = countryAlias[d.Country] || d.Country;
    scoreMap[name] = toNum(d.Score);
  });

  const color = d3.scaleSequential(d3.interpolateYlGnBu)
    .domain([0, 100]);

  svg.selectAll("path")
    .data(geo.features)
    .join("path")
    .attr("d", path)
    .attr("stroke", "#222")
    .attr("fill", d => {
      const s = scoreMap[d.properties.name];
      return s ? color(s) : "#111";
    });
}

// =========================
// 🔎 FILTER INPUT BIND
// =========================
document.getElementById("filterInput")?.addEventListener("input", (e) => {
  currentFilter = e.target.value;
  updateUI();
});

// =========================
// 🔒 VISIBILITY CONTROL
// =========================
document.addEventListener("visibilitychange", () => {
  document.hidden ? stopPolling() : startPolling();
});

window.addEventListener("beforeunload", () => {
  stopPolling();
  if (controller) controller.abort();
});

// =========================
// 🚀 INIT
// =========================
document.addEventListener("DOMContentLoaded", () => {
  loadData();
  startPolling();
});
