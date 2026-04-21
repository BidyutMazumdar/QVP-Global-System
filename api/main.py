from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import csv
import os
import hashlib
import json
import copy
from typing import Dict, List

from engine.qssi_engine import compute_qssi

app = FastAPI(
    title="QVP™ Global System API",
    description="QSSI™ + OMS-1™ Unified Sovereign Intelligence System",
    version="2026.2 FINAL LOCK"
)

# =========================
# 🔒 BASE PATH (DEPLOYMENT SAFE)
# =========================

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# =========================
# 🔒 TEMPLATE CONFIG (FAIL-SAFE)
# =========================

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

if not os.path.exists(TEMPLATE_DIR):
    raise RuntimeError("Templates directory missing")

templates = Jinja2Templates(directory=TEMPLATE_DIR)

# =========================
# CONFIGURATION
# =========================

DATASET_VERSION = "2026.1"
FORMULA = "QSSI_adj = 100 * (Σ w_i x_i) * (1 - R)"

DATASET_PATH = os.path.join(BASE_DIR, "dataset", "qssi_data.csv")

# =========================
# HASHING (CANONICAL)
# =========================

def run_hash(data: List[Dict]) -> str:
    canonical = json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":")
    ).encode()
    return hashlib.sha256(canonical).hexdigest()

# =========================
# SNAPSHOT ENGINE (TRUE LOCK)
# =========================

def safe_init():
    try:
        if not os.path.exists(DATASET_PATH):
            raise Exception("Dataset not found")

        results = []
        errors = []

        # 🔒 SINGLE READ (HASH + DATA SAME SNAPSHOT)
        with open(DATASET_PATH, "rb") as f:
            raw_bytes = f.read()
            dataset_hash = hashlib.sha256(raw_bytes).hexdigest()

        text_data = raw_bytes.decode("utf-8", errors="replace").splitlines()
        reader = csv.DictReader(text_data)

        for row in reader:
            row_clean = {k.strip().upper(): v for k, v in row.items()}

            try:
                result = compute_qssi(
                    float(row_clean["PQC"]),
                    float(row_clean["AI"]),
                    float(row_clean["LEGAL"]),
                    float(row_clean["RES"]),
                    float(row_clean["RISK"])
                )
            except Exception as e:
                errors.append({
                    "row": row_clean,
                    "error": str(e)
                })
                continue

            result["Country"] = row_clean.get("COUNTRY", "Unknown")
            results.append(result)

        # 🔒 SORT (DETERMINISTIC)
        results = sorted(results, key=lambda x: x["Score"], reverse=True)

        # 🔒 RANK ASSIGNMENT
        for i, r in enumerate(results):
            r["Rank"] = i + 1

        # 🔒 FLOAT NORMALIZATION
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
        return {
            "error": str(e),
            "data": [],
            "errors": [],
            "dataset_hash": None,
            "run_id": None
        }

# =========================
# 🔒 SNAPSHOT LOCK (IMMUTABLE STATE)
# =========================

ENGINE_CACHE = safe_init()

# =========================
# API ENDPOINTS
# =========================

@app.get("/")
async def root():
    return {
        "system": "QVP GLOBAL SYSTEM",
        "version": "2026.2 FINAL LOCK",
        "status": "ABSOLUTE 🔒🔐",
        "snapshot_locked": True
    }


# 🔒 FULL DATA (NO VALIDATION NEEDED)
@app.get("/qssi/rankings")
async def rankings():
    return copy.deepcopy(ENGINE_CACHE)


# 🔒 SAFE FILTERED ENDPOINTS
@app.get("/top/{n}")
async def top_n(n: int):
    if not ENGINE_CACHE.get("data"):
        return copy.deepcopy(ENGINE_CACHE)

    data = ENGINE_CACHE["data"]
    n = max(1, min(n, len(data)))
    return copy.deepcopy(data[:n])


@app.get("/country/{name}")
async def country(name: str):
    if not ENGINE_CACHE.get("data"):
        return copy.deepcopy(ENGINE_CACHE)

    result = [
        d for d in ENGINE_CACHE["data"]
        if d["Country"].lower() == name.lower()
    ]

    return copy.deepcopy(result or {"error": "Country not found"})


@app.get("/tier/{tier}")
async def tier_filter(tier: str):
    if not ENGINE_CACHE.get("data"):
        return copy.deepcopy(ENGINE_CACHE)

    result = [
        d for d in ENGINE_CACHE["data"]
        if d["Tier"].lower() == tier.lower()
    ]

    return copy.deepcopy(result)


# 🔒 META (AUDIT SAFE)
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
# 🔒 DASHBOARD (FINAL UI BINDING)
# =========================

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )
