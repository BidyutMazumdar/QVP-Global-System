from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import csv
import os

app = FastAPI()


def load_data():
    data = []

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "dataset", "qssi_data.csv")

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

            score = 100 * (0.25 * pqc + 0.25 * ai + 0.25 * legal + 0.25 * res)
            adjusted = score * (1 - risk)

            data.append({
                "Country": row.get("COUNTRY", "Unknown"),
                "QSSI": round(score, 2),
                "Adjusted": round(adjusted, 2)
            })

    return sorted(data, key=lambda x: x["Adjusted"], reverse=True)


@app.get("/")
def home():
    return {"message": "QVP Global Security Index API is running"}


@app.get("/rankings")
def rankings():
    return load_data()


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>QVP Global Dashboard</title>
    </head>
    <body>
        <h1>QVP Global Security Index</h1>

        <table border="1" id="data"></table>

        <script>
            fetch('/rankings')
                .then(res => res.json())
                .then(data => {
                    let html = "<tr><th>Rank</th><th>Country</th><th>QSSI</th><th>Adjusted</th></tr>";
                    data.forEach((d,i) => {
                        html += `<tr>
                            <td>${i+1}</td>
                            <td>${d.Country}</td>
                            <td>${d.QSSI}</td>
                            <td>${d.Adjusted}</td>
                        </tr>`;
                    });
                    document.getElementById("data").innerHTML = html;
                });
        </script>
    </body>
    </html>
    """
