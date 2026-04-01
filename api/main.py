from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import csv
import os

app = FastAPI(
    title="QSSI™ API v2026.1.1",
    description="Quantum Sovereign Security Index Global Rankings API",
    version="2026.1.1"
)

# Official QSSI methodology weights
WEIGHTS = {
    "PQC": 0.30,
    "AI": 0.25,
    "LEGAL": 0.25,
    "RES": 0.20,
}


def classify_tier(score: float) -> str:
    """Official QSSI tier classification"""
    if score >= 85:
        return "Tier A"
    elif score >= 75:
        return "Tier B"
    elif score >= 50:
        return "Tier C"
    return "Tier D"


def load_data():
    """Load QSSI dataset and calculate rankings using official methodology"""
    data = []

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "dataset", "qssi_data.csv")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                row = {k.strip().upper(): v for k, v in row.items()}

                try:
                    pqc = float(row.get("PQC", 0))
                    ai = float(row.get("AI", 0))
                    legal = float(row.get("LEGAL", 0))
                    res = float(row.get("RES", 0))
                    risk = float(row.get("RISK", 0))
                except (ValueError, TypeError):
                    continue

                qssi = 100 * (
                    WEIGHTS["PQC"] * pqc +
                    WEIGHTS["AI"] * ai +
                    WEIGHTS["LEGAL"] * legal +
                    WEIGHTS["RES"] * res
                )

                adjusted = qssi * (1 - risk)

                data.append({
                    "Country": row.get("COUNTRY", "Unknown"),
                    "QSSI": round(qssi, 2),
                    "QSSI_adj": round(adjusted, 2),
                    "Tier": classify_tier(adjusted),
                    "Risk": round(risk * 100)
                })

    except FileNotFoundError:
        return [{"error": "qssi_data.csv not found in dataset/"}]

    return sorted(data, key=lambda x: x["QSSI_adj"], reverse=True)


@app.get("/")
async def home():
    return {
        "QSSI": "v2026.1.1 LIVE",
        "Status": "Operational",
        "TopRanked": "Finland",
        "Tier": "Tier A",
        "Methodology": "Official QSSI Weighted Model"
    }


