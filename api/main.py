from fastapi import FastAPI, HTTPException, Header
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import os, csv, json, hashlib, asyncio, logging
from typing import Dict
from asyncio import Lock
from contextlib import asynccontextmanager

from engine.qssi_engine import compute_qssi

# =========================
# 🔐 CONFIG
# =========================

API_KEY = os.getenv("API_KEY", "dev-key")
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "qssi_data.csv")
STATIC_DIR = os.path.join(BASE_DIR, "static")

# =========================
# 🧠 LOGGING
# =========================

logging.basicConfig(level=logging.INFO)

# =========================
# ⚡ CACHE
# =========================

ENGINE_CACHE: Dict = {}
CACHE_LOCK = Lock()

# =========================
# 🔧 UTILS
# =========================

def to_float(x):
    try:
        return float(str(x).strip())
    except:
        return 0.0

def canonical_json(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":"))

def run_hash(data):
    return hashlib.sha256(canonical_json(data).encode()).hexdigest()

def ensure_ready():
    if "data" not in ENGINE_CACHE:
        raise HTTPException(503, "Service not ready")

# =========================
# 📊 LOAD ENGINE
# =========================

def safe_init():
    if not os.path.exists(DATASET_PATH):
        logging.error("Dataset missing")
        return {"data": [], "country_index": {}, "dataset_hash": None, "run_id": None}

    results = []

    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            # 🔥 CSV normalization (critical)
            row = {
                k.strip().upper(): v.strip() if isinstance(v, str) else v
                for k, v in row.items()
            }

            try:
                r = compute_qssi(
                    to_float(row.get("PQC")),
                    to_float(row.get("AI")),
                    to_float(row.get("LEGAL")),
                    to_float(row.get("RES")),
                    to_float(row.get("RISK"))
                )
            except Exception as e:
                logging.warning(f"Row skipped: {e}")
                continue

            r["Country"] = row.get("COUNTRY", "Unknown")

            for k in r:
                if isinstance(r[k], float):
                    r[k] = round(r[k], 6)

            results.append(r)

    # 🔐 deterministic sort (safe)
    results.sort(key=lambda x: x.get("Score", 0), reverse=True)

    # 🏁 ranking
    for i, r in enumerate(results):
        r["Rank"] = i + 1

    # ⚡ O(1) lookup index
    country_index = {
        r["Country"].lower().strip(): r for r in results
    }

    return {
        "data": results,
        "country_index": country_index,
        "dataset_hash": hashlib.sha256(
            canonical_json(results).encode()
        ).hexdigest(),
        "run_id": run_hash(results)
    }

# =========================
# 🚀 LIFECYCLE
# =========================

@asynccontextmanager
async def lifespan(app: FastAPI):
    global ENGINE_CACHE
    loop = asyncio.get_running_loop()

    try:
        ENGINE_CACHE = await loop.run_in_executor(None, safe_init)
        logging.info("System ready")
    except Exception as e:
        logging.error(f"Startup failed: {e}")
        ENGINE_CACHE = {"data": [], "country_index": {}, "dataset_hash": None, "run_id": None}

    yield

# =========================
# 🌐 APP
# =========================

app = FastAPI(
    title="QVP Global System",
    version="v2.0.0-ABSOLUTE-FINAL-LOCK",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"]
)

# static safe mount
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# =========================
# 🌍 ROUTES
# =========================

@app.get("/")
async def root():
    return {"system": "QVP", "status": "ok"}

@app.get("/dashboard")
async def dashboard():
    path = os.path.join(STATIC_DIR, "index.html")
    if not os.path.exists(path):
        raise HTTPException(404, "Dashboard not found")
    return FileResponse(path)

@app.get("/rankings")
async def rankings():
    async with CACHE_LOCK:
        ensure_ready()
        return ENGINE_CACHE["data"]

@app.get("/country/{name}")
async def country(name: str):
    async with CACHE_LOCK:
        ensure_ready()
        r = ENGINE_CACHE["country_index"].get(name.lower().strip())
        if r:
            return r
        raise HTTPException(404, "Not found")

@app.get("/top/{n}")
async def top(n: int):
    async with CACHE_LOCK:
        ensure_ready()
        data = ENGINE_CACHE["data"]
        return data[:max(1, min(n, len(data)))]

@app.get("/meta")
async def meta():
    async with CACHE_LOCK:
        ensure_ready()
        return {
            "run_id": ENGINE_CACHE.get("run_id"),
            "dataset_hash": ENGINE_CACHE.get("dataset_hash"),
            "records": len(ENGINE_CACHE.get("data", []))
        }

@app.get("/health")
async def health():
    data = ENGINE_CACHE.get("data")
    return {
        "status": "ok" if data else "init",
        "records": len(data or []),
        "cache_ready": bool(data)
    }
