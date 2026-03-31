from fastapi import FastAPI
import csv
import os

app = FastAPI()

def load_data():
    data = []

    # Absolute path fix (VERY IMPORTANT for Railway)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "dataset", "qssi_data.csv")

    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pqc = float(row['PQC'])
            ai = float(row['AI'])
            legal = float(row['LEGAL'])
            res = float(row['RES'])
            risk = float(row['Risk'])

            score = 100 * (0.25*pqc + 0.25*ai + 0.25*legal + 0.25*res)
            adjusted = score * (1 - risk)

            data.append({
                "Country": row["Country"],
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
