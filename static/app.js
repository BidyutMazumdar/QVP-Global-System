const API_URL = "/rankings";

// =========================
// 🌐 GLOBAL STATE
// =========================
let controller = null;
let fullData = [];
let chartInstance = null;
let lastHash = null;
let previousRanks = {};
let geoData = null;
let debounce;

// MAP CACHE
let mapInitialized = false;
let projection = null;
let path = null;

// POLLING
let polling = false;

// REQUEST GUARD
let requestId = 0;

// =========================
// 🔢 SAFE NUMBER
// =========================
const toNum = (v) => {
  const n = Number(v);
  return Number.isFinite(n) ? n : 0;
};

// =========================
// 🌍 GEO DATA (FAIL-SAFE)
// =========================
async function getGeoData() {
  if (!geoData) {
    try {
      geoData = await d3.json(
        "https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson"
      );
    } catch {
      console.error("GeoJSON load failed");
      geoData = { features: [] };
    }
  }
  return geoData;
}

// =========================
// 🚀 LOAD DATA (FULL SAFE)
// =========================
async function loadData() {
  const currentId = ++requestId;
  const loading = document.getElementById("loading");

  if (controller) controller.abort();
  controller = new AbortController();

  let timeout;

  try {
    timeout = setTimeout(() => controller.abort(), 8000);

    const res = await fetch(API_URL, {
      cache: "no-store",
      signal: controller.signal
    });

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    const json = await res.json();

    // 🛑 RACE GUARD
    if (currentId !== requestId) return;

    if (json.dataset_hash && json.dataset_hash === lastHash) return;
    lastHash = json.dataset_hash;

    fullData = Array.isArray(json.data) ? json.data : [];

    if (loading) loading.style.display = "none";

    renderAll(fullData);

    // ✅ Sync prediction safely
    if (fullData.length) loadPrediction(currentId);

  } catch (err) {
    if (err.name === "AbortError") return;

    if (currentId === requestId && loading) {
      loading.style.display = "block";
      loading.innerText = "⚠️ Failed to load data";
      loading.style.color = "red";
    }

  } finally {
    clearTimeout(timeout);
    controller = null;
  }
}

// =========================
// 🔁 POLLING ENGINE
// =========================
async function startPolling() {
  if (polling) return;
  polling = true;

  while (polling) {
    await loadData();
    await new Promise(r => setTimeout(r, 15000));
  }
}

function stopPolling() {
  polling = false;
}

// TAB VISIBILITY CONTROL
document.addEventListener("visibilitychange", () => {
  document.hidden ? stopPolling() : startPolling();
});

// =========================
// 🔍 COMMAND FILTER
// =========================
document.getElementById("command")?.addEventListener("input", (e) => {
  clearTimeout(debounce);

  debounce = setTimeout(() => {
    const q = e.target.value.toLowerCase().trim();
    let filtered = [...fullData];

    if (q.includes("tier:")) {
      const t = q.split("tier:")[1].trim().toUpperCase();
      filtered = filtered.filter(d => d.Tier?.includes(t));
    }

    if (q.includes("score>")) {
      const v = Number(q.split("score>")[1]);
      filtered = filtered.filter(d => toNum(d.Score) > v);
    }

    if (q.includes("country:")) {
      const c = q.split("country:")[1].trim();
      filtered = filtered.filter(d =>
        d.Country?.toLowerCase().includes(c)
      );
    }

    renderAll(filtered);
  }, 200);
});

// =========================
// 🎯 PIPELINE
// =========================
function renderAll(data) {
  render(data);
  renderChart(data);
  renderMap(data);
}

