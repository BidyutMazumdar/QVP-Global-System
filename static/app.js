const API_URL = "/rankings";

let controller = null;
let fullData = [];
let chartInstance = null;
let lastHash = null;
let previousRanks = {};
let geoData = null;
let debounce;
let mapInitialized = false;

// =========================
// 🔢 SAFE NUMBER PARSER
// =========================
function toNum(v) {
  const n = Number(v);
  return isNaN(n) ? 0 : n;
}

// =========================
// 🌍 GEOJSON CACHE
// =========================
async function getGeoData() {
  if (!geoData) {
    geoData = await d3.json(
      "https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson"
    );
  }
  return geoData;
}

// =========================
// 🚀 LOAD DATA
// =========================
async function loadData() {
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

    if (json.dataset_hash && json.dataset_hash === lastHash) return;
    lastHash = json.dataset_hash;

    fullData = Array.isArray(json.data) ? json.data : [];

    if (loading) loading.style.display = "none";

    renderAll(fullData);

  } catch (err) {
    if (err.name === "AbortError") return;

    if (loading) {
      loading.style.display = "block";
      loading.innerText = "⚠️ Failed to load data";
      loading.style.color = "red";
    }

  } finally {
    if (timeout) clearTimeout(timeout);
    controller = null;
  }
}

// =========================
// 🔍 COMMAND PARSER
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
// 🎯 MAIN PIPELINE
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
    if (leaderEl) leaderEl.innerHTML = "No data";
    if (top10El) top10El.innerHTML = "";
    if (tableEl) tableEl.innerHTML = "";
    return;
  }

  const newRanks = {};

  // Leader
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

  // Top 10
  if (top10El) {
    top10El.innerHTML = "";
    rows.slice(0, 10).forEach(r => {
      const li = document.createElement("li");
      li.textContent = `${r.Rank}. ${r.Country} (${toNum(r.Score)})`;
      top10El.appendChild(li);
    });
  }

  // Table
  if (tableEl) {
    tableEl.innerHTML = "";

    rows.forEach(r => {
      const prevRank = previousRanks[r.Country];
      const change = prevRank ? prevRank - r.Rank : 0;

      let arrow = "";
      if (change > 0) arrow = "↑";
      else if (change < 0) arrow = "↓";

      const tr = document.createElement("tr");

      tr.innerHTML = `
        <td>${r.Rank} ${arrow}</td>
        <td>${r.Country}</td>
        <td>${toNum(r.Score)}</td>
        <td class="${tierClass(r.Tier)}">${r.Tier}</td>
      `;

      if (arrow) {
        tr.style.transition = "all 0.3s ease-in-out";
        tr.style.background = change > 0 ? "#063" : "#600";
      }

      tableEl.appendChild(tr);
      newRanks[r.Country] = r.Rank;
    });
  }

  previousRanks = newRanks;
}

// =========================
// 🎯 TIER CLASS
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
// 🌍 MAP
// =========================
async function renderMap(data) {
  const svg = d3.select("#worldMap");
  const geo = await getGeoData();

  const projection = d3.geoMercator().fitSize([1000, 500], geo);
  const path = d3.geoPath().projection(projection);

  const scoreMap = {};
  data.forEach(d => scoreMap[d.Country] = toNum(d.Score));

  const color = d3.scaleSequential(d3.interpolateYlGnBu)
    .domain([40, 90]);

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
// 🎛️ SIMULATION
// =========================
document.getElementById("adjust")?.addEventListener("input", (e) => {
  const val = Number(e.target.value);

  const simulated = fullData.map(d => ({
    ...d,
    Score: toNum(d.Score) + val
  }));

  renderAll(simulated);
});

// =========================
// ⚙️ POLICY ENGINE
// =========================
document.getElementById("risk")?.addEventListener("input", (e) => {
  const epsilon = Number(e.target.value);

  const updated = fullData.map(d => ({
    ...d,
    Score: toNum(d.Score) * epsilon
  }));

  renderAll(updated);
});

// =========================
// 🔁 AUTO REFRESH
// =========================
setInterval(loadData, 15000);

// =========================
// 🤖 AI PREDICTION
// =========================
async function loadPrediction() {
  try {
    const res = await fetch("/predict");
    const pred = await res.json();

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
  loadPrediction();
});
