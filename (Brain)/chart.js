// =========================
// 📈 CHART (ABSOLUTE FINAL 🔒)
// =========================
function renderChart(data) {
  const canvas = document.getElementById("chart");
  if (!canvas) return;

  const ctx = canvas.getContext("2d");

  // =========================
  // 🧠 DPI / RETINA FIX
  // =========================
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();

  if (canvas.width !== rect.width * dpr || canvas.height !== rect.height * dpr) {
    canvas.width = rect.width * dpr;
    canvas.height = rect.height * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  // =========================
  // 🎯 SAFE TOP N
  // =========================
  const TOP_N = 10;

  const sorted = [...data].sort((a, b) => toNum(b.Score) - toNum(a.Score));
  const top = sorted.slice(0, TOP_N);

  const labels = top.map(d => d.Country);

  // 🛡️ Clamp protection
  const clamp = (v, min = 0, max = 100) => Math.min(max, Math.max(min, v));

  const scoreData = top.map(d => clamp(toNum(d.Score)));
  const predictedData = top.map(d => clamp(toNum(d.predicted ?? 0)));

  // =========================
  // 🧯 MEMORY SAFETY
  // =========================
  if (chartInstance && chartInstance.canvas !== canvas) {
    chartInstance.destroy();
    chartInstance = null;
  }

  // =========================
  // 🔁 SAFE UPDATE
  // =========================
  if (chartInstance) {
    chartInstance.data.labels = labels;

    if (chartInstance.data.datasets[0]) {
      chartInstance.data.datasets[0].data = scoreData;
    }

    if (chartInstance.data.datasets[1]) {
      chartInstance.data.datasets[1].data = predictedData;
    }

    chartInstance.update("none"); // no animation for polling
    return;
  }

  // =========================
  // 🚀 CREATE (IMMUTABLE)
  // =========================
  chartInstance = new Chart(ctx, {
    type: "bar",
    data: {
      labels,
      datasets: [
        {
          label: "Score",
          data: scoreData,
          borderWidth: 1,
          borderRadius: 6,
          maxBarThickness: 32
        },
        {
          type: "line",
          label: "Predicted",
          data: predictedData,
          tension: 0.35,
          borderWidth: 2,
          pointRadius: 3,
          borderDash: [6, 4],
          fill: false
        }
      ]
    },

    options: {
      responsive: true,
      maintainAspectRatio: false,

      interaction: {
        mode: "index",
        intersect: false
      },

      animation: false, // 🔥 critical for real-time

      plugins: {
        legend: {
          labels: {
            color: "#9ca3af",
            font: { size: 12 }
          }
        },

        tooltip: {
          backgroundColor: "#111827",
          borderColor: "#1f2937",
          borderWidth: 1,
          titleColor: "#e5e7eb",
          bodyColor: "#9ca3af",
          padding: 10,
          displayColors: false,
          callbacks: {
            label: (ctx) => {
              const val = toNum(ctx.raw);
              return `${ctx.dataset.label}: ${val}`;
            }
          }
        }
      },

      scales: {
        x: {
          ticks: {
            color: "#9ca3af",
            maxRotation: 45,
            minRotation: 30
          },
          grid: {
            display: false
          }
        },

        y: {
          beginAtZero: true,
          ticks: {
            color: "#9ca3af"
          },
          grid: {
            color: "rgba(255,255,255,0.05)"
          }
        }
      }
    }
  });
}
