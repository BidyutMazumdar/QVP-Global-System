from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import csv
import os
import hashlib
from typing import List, Dict

app = FastAPI(
    title="QSSI™ API v2026.1.1",
    description="Quantum Sovereign Security Index — Deterministic Execution API",
    version="2026.1.1"
)

# =========================
# CONFIGURATION (LOCKED)
# =========================

WEIGHTS = {
    "PQC": 0.30,
    "AI": 0.25,
    "LEGAL": 0.25,
    "RES": 0.20,
}

FORMULA = "QSSI_adj = 100 * (Σ w_i x_i) * (1 - R)"
UNCERTAINTY_BOUND = 5.0
SIGMA = 0.02
DATASET_VERSION = "2026.1"

# =========================
# VALIDATION
# =========================

def validate(value: float) -> float:
    v = float(value)
    if v < 0 or v > 1:
        raise ValueError("Value out of bounds [0,1]")
    return v

# =========================
# CORE ENGINE
# =========================

def classify_tier(score: float) -> str:
    if score >= 85:
        return "Tier A"
    elif score >= 75:
        return "Tier B"
    elif score >= 50:
        return "Tier C"
    return "Tier D"


def compute_uncertainty() -> float:
    eps = (sum([(w * SIGMA) ** 2 for w in WEIGHTS.values()])) ** 0.5 * 100
    return round(min(eps, UNCERTAINTY_BOUND), 2)


def sha256_file(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def load_engine() -> Dict:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "dataset", "qssi_data.csv")

    results = []
    errors = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                row_clean = {k.strip().upper(): v for k, v in row.items()}

                try:
                    pqc = validate(row_clean["PQC"])
                    ai = validate(row_clean["AI"])
                    legal = validate(row_clean["LEGAL"])
                    res = validate(row_clean["RES"])
                    risk = validate(row_clean["RISK"])
                except Exception as e:
                    errors.append({
                        "row": row_clean,
                        "error": str(e)
                    })
                    continue

                qssi = (
                    WEIGHTS["PQC"] * pqc +
                    WEIGHTS["AI"] * ai +
                    WEIGHTS["LEGAL"] * legal +
                    WEIGHTS["RES"] * res
                )

                qssi_scaled = 100 * qssi
                qssi_adj = qssi_scaled * (1 - risk)

                results.append({
                    "Country": row_clean.get("COUNTRY", "Unknown"),
                    "QSSI": round(qssi, 4),
                    "QSSI_scaled": round(qssi_scaled, 2),
                    "QSSI_adj": round(qssi_adj, 2),
                    "ε": compute_uncertainty()
                })

    except FileNotFoundError:
        return {"error": "dataset/qssi_data.csv not found"}

    # =========================
    # INTEGRITY CHECK
    # =========================

    if len(results) < 10:
        return {
            "error": "Insufficient valid data after validation",
            "valid_rows": len(results),
            "errors": errors
        }

    # =========================
    # RANKING
    # =========================

    results = sorted(results, key=lambda x: x["QSSI_adj"], reverse=True)

    for i, r in enumerate(results):
        r["Rank"] = i + 1
        r["Tier"] = classify_tier(r["QSSI_adj"])
        r["Score"] = r["QSSI_adj"]

    return {
        "data": results,
        "errors": errors
    }

# =========================
# API ENDPOINTS
# =========================

@app.get("/")
async def root():
    return {
        "system": "QSSI™ v2026.1.1",
        "status": "LIVE",
        "type": "Deterministic Scientific Execution API",
        "integrity": "ENGINE-ALIGNED + AUDIT-TRACE"
    }


@app.get("/rankings")
async def rankings():
    return load_engine()


@app.get("/top/{n}")
async def top_n(n: int):
    engine_output = load_engine()

    if "data" not in engine_output:
        return engine_output

    data = engine_output["data"]
    n = max(1, min(n, len(data)))

    return data[:n]


@app.get("/country/{name}")
async def country(name: str):
    engine_output = load_engine()

    if "data" not in engine_output:
        return engine_output

    data = engine_output["data"]
    result = [d for d in data if d["Country"].lower() == name.lower()]

    return result or {"error": "Country not found"}


@app.get("/tier/{tier}")
async def tier_filter(tier: str):
    engine_output = load_engine()

    if "data" not in engine_output:
        return engine_output

    data = engine_output["data"]
    return [d for d in data if d["Tier"].lower() == tier.lower()]


@app.get("/meta")
async def meta():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_path = os.path.join(base_dir, "dataset", "qssi_data.csv")

    return {
        "version": "v2026.1.1",
        "dataset_version": DATASET_VERSION,
        "weights": WEIGHTS,
        "formula": FORMULA,
        "uncertainty_model": f"sigma={SIGMA}, bounded ≤ {UNCERTAINTY_BOUND}",
        "dataset_hash": sha256_file(dataset_path) if os.path.exists(dataset_path) else None,
        "deterministic": True,
        "reproducible": True,
        "audit_trace": True
    }


# =========================
# DASHBOARD
# =========================

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    return "<h1>QSSI™ Dashboard — Engine Verified & Audit-Trace Enabled</h1>"
