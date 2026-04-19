from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import math
import hashlib
import json
import csv
import os

app = FastAPI(
    title="QVP™ Global System API",
    description="QSSI™ + OMS-1™ Unified Sovereign Intelligence System",
    version="2026.1 FINAL LOCK"
)

EPSILON = 0.01

WEIGHTS = {
    "PQC": 0.30,
    "AI": 0.25,
    "LEGAL": 0.25,
    "RES": 0.20,
}

def classify_tier(score: float) -> str:
    if score >= 85:
        return "Tier A"
    elif score >= 75:
        return "Tier B"
    elif score >= 50:
        return "Tier C"
    return "Tier D"

def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))

def load_data():
    data = []
    file_path = os.getenv("QSSI_DATA_PATH", "dataset/qssi_data.csv")

    if not os.path.exists(file_path):
        return [{"error": "qssi_data.csv not found"}]

    try:
        with open(file_path, "r", encoding="utf-8", newline="") as f:
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

                risk = clamp01(risk)

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

    except Exception:
        return [{"error": "Dataset read failure"}]

    return sorted(data, key=lambda x: x["QSSI_adj"], reverse=True)

@app.get("/")
async def root():
    return {
        "System": "QVP GLOBAL SYSTEM",
        "Version": "2026.1 FINAL LOCK",
        "Modules": {
            "QSSI": "/qssi/rankings",
            "OMS-1": "/oms/compute"
        },
        "Status": "Operational",
        "Compliance": [
            "Deterministic Execution",
            "Auditable (SHA-256)",
            "ISO-Grade Design"
        ]
    }

@app.get("/qssi/rankings")
async def rankings():
    data = load_data()
    if data and "error" in data[0]:
        raise HTTPException(status_code=500, detail=data[0]["error"])
    return data

class InputData(BaseModel):
    I: float = Field(..., ge=0, le=1)
    A: float = Field(..., ge=0, le=1)
    R: float = Field(..., ge=0, le=1)
    C: float = Field(..., ge=0, le=1)

class Parameters(BaseModel):
    lambda_: float = Field(..., ge=0, le=1)
    Vt: float = Field(..., ge=0, le=1)
    Rs: float = Field(..., ge=0, le=1)
    Co: float = Field(..., ge=0, le=1)
    AGAPn: float = Field(..., ge=0, le=1)
    weights: List[float] = Field(..., min_items=1)

class RequestModel(BaseModel):
    input: InputData
    parameters: Parameters

def validate_weights(weights: List[float], values: List[float]):
    if len(weights) != len(values):
        raise ValueError("Weights mismatch")
    if any(w < 0 for w in weights):
        raise ValueError("Weights must be non-negative")
    if not math.isclose(sum(weights), 1.0, rel_tol=1e-6):
        raise ValueError("Weights must sum to 1")

def compute_sigma(lambda_, Vt):
    return lambda_ * Vt

def compute_io(weights, values):
    return sum(w * x for w, x in zip(weights, values))

def compute_contributions(I, A, C, R, sigma_t):
    denom = (R + EPSILON) * (1 + sigma_t)
    raw = {
        "I": ((A * C) / denom) * I,
        "A": ((I * C) / denom) * A,
        "C": ((I * A) / denom) * C,
    }
    total = sum(raw.values()) or 1.0
    return {k: round(v / total, 8) for k, v in raw.items()}

def compute_decision(input_data, params):
    I = clamp01(input_data.I)
    A = clamp01(input_data.A)
    R = clamp01(input_data.R)
    C = clamp01(input_data.C)

    sigma_t = compute_sigma(params.lambda_, params.Vt)
    Xi = [I, A, C]

    try:
        validate_weights(params.weights, Xi)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    Io = compute_io(params.weights, Xi)

    denom = max(EPSILON, (R + EPSILON) * (1 + sigma_t))
    Ds_raw = (I * A * C) / denom
    Ds = min(1.0, max(0.0, Ds_raw))

    Cs = Io * params.Rs * params.AGAPn * math.exp(-sigma_t)
    Ad = Cs * params.Co * Io * params.Rs * math.exp(-sigma_t)

    return {
        "Ds": round(Ds, 8),
        "Cs": round(Cs, 8),
        "Ad": round(Ad, 8),
        "sigma_t": round(sigma_t, 8),
        "Io": round(Io, 8),
        "explainability": compute_contributions(I, A, C, R, sigma_t)
    }

def generate_hash(data):
    encoded = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":")
    ).encode()
    return hashlib.sha256(encoded).hexdigest()

@app.post("/oms/compute")
async def oms_compute(request: RequestModel):
    result = compute_decision(request.input, request.parameters)

    audit_data = {
        "input": request.input.model_dump(),
        "parameters": request.parameters.model_dump(),
        "output": result
    }

    return {
        "result": result,
        "audit_hash": generate_hash(audit_data)
    }
