from fastapi import FastAPI
import csv
import os

app = FastAPI()

def load_data():
    data = []

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "dataset", "qssi_data.csv")

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            row = {k.strip().upper(): v for k, v in row.items()}

            try:
                pqc = float(row.get('PQC', 0))
                ai = float(row.get('AI', 0))
                legal = float(row.get('LEGAL', 0))
                res = float(row.get('RES', 0))
                risk = float(row.get('RISK', 0))
            except ValueError:
                continue

            score = 100 * (0.25*pqc + 0.25*ai + 0.25*legal + 0.25*res)
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
