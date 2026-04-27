# =========================
# 🌐 IMPORTS
# =========================
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import os
import csv
import json
import hashlib
import asyncio
import logging

from typing import Dict
from asyncio import Lock
from contextlib import asynccontextmanager

from engine.qssi_engine import compute_qssi

# =========================
# 🔐 CONFIG
# =========================
API_KEY = os.getenv("API_KEY", "dev-key")
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "qssi_data.csv")
STATIC_DIR = os.path.join(BASE_DIR, "static")

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
    if not ENGINE_CACHE or not ENGINE_CACHE.get("data"):
        raise HTTPException(503, "Service not ready")


# =========================
# 🌍 NORMALIZATION (STRICT)
# =========================
def normalize_country(name: str) -> str:
    name = str(name).strip()

    mapping = {
        "Republic Of Korea": "South Korea",
        "Korea, Republic Of": "South Korea",
        "Korea": "South Korea",

        "Russian Federation": "Russia",

        "Türkiye": "Turkey",

        "UAE": "United Arab Emirates",
        "United Arab Emirates (UAE)": "United Arab Emirates",

        "USA": "United States",
        "United States Of America": "United States",

        "Iran, Islamic Republic Of": "Iran"
    }

    return mapping.get(name, name)


# =========================
# 🏷️ TIER ENGINE
# =========================
def compute_tier(score: float) -> str:
    if score >= 85:
        return "Tier A"
    if score >= 75:
        return "Tier B"
    if score >= 60:
        return "Tier C"
    return "Tier D"


# =========================
# 📊 CORE ENGINE INIT
# =========================
def safe_init():
    if not os.path.exists(DATASET_PATH):
        logging.error("Dataset missing")
        return {
            "data": [],
            "country_index": {},
            "dataset_hash": None,
            "run_id": None
        }

    results = []

    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            row = {
                k.strip().upper(): (v.strip() if isinstance(v, str) else v)
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

            # 🌍 COUNTRY
            country = normalize_country(row.get("COUNTRY", "Unknown"))

            # 📊 SCORE
            try:
                score = float(r.get("Score", 0))
            except:
                score = 0.0

            score = round(score, 2)

            # 🏷️ TIER
            tier = compute_tier(score)
            tier_clean = tier.split(" ")[1]

            # 🧱 CLEAN RECORD (NO CONTAMINATION)
            record = {}
            for k, v in r.items():
                if k not in ("Score", "Tier", "TierRaw"):
                    record[k] = v

            record.update({
                "Country": country,
                "Score": score,
                "Tier": tier,
                "TierRaw": tier_clean
            })

            # 🔒 FLOAT CONTROL
            for k, v in record.items():
                if isinstance(v, float) and k != "Score":
                    record[k] = round(v, 6)

            results.append(record)

    # 🏁 SORT
    results.sort(key=lambda x: x["Score"], reverse=True)

    # 🏆 RANK (keep OR remove — choose one architecture)
    for i, r in enumerate(results):
        r["Rank"] = i + 1

    # ⚡ INDEX
    country_index = {}
    for r in results:
        key = r["Country"].lower()
        if key not in country_index:
            country_index[key] = r

    # 🔐 HASH
    dataset_hash = hashlib.sha256(
        canonical_json(results).encode()
    ).hexdigest()

    return {
        "data": results,
        "country_index": country_index,
        "dataset_hash": dataset_hash,
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
        ENGINE_CACHE = {
            "data": [],
            "country_index": {},
            "dataset_hash": None,
            "run_id": None
        }

    yield


# =========================
# 🌐 APP INIT
# =========================
app = FastAPI(
    title="QVP Global System",
    version="v3.2.0-FINAL-LOCKED",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"]
)

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
    if n <= 0:
        raise HTTPException(400, "n must be positive")

    async with CACHE_LOCK:
        ensure_ready()
        data = ENGINE_CACHE["data"]
        return data[:min(n, len(data))]


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
    async with CACHE_LOCK:
        data = ENGINE_CACHE.get("data")
        return {
            "status": "ok" if data else "init",
            "records": len(data or []),
            "cache_ready": bool(data)
        }
