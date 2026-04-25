// =========================
// 🌍 MAP ENGINE (ABSOLUTE FINAL 🔒)
// =========================

let geoCache = null;
let projection = null;
let path = null;
let lastSize = { w: 0, h: 0 };

// =========================
// 📦 LOAD GEO
// =========================
async function loadGeo() {
  if (geoCache) return geoCache;

  try {
    geoCache = await d3.json(
      "https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/world.geojson"
    );
  } catch {
    geoCache = { features: [] };
  }

  return geoCache;
}

// =========================
// 🎯 NORMALIZE
// =========================
function normalizeName(name) {
  return (name || "").toLowerCase().trim();
}

// =========================
// 🌍 RENDER MAP (LOCKED)
// =========================
async function renderMap(data) {
  const svg = d3.select("#worldMap");
  if (!svg.node()) return;

  const geo = await loadGeo();
  if (!geo.features.length) return;

  const width = svg.node().clientWidth || 1000;
  const height = svg.node().clientHeight || 500;

  // =========================
  // 🧠 RESIZE-AWARE PROJECTION
  // =========================
  if (width !== lastSize.w || height !== lastSize.h) {
    projection = d3.geoMercator().fitSize([width, height], geo);
    path = d3.geoPath().projection(projection);
    lastSize = { w: width, h: height };
  }

  // =========================
  // 📊 DATA MAP
  // =========================
  const scoreMap = {};
  data.forEach(d => {
    scoreMap[normalizeName(d.Country)] = toNum(d.Score);
  });

  const clamp = (v, min = 0, max = 100) => Math.min(max, Math.max(min, v));

  const intensity = Number(
    document.getElementById("intensity")?.value || 1
  );

  const color = d3.scaleSequential(d3.interpolateYlGnBu)
    .domain([0, 100]);

  // =========================
  // 🔁 JOIN (OPTIMIZED)
  // =========================
  const paths = svg.selectAll("path")
    .data(geo.features, d => d.properties.name);

  const enter = paths.enter()
    .append("path")
    .attr("stroke", "#222");

  const merged = enter.merge(paths);

  merged
    .attr("d", path)
    .attr("fill", d => {
      const name = normalizeName(d.properties.name);
      const score = scoreMap[name];

      if (!score) return "#111";

      return color(clamp(score * intensity));
    });

  paths.exit().remove();

  // =========================
  // ⚡ EVENTS (BIND ONCE)
// =========================
  if (!svg.node().__eventsBound) {
    svg.selectAll("path")
      .on("mouseenter", function (event, d) {
        const name = d.properties.name;
        const val = scoreMap[normalizeName(name)];

        d3.select("#countryDetail").html(`
          <h3>${name}</h3>
          <p>Score: ${val ?? "-"}</p>
        `);

        d3.select(this).attr("stroke", "#fff");
      })
      .on("mouseleave", function () {
        d3.select(this).attr("stroke", "#222");
      });

    svg.node().__eventsBound = true;
  }
}
