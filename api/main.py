from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

import csv
import os
import hashlib
import json
import copy
import logging
from typing import Dict, List

from engine.qssi_engine import compute_qssi

# =========================
# LOGGING
# =========================
logging.basicConfig(level=logging.INFO)

# =========================
# APP INIT
# =========================
app = FastAPI(
    title="QVP™ Global System API",
    description="QSSI™ + OMS-1™ Unified Sovereign Intelligence System",
    version="2026.2 FINAL LOCK"
)

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# BASE PATH
# =========================
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "qssi_data.csv")
STATIC_DIR = os.path.join(BASE_DIR, "static")

DATASET_VERSION = "2026.1"
FORMULA = "QSSI_adj = 100 * (Σ w_i x_i) * (1 - R)"

# =========================
# SAFE FLOAT PARSER
# =========================
def to_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0

# =========================
# HASH FUNCTION
# =========================
def run_hash(data: List[Dict]) -> str:
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(canonical).hexdigest()

# =========================
# ENGINE INIT
# =========================
def safe_init():
    try:
        if not os.path.exists(DATASET_PATH):
            raise Exception("Dataset not found")

        results = []
        errors = []

        with open(DATASET_PATH, "rb") as f:
            raw_bytes = f.read()
            dataset_hash = hashlib.sha256(raw_bytes).hexdigest()

        text_data = raw_bytes.decode("utf-8", errors="replace").splitlines()
        reader = csv.DictReader(text_data)

        for row in reader:
            row_clean = {
                k.strip().upper(): (v.strip() if isinstance(v, str) else v)
                for k, v in row.items()
            }

            try:
                result = compute_qssi(
                    to_float(row_clean.get("PQC")),
                    to_float(row_clean.get("AI")),
                    to_float(row_clean.get("LEGAL")),
                    to_float(row_clean.get("RES")),
                    to_float(row_clean.get("RISK"))
                )
            except Exception as e:
                errors.append({"row": row_clean, "error": str(e)})
                continue

            result["Country"] = row_clean.get("COUNTRY", "Unknown")
            results.append(result)

        results = sorted(results, key=lambda x: x["Score"], reverse=True)

        for i, r in enumerate(results):
            r["Rank"] = i + 1

        for r in results:
            for k, v in r.items():
                if isinstance(v, float):
                    r[k] = round(v, 6)

        return {
            "data": results,
            "errors": errors,
            "dataset_hash": dataset_hash,
            "run_id": run_hash(results)
        }

    except Exception as e:
        logging.error(f"Engine init failed: {e}")
        return {
            "error": str(e),
            "data": [],
            "errors": [],
            "dataset_hash": None,
            "run_id": None
        }

# =========================
# SNAPSHOT CACHE
# =========================
ENGINE_CACHE = safe_init()

# =========================
# STATIC FILES
# =========================
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# =========================
# ROOT
# =========================
@app.get("/", include_in_schema=False)
async def root():
    return {
        "system": "QVP GLOBAL SYSTEM",
        "docs": "/docs",
        "rankings": "/rankings",
        "health": "/health"
    }

# =========================
# DASHBOARD
# =========================
@app.get("/dashboard")
async def dashboard():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

# =========================
# API ENDPOINTS
# =========================

@app.get("/qssi/rankings")
async def rankings():
    return copy.deepcopy(ENGINE_CACHE)

@app.get("/rankings")
async def rankings_alias():
    return copy.deepcopy(ENGINE_CACHE)

@app.get("/top/{n}")
async def top_n(n: int):
    data = ENGINE_CACHE.get("data", [])
    n = max(1, min(n, len(data)))
    return copy.deepcopy(data[:n])

@app.get("/country/{name}")
async def country(name: str):
    data = ENGINE_CACHE.get("data", [])
    result = [
        d for d in data
        if str(d.get("Country", "")).lower() == name.lower()
    ]
    return copy.deepcopy(result or {"error": "Country not found"})

@app.get("/tier/{tier}")
async def tier_filter(tier: str):
    data = ENGINE_CACHE.get("data", [])
    result = [
        d for d in data
        if str(d.get("Tier", "")).lower() == tier.lower()
    ]
    return copy.deepcopy(result)

@app.get("/meta")
async def meta():
    return {
        "version": "2026.2 FINAL LOCK",
        "dataset_version": DATASET_VERSION,
        "dataset_hash": ENGINE_CACHE.get("dataset_hash"),
        "run_id": ENGINE_CACHE.get("run_id"),
        "formula": FORMULA,
        "deterministic": True,
        "reproducible": True,
        "audit_trace": True,
        "snapshot_locked": True
    }

# =========================
# HEALTH CHECK
# =========================
@app.get("/health")
async def health():
    return {"status": "ok"}