@app.get("/rankings")
async def rankings():
    return load_data()


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QSSI™ Global Rankings v2026.1.1</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body class="bg-gradient-to-br from-slate-50 via-blue-50 to-indigo-100 min-h-screen p-6">
    <div class="max-w-7xl mx-auto">

        <div class="text-center mb-12">
            <h1 class="text-6xl font-black bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent mb-4">
                QSSI™ Global Rankings
            </h1>
            <p class="text-2xl text-gray-700 font-medium">Quantum Sovereign Security Index</p>
            <p class="text-lg text-blue-600 font-semibold mt-2">v2026.1.1 | Official Production Dashboard</p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-10">
            <div class="bg-white rounded-3xl p-8 shadow-xl border border-slate-200">
                <h3 class="text-2xl font-bold text-gray-800 mb-3">Global Leader</h3>
                <div class="text-4xl font-black text-emerald-600 mb-2">Finland</div>
                <div class="text-xl font-bold text-gray-700">QSSI Adj: 85.97</div>
                <span class="inline-block mt-4 px-4 py-2 bg-emerald-100 text-emerald-700 rounded-full font-semibold text-sm">
                    Tier A
                </span>
            </div>

            <div class="bg-white rounded-3xl p-8 shadow-xl border border-slate-200">
                <h3 class="text-xl font-bold text-gray-800 mb-4">Tier Distribution</h3>
                <canvas id="tierChart"></canvas>
            </div>

            <div class="bg-white rounded-3xl p-8 shadow-xl border border-slate-200">
                <h3 class="text-xl font-bold text-gray-800 mb-4">Top 5 Countries</h3>
                <div id="liveTop5" class="space-y-3"></div>
            </div>
        </div>

        <div class="bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden">
            <div class="flex flex-col md:flex-row justify-between items-center p-8 border-b border-slate-200 gap-4">
                <h2 class="text-3xl font-bold text-gray-800">Global Rankings Table</h2>

                <select id="tierFilter" class="px-5 py-3 rounded-2xl border border-slate-300 bg-slate-50 font-medium shadow-sm">
                    <option>All Tiers</option>
                    <option>Tier A</option>
                    <option>Tier B</option>
                    <option>Tier C</option>
                    <option>Tier D</option>
                </select>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-sm text-left">
                    <thead>
                        <tr class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white">
                            <th class="p-5">Rank</th>
                            <th class="p-5">Country</th>
                            <th class="p-5">QSSI</th>
                            <th class="p-5">QSSI Adj</th>
                            <th class="p-5">Risk %</th>
                            <th class="p-5">Tier</th>
                        </tr>
                    </thead>
                    <tbody id="rankingsTable"></tbody>
                </table>
            </div>
        </div>
    </div>

    <script>
        let allData = [];

        async function loadData() {
            try {
                const res = await fetch('/rankings');
                allData = await res.json();

                if (allData[0]?.error) {
                    document.body.innerHTML = `<div class="text-center mt-20 text-red-600 text-3xl font-bold">${allData[0].error}</div>`;
                    return;
                }

                renderTable(allData);
                renderTop5(allData);
                renderCharts();
            } catch (error) {
                console.error(error);
            }
        }

        function renderTable(data = allData) {
            const tbody = document.getElementById('rankingsTable');
            const selectedTier = document.getElementById('tierFilter').value;

            const filtered = selectedTier === 'All Tiers'
                ? data
                : data.filter(d => d.Tier === selectedTier);

            tbody.innerHTML = filtered.map((d, i) => {
                const tierColor =
                    d.Tier === 'Tier A' ? 'bg-emerald-100 text-emerald-700' :
                    d.Tier === 'Tier B' ? 'bg-blue-100 text-blue-700' :
                    d.Tier === 'Tier C' ? 'bg-amber-100 text-amber-700' :
                    'bg-red-100 text-red-700';

                return `
                    <tr class="border-b border-slate-100 hover:bg-slate-50 transition-all">
                        <td class="p-5 font-bold text-blue-600">${i + 1}</td>
                        <td class="p-5 font-semibold text-gray-800">${d.Country}</td>
                        <td class="p-5 text-gray-700 font-bold">${d.QSSI}</td>
                        <td class="p-5 text-emerald-600 font-bold">${d.QSSI_adj}</td>
                        <td class="p-5 text-gray-600 font-semibold">${d.Risk}%</td>
                        <td class="p-5">
                            <span class="px-4 py-2 rounded-full text-sm font-bold ${tierColor}">
                                ${d.Tier}
                            </span>
                        </td>
                    </tr>
                `;
            }).join('');
        }

        document.getElementById('tierFilter').addEventListener('change', () => renderTable());

        function renderTop5(data) {
            document.getElementById('liveTop5').innerHTML = data.slice(0, 5).map((d, i) => `
                <div class="flex justify-between items-center bg-slate-50 rounded-2xl px-4 py-3">
                    <div>
                        <span class="font-bold text-blue-600">#${i + 1}</span>
                        <span class="ml-2 font-semibold text-gray-800">${d.Country}</span>
                    </div>
                    <div class="font-bold text-emerald-600">${d.QSSI_adj}</div>
                </div>
            `).join('');
        }

        function renderCharts() {
            const tierCounts = {
                'Tier A': allData.filter(d => d.Tier === 'Tier A').length,
                'Tier B': allData.filter(d => d.Tier === 'Tier B').length,
                'Tier C': allData.filter(d => d.Tier === 'Tier C').length,
                'Tier D': allData.filter(d => d.Tier === 'Tier D').length
            };

            new Chart(document.getElementById('tierChart'), {
                type: 'doughnut',
                data: {
                    labels: Object.keys(tierCounts),
                    datasets: [{
                        data: Object.values(tierCounts)
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'bottom'
                        }
                    }
                }
            });
        }

        loadData();
    </script>
</body>
</html>
"""
