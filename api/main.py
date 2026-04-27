from fastapi import FastAPI, Header, HTTPException, status
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import os, csv, json, hashlib, asyncio, logging
from typing import Dict
from asyncio import Lock
from contextlib import asynccontextmanager

from engine.qssi_engine import compute_qssi

# =========================
# 🔐 ENV
# =========================
API_KEY = os.getenv("API_KEY", "dev-key")

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
        return float(x)
    except:
        return 0.0

def run_hash(data):
    return hashlib.sha256(
        json.dumps(data, sort_keys=True).encode()
    ).hexdigest()

def ensure_ready():
    if "data" not in ENGINE_CACHE:
        raise HTTPException(503, "Service not ready")

# =========================
# 📊 LOAD ENGINE
# =========================
def safe_init():
    if not os.path.exists(DATASET_PATH):
        raise RuntimeError("Dataset missing")

    results = []

    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
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

    # sort deterministic
    results.sort(key=lambda x: x["Score"], reverse=True)

    # ranking
    for i, r in enumerate(results):
        r["Rank"] = i + 1

    # 🔥 country index (O(1) lookup)
    country_index = {
        r["Country"].lower().strip(): r for r in results
    }

    return {
        "data": results,
        "country_index": country_index,
        "dataset_hash": hashlib.sha256(
            json.dumps(results, sort_keys=True).encode()
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

    ENGINE_CACHE = await loop.run_in_executor(None, safe_init)
    logging.info("System ready")

    yield

# =========================
# 🌐 APP
# =========================
app = FastAPI(
    title="QVP Global System",
    version="v2.0.0-ABSOLUTE-LOCK",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# =========================
# 🔐 AUTH
# =========================
def verify_key(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(401, "Unauthorized")

# =========================
# 🌍 ROUTES
# =========================
@app.get("/")
async def root():
    return {"system": "QVP", "status": "ok"}

@app.get("/dashboard")
async def dashboard():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

@app.get("/rankings")
async def rankings():
    async with CACHE_LOCK:
        ensure_ready()
        return ENGINE_CACHE["data"]

@app.get("/meta")
async def meta():
    async with CACHE_LOCK:
        ensure_ready()
        return {
            "run_id": ENGINE_CACHE["run_id"],
            "dataset_hash": ENGINE_CACHE["dataset_hash"],
            "records": len(ENGINE_CACHE["data"])
        }

@app.get("/country/{name}")
async def country(name: str):
    async with CACHE_LOCK:
        ensure_ready()
        r = ENGINE_CACHE["country_index"].get(name.lower().strip())
        if r:
            return r
    raise HTTPException(404, "Country not found")

@app.get("/top/{n}")
async def top(n: int):
    async with CACHE_LOCK:
        ensure_ready()
        data = ENGINE_CACHE["data"]
        n = max(1, min(n, len(data)))
        return data[:n]

@app.get("/health")
async def health():
    status_val = "ok" if ENGINE_CACHE.get("data") else "init"
    return {
        "status": status_val,
        "records": len(ENGINE_CACHE.get("data", []))
    }