// =========================
// 🎨 UI RENDER
// =========================
function render(rows) {
  const leaderEl = document.getElementById("leader");
  const top10El = document.getElementById("top10");
  const tableEl = document.getElementById("table");

  if (!rows.length) {
    leaderEl && (leaderEl.innerHTML = "No data");
    top10El && (top10El.innerHTML = "");
    tableEl && (tableEl.innerHTML = "");
    return;
  }

  const newRanks = {};

  const leader = rows[0];
  const prev = previousRanks[leader.Country];
  const delta = prev ? prev - leader.Rank : 0;
  const arrow = delta > 0 ? "↑" : delta < 0 ? "↓" : "→";

  if (leaderEl) {
    leaderEl.innerHTML = `
      <div style="font-size:20px;font-weight:bold">${leader.Country}</div>
      <div>Score: ${toNum(leader.Score)}</div>
      <div class="${tierClass(leader.Tier)}">${leader.Tier}</div>
      <div>Change: ${arrow} ${delta}</div>
    `;
  }

  if (top10El) {
    top10El.innerHTML = "";
    rows.slice(0, 10).forEach(r => {
      const li = document.createElement("li");
      li.textContent = `${r.Rank}. ${r.Country} (${toNum(r.Score)})`;
      top10El.appendChild(li);
    });
  }

  if (tableEl) {
    tableEl.innerHTML = "";

    rows.forEach(r => {
      const prevRank = previousRanks[r.Country];
      const change = prevRank ? prevRank - r.Rank : 0;

      const arrow = change > 0 ? "↑" : change < 0 ? "↓" : "";

      const tr = document.createElement("tr");

      tr.innerHTML = `
        <td>${r.Rank} ${arrow}</td>
        <td>${r.Country}</td>
        <td>${toNum(r.Score)}</td>
        <td class="${tierClass(r.Tier)}">${r.Tier}</td>
      `;

      if (arrow) {
        tr.style.background = change > 0 ? "#063" : "#600";
      }

      tableEl.appendChild(tr);
      newRanks[r.Country] = r.Rank;
    });
  }

  previousRanks = newRanks;
}

// =========================
// 🎯 TIER
// =========================
function tierClass(t) {
  if (!t) return "";
  if (t.includes("A")) return "tier-a";
  if (t.includes("B")) return "tier-b";
  if (t.includes("C")) return "tier-c";
  return "tier-d";
}

// =========================
// 📊 CHART
// =========================
function renderChart(data) {
  const ctx = document.getElementById("chart");
  if (!ctx) return;

  const top = data.slice(0, 10);

  if (chartInstance) {
    chartInstance.data.labels = top.map(d => d.Country);
    chartInstance.data.datasets[0].data = top.map(d => toNum(d.Score));
    chartInstance.update();
    return;
  }

  chartInstance = new Chart(ctx, {
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
// 🌍 MAP (AUTO SCALE SAFE)
// =========================
async function renderMap(data) {
  const svg = d3.select("#worldMap");
  const geo = await getGeoData();

  if (!projection) {
    projection = d3.geoMercator().fitSize([1000, 500], geo);
    path = d3.geoPath().projection(projection);
  }

  const scoreMap = {};
  data.forEach(d => scoreMap[d.Country] = toNum(d.Score));

  const scores = Object.values(scoreMap);
  const min = scores.length ? Math.min(...scores) : 0;
  const max = scores.length ? Math.max(...scores) : 100;

  const color = d3.scaleSequential(d3.interpolateYlGnBu)
    .domain([min, max]);

  if (!mapInitialized) {
    svg.selectAll("path")
      .data(geo.features)
      .enter()
      .append("path")
      .attr("d", path)
      .attr("stroke", "#222")
      .each(function () {
        d3.select(this).append("title");
      });

    mapInitialized = true;
  }

  svg.selectAll("path")
    .transition()
    .duration(300)
    .attr("fill", d => {
      const s = scoreMap[d.properties.name];
      return s ? color(s) : "#111";
    })
    .select("title")
    .text(d => {
      const s = scoreMap[d.properties.name];
      return `${d.properties.name}: ${s ?? "N/A"}`;
    });
}

// =========================
// 🤖 PREDICTION (RACE SAFE)
// =========================
async function loadPrediction(currentId) {
  try {
    const res = await fetch("/predict");
    const pred = await res.json();

    if (currentId !== requestId) return;

    const map = {};
    pred.forEach(p => map[p.Country] = toNum(p.PredictedScore));

    fullData.forEach(d => {
      d.predicted = map[d.Country];
    });

  } catch {}
}

// =========================
// INIT
// =========================
document.addEventListener("DOMContentLoaded", () => {
  loadData();
  startPolling();
});
