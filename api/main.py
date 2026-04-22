from fastapi import FastAPI, Header, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

import csv, os, hashlib, json, logging, asyncio
from typing import Dict, List
from asyncio import Lock
from contextlib import asynccontextmanager

from engine.qssi_engine import compute_qssi


API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("API_KEY not set")

ALLOWED_ORIGINS = [
    o.strip() for o in os.getenv("ALLOWED_ORIGINS", "").split(",") if o.strip()
]
if not ALLOWED_ORIGINS:
    raise RuntimeError("ALLOWED_ORIGINS not set")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


ENGINE_CACHE: Dict = {}
CACHE_LOCK = Lock()


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "qssi_data.csv")
STATIC_DIR = os.path.join(BASE_DIR, "static")


def to_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def run_hash(data: List[Dict]) -> str:
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(canonical).hexdigest()


def safe_init():
    if not os.path.exists(DATASET_PATH):
        raise RuntimeError("Dataset not found")

    results, errors = [], []

    with open(DATASET_PATH, "rb") as f:
        raw_bytes = f.read()
        dataset_hash = hashlib.sha256(raw_bytes).hexdigest()

    reader = csv.DictReader(raw_bytes.decode("utf-8", "replace").splitlines())

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

    results.sort(key=lambda x: x["Score"], reverse=True)

    for i, r in enumerate(results):
        r["Rank"] = i + 1
        for k, v in r.items():
            if isinstance(v, float):
                r[k] = round(v, 6)

    return {
        "data": results,
        "errors": errors,
        "dataset_hash": dataset_hash,
        "run_id": run_hash(results)
    }


@asynccontextmanager
async def lifespan(app: FastAPI):
    loop = asyncio.get_running_loop()
    global ENGINE_CACHE

    try:
        ENGINE_CACHE = await loop.run_in_executor(None, safe_init)
    except Exception as e:
        logging.critical(f"Startup failed: {e}")
        raise RuntimeError("Critical startup failure")

    yield


app = FastAPI(
    title="QVP™ Global System API",
    description="QSSI™ Sovereign Intelligence Infrastructure",
    version="2026.10",
    lifespan=lifespan
)


def verify_key(x_api_key: str = Header(None, alias="X-API-KEY")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")


app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


def ensure_ready(cache: Dict):
    if not cache or "data" not in cache:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Service unavailable"
        )


@app.get("/")
async def root():
    return {
        "system": "QVP GLOBAL SYSTEM",
        "docs": "/docs",
        "rankings": "/rankings",
        "health": "/health"
    }


@app.get("/dashboard")
async def dashboard():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


@app.get("/rankings")
async def rankings():
    async with CACHE_LOCK:
        ensure_ready(ENGINE_CACHE)
        return ENGINE_CACHE


@app.get("/top/{n}")
async def top_n(n: int):
    async with CACHE_LOCK:
        ensure_ready(ENGINE_CACHE)
        data = ENGINE_CACHE.get("data", [])
        return data[:max(1, min(n, len(data)))]


@app.get("/country/{name}")
async def country(name: str):
    async with CACHE_LOCK:
        ensure_ready(ENGINE_CACHE)
        data = ENGINE_CACHE.get("data", [])
        result = [d for d in data if d.get("Country", "").lower() == name.lower()]

    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return result


@app.get("/tier/{tier}")
async def tier_filter(tier: str):
    async with CACHE_LOCK:
        ensure_ready(ENGINE_CACHE)
        data = ENGINE_CACHE.get("data", [])
        return [d for d in data if d.get("Tier", "").lower() == tier.lower()]


@app.get("/meta")
async def meta():
    async with CACHE_LOCK:
        ensure_ready(ENGINE_CACHE)
        return {
            "version": "2026.10",
            "dataset_hash": ENGINE_CACHE.get("dataset_hash"),
            "run_id": ENGINE_CACHE.get("run_id"),
            "records": len(ENGINE_CACHE.get("data", [])),
            "errors": len(ENGINE_CACHE.get("errors", [])),
            "deterministic": True,
            "audit_trace": True
        }


async def _refresh_logic():
    loop = asyncio.get_running_loop()
    new_cache = await loop.run_in_executor(None, safe_init)

    if not new_cache or "data" not in new_cache:
        raise ValueError("invalid dataset")

    async with CACHE_LOCK:
        global ENGINE_CACHE
        ENGINE_CACHE = new_cache


@app.post("/refresh")
async def refresh(x_api_key: str = Header(None, alias="X-API-KEY")):
    verify_key(x_api_key)

    try:
        await asyncio.wait_for(_refresh_logic(), timeout=10)
    except asyncio.TimeoutError:
        raise HTTPException(status_code=503, detail="Refresh timeout")
    except ValueError:
        raise HTTPException(status_code=503, detail="Invalid dataset")
    except Exception as e:
        logging.error(f"Refresh failed: {e}")
        raise HTTPException(status_code=500, detail="Internal error")

    return {
        "status": "refreshed",
        "dataset_hash": ENGINE_CACHE.get("dataset_hash"),
        "run_id": ENGINE_CACHE.get("run_id")
    }


@app.get("/v1/rankings")
async def v1_rankings(x_api_key: str = Header(None, alias="X-API-KEY")):
    verify_key(x_api_key)
    return await rankings()


@app.get("/v1/top/{n}")
async def v1_top(n: int, x_api_key: str = Header(None, alias="X-API-KEY")):
    verify_key(x_api_key)
    return await top_n(n)


@app.get("/v1/meta")
async def v1_meta(x_api_key: str = Header(None, alias="X-API-KEY")):
    verify_key(x_api_key)
    return await meta()


@app.get("/health")
async def health():
    async with CACHE_LOCK:
        cache = ENGINE_CACHE

        if not cache or "data" not in cache:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail={
                    "status": "error",
                    "dataset_loaded": False,
                    "records": 0,
                    "errors": 0
                }
            )

        return {
            "status": "ok",
            "dataset_loaded": True,
            "records": len(cache.get("data", [])),
            "errors": len(cache.get("errors", []))
        }
