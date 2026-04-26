from fastapi import FastAPI, Header, HTTPException, status, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

import csv, os, hashlib, json, logging, asyncio
from typing import Dict, List
from asyncio import Lock
from contextlib import asynccontextmanager
from time import time

from engine.qssi_engine import compute_qssi


# =========================
# 🔐 ENV CONFIG
# =========================
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise RuntimeError("API_KEY not set")

ALLOWED_ORIGINS = [
    o.strip() for o in os.getenv("ALLOWED_ORIGINS", "").split(",") if o.strip()
]
if not ALLOWED_ORIGINS:
    raise RuntimeError("ALLOWED_ORIGINS not set")

TRUST_PROXY = os.getenv("TRUST_PROXY", "false").lower() == "true"


# =========================
# 🧠 LOGGING
# =========================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


# =========================
# ⚡ GLOBAL STATE
# =========================
ENGINE_CACHE: Dict = {}
CACHE_LOCK = Lock()

LAST_CALL = {}
MAX_TRACKED_IPS = 10000

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "qssi_data.csv")
STATIC_DIR = os.path.join(BASE_DIR, "static")


# =========================
# 🔧 UTILS
# =========================
def to_float(x):
    try:
        return float(x)
    except:
        return 0.0


def run_hash(data: List[Dict]) -> str:
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(canonical).hexdigest()


def get_client_ip(request: Request) -> str:
    if TRUST_PROXY:
        forwarded = request.headers.get("X-Forwarded-For")
        if forwarded:
            return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


def rate_limit(ip: str, limit=10, window=1):
    now = time()
    calls = LAST_CALL.get(ip, [])
    calls = [t for t in calls if now - t < window]

    if len(calls) >= limit:
        raise HTTPException(status_code=429, detail="Too many requests")

    calls.append(now)
    LAST_CALL[ip] = calls

    if len(LAST_CALL) > MAX_TRACKED_IPS:
        LAST_CALL.clear()


# =========================
# 📊 ENGINE INIT
# =========================
def safe_init():
    if not os.path.exists(DATASET_PATH):
        raise RuntimeError("Dataset not found")

    results, errors = [], []

    with open(DATASET_PATH, "rb") as f:
        raw_bytes = f.read()
        dataset_hash = hashlib.sha256(raw_bytes).hexdigest()

    reader = csv.DictReader(
        raw_bytes.decode("utf-8", errors="replace").splitlines()
    )

    EXPECTED_FIELDS = ["PQC", "AI", "LEGAL", "RES", "RISK", "COUNTRY"]

    for row in reader:
        row_clean = {
            k.strip().upper(): (v.strip() if isinstance(v, str) else v)
            for k, v in row.items()
        }

        for field in EXPECTED_FIELDS:
            if field not in row_clean:
                row_clean[field] = 0

        try:
            result = compute_qssi(
                to_float(row_clean.get("PQC")),
                to_float(row_clean.get("AI")),
                to_float(row_clean.get("LEGAL")),
                to_float(row_clean.get("RES")),
                to_float(row_clean.get("RISK"))
            )
        except Exception as e:
            logging.error(f"Row failed: {row_clean} | {e}")
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

    logging.info(f"Dataset loaded: {len(results)} records")
    logging.warning(f"Dataset errors: {len(errors)}")

    return {
        "data": results,
        "errors": errors,
        "dataset_hash": dataset_hash,
        "run_id": run_hash(results)
    }


# =========================
# 🚀 LIFECYCLE
# =========================
@asynccontextmanager
async def lifespan(app: FastAPI):
    loop = asyncio.get_running_loop()
    global ENGINE_CACHE

    try:
        ENGINE_CACHE = await asyncio.wait_for(
            loop.run_in_executor(None, safe_init),
            timeout=30
        )
    except Exception as e:
        logging.critical(f"Startup failed: {e}")
        ENGINE_CACHE = {
            "data": [],
            "errors": ["startup_failed"],
            "dataset_hash": None,
            "run_id": None
        }

    yield


# =========================
# 🌐 APP INIT
# =========================
app = FastAPI(
    title="QVP™ Global System API",
    version="2026.10",
    lifespan=lifespan
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
else:
    logging.warning("Static directory not found, skipping mount")


# =========================
# 🔐 SECURITY
# =========================
def verify_key(x_api_key: str = Header(None, alias="X-API-KEY")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")


def ensure_ready():
    if not ENGINE_CACHE or "data" not in ENGINE_CACHE:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Service unavailable"
        )


# =========================
# 📡 MIDDLEWARE
# =========================
@app.middleware("http")
async def version_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-API-Version"] = "2026.10"
    return response


# =========================
# 🌍 ROUTES
# =========================
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
    path = os.path.join(STATIC_DIR, "index.html")
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Dashboard not found")
    return FileResponse(path)


@app.get("/rankings")
async def rankings(request: Request, x_api_key: str = Header(None, alias="X-API-KEY")):
    verify_key(x_api_key)
    rate_limit(get_client_ip(request))

    async with CACHE_LOCK:
        ensure_ready()
        return ENGINE_CACHE


@app.get("/top/{n}")
async def top_n(n: int, request: Request, x_api_key: str = Header(None, alias="X-API-KEY")):
    if n <= 0:
        raise HTTPException(status_code=400, detail="Invalid n")

    verify_key(x_api_key)
    rate_limit(get_client_ip(request))

    async with CACHE_LOCK:
        ensure_ready()
        return ENGINE_CACHE["data"][:min(n, len(ENGINE_CACHE["data"]))]


@app.get("/country/{name}")
async def country(name: str):
    async with CACHE_LOCK:
        ensure_ready()
        result = [d for d in ENGINE_CACHE["data"] if d["Country"].lower() == name.lower()]
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return result


@app.get("/tier/{tier}")
async def tier_filter(tier: str):
    async with CACHE_LOCK:
        ensure_ready()
        return [d for d in ENGINE_CACHE["data"] if d.get("Tier", "").lower() == tier.lower()]


@app.get("/meta")
async def meta():
    async with CACHE_LOCK:
        ensure_ready()
        return {
            "version": "2026.10",
            "dataset_hash": ENGINE_CACHE["dataset_hash"],
            "run_id": ENGINE_CACHE["run_id"],
            "records": len(ENGINE_CACHE["data"]),
            "errors": len(ENGINE_CACHE["errors"])
        }


@app.post("/refresh")
async def refresh(x_api_key: str = Header(None, alias="X-API-KEY")):
    verify_key(x_api_key)

    loop = asyncio.get_running_loop()
    new_cache = await asyncio.wait_for(
        loop.run_in_executor(None, safe_init),
        timeout=15
    )

    # 🔒 CRITICAL SAFETY
    if not new_cache or "data" not in new_cache:
        raise HTTPException(status_code=503, detail="Invalid dataset")

    async with CACHE_LOCK:
        global ENGINE_CACHE
        ENGINE_CACHE = new_cache

    return {
        "status": "refreshed",
        "dataset_hash": ENGINE_CACHE.get("dataset_hash"),
        "run_id": ENGINE_CACHE.get("run_id")
    }


@app.get("/health")
async def health():
    return {
        "status": "ok" if ENGINE_CACHE else "initializing",
        "records": len(ENGINE_CACHE.get("data", []))
    }
