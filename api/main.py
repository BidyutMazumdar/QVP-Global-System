from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.staticfiles import StaticFiles

import os, csv, json, hashlib, asyncio, logging, uuid
from typing import Dict
from contextlib import asynccontextmanager
from asyncio import Lock

import redis.asyncio as redis
from prometheus_fastapi_instrumentator import Instrumentator
from engine.qssi_engine import compute_qssi

# =========================
# 🔐 ENV CONFIG
# =========================
API_KEY = os.getenv("API_KEY")
REDIS_URL = os.getenv("REDIS_URL")
TRUST_PROXY = os.getenv("TRUST_PROXY", "false").lower() == "true"

if not API_KEY:
    raise RuntimeError("API_KEY missing")
if not REDIS_URL:
    raise RuntimeError("REDIS_URL missing")

redis_client = redis.from_url(REDIS_URL, decode_responses=True)

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

def run_hash(data):
    return hashlib.sha256(
        json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

def get_ip(request: Request):
    if TRUST_PROXY:
        forwarded = request.headers.get("X-Forwarded-For")
        if forwarded:
            return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"

# =========================
# 🚦 RATE LIMIT (SAFE)
# =========================
try:
    RATE_SCRIPT = redis_client.register_script("""
    local current = redis.call("INCR", KEYS[1])
    if current == 1 then redis.call("EXPIRE", KEYS[1], ARGV[1]) end
    return current
    """)
except Exception as e:
    logging.warning(f"Redis script init failed: {e}")
    RATE_SCRIPT = None

async def rate_limit(ip: str, limit=60, window=60):
    if not RATE_SCRIPT:
        return
    try:
        key = f"rate:{ip}"
        count = await RATE_SCRIPT(keys=[key], args=[window])
        if int(count) > limit:
            raise HTTPException(429, "Too many requests")
    except Exception as e:
        logging.warning(f"Rate limit fallback: {e}")

# =========================
# 📊 ENGINE
# =========================
def safe_init():
    if not os.path.exists(DATASET_PATH):
        raise RuntimeError("Dataset missing")

    results, errors = [], []

    with open(DATASET_PATH, "rb") as f:
        raw = f.read()
        dataset_hash = hashlib.sha256(raw).hexdigest()

    reader = csv.DictReader(raw.decode("utf-8", errors="replace").splitlines())
    EXPECTED = ["PQC", "AI", "LEGAL", "RES", "RISK", "COUNTRY"]

    for row in reader:
        row = {k.strip().upper(): (v.strip() if isinstance(v, str) else v) for k, v in row.items()}
        for f in EXPECTED:
            row.setdefault(f, 0)

        try:
            r = compute_qssi(
                to_float(row["PQC"]),
                to_float(row["AI"]),
                to_float(row["LEGAL"]),
                to_float(row["RES"]),
                to_float(row["RISK"])
            )
        except Exception as e:
            errors.append({"row": row, "error": str(e)})
            continue

        r["Country"] = row.get("COUNTRY", "Unknown")

        for k in r:
            if isinstance(r[k], float):
                r[k] = round(r[k], 6)

        results.append(r)

    results.sort(key=lambda x: x["Score"], reverse=True)

    for i, r in enumerate(results):
        r["Rank"] = i + 1

    return {
        "data": results,
        "errors": errors,
        "dataset_hash": dataset_hash,
        "run_id": run_hash(results),
        "country_index": {r["Country"].lower().strip(): r for r in results}
    }

# =========================
# 🔄 REFRESH
# =========================
async def refresh_cache():
    loop = asyncio.get_running_loop()
    new = await loop.run_in_executor(None, safe_init)

    if new.get("data"):
        async with CACHE_LOCK:
            global ENGINE_CACHE
            ENGINE_CACHE = new

# =========================
# 🚀 LIFECYCLE
# =========================
@asynccontextmanager
async def lifespan(app: FastAPI):
    global ENGINE_CACHE
    loop = asyncio.get_running_loop()

    try:
        ENGINE_CACHE = await asyncio.wait_for(
            loop.run_in_executor(None, safe_init),
            timeout=30
        )
        logging.info("Startup cache loaded")
    except Exception as e:
        logging.critical(f"Startup failed: {e}")
        ENGINE_CACHE = {"data": [], "errors": ["startup_failed"]}

    app.state.refreshing = False
    yield

    try:
        await redis_client.close()
    except Exception as e:
        logging.warning(f"Redis shutdown issue: {e}")

    logging.info("Shutdown clean")

# =========================
# 🌐 APP
# =========================
app = FastAPI(title="QVP API", version="v1.0.0-FINAL-LOCK", lifespan=lifespan)

app.add_middleware(GZipMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),
    allow_methods=["*"],
    allow_headers=["*"]
)

Instrumentator().instrument(app).expose(app)

if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# =========================
# 🔐 GLOBAL ERROR HANDLER
# =========================
@app.exception_handler(Exception)
async def global_handler(request: Request, exc: Exception):
    logging.error(f"{request.method} {request.url.path} | {exc}")

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "request_id": getattr(request.state, "request_id", None)
        }
    )

# =========================
# ⚡ CORE MIDDLEWARE
# =========================
@app.middleware("http")
async def core(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id

    run_id = ENGINE_CACHE.get("run_id")
    etag = f'W/"{run_id}"' if run_id else None

    if etag and request.url.path in ["/rankings", "/meta"]:
        if request.headers.get("If-None-Match") == etag:
            return Response(status_code=304)

    try:
        res = await asyncio.wait_for(call_next(request), timeout=10)
    except asyncio.TimeoutError:
        return JSONResponse(
            status_code=504,
            content={"error": "timeout", "request_id": request_id}
        )

    res.headers["X-Content-Type-Options"] = "nosniff"
    res.headers["X-Frame-Options"] = "DENY"
    res.headers["Referrer-Policy"] = "no-referrer"

    res.headers["X-Request-ID"] = request_id
    res.headers["Cache-Control"] = "public, max-age=20, stale-while-revalidate=60"
    res.headers["X-API-Version"] = "v1.0.0-FINAL-LOCK"

    if etag:
        res.headers["ETag"] = etag

    res.headers.pop("server", None)

    return res

# =========================
# 🔐 HELPERS
# =========================
def verify_key(k):
    if not k or k != API_KEY:
        raise HTTPException(401, "Unauthorized")

def ensure_ready():
    if not ENGINE_CACHE or not ENGINE_CACHE.get("data"):
        raise HTTPException(503, "Service not ready")

# =========================
# 🌍 ROUTES
# =========================
@app.get("/")
async def root():
    return {
        "system": "QVP GLOBAL SYSTEM",
        "version": "v1.0.0-FINAL-LOCK",
        "status": "operational"
    }

@app.get("/rankings")
async def rankings(request: Request):
    await rate_limit(get_ip(request))
    ensure_ready()

    return {
        "data": ENGINE_CACHE["data"],
        "run_id": ENGINE_CACHE["run_id"],
        "dataset_hash": ENGINE_CACHE.get("dataset_hash")
    }

@app.get("/top/{n}")
async def top(n: int, request: Request):
    if n <= 0:
        raise HTTPException(400, "Invalid n")

    await rate_limit(get_ip(request))
    ensure_ready()
    return ENGINE_CACHE["data"][:min(n, 100)]

@app.get("/country/{name}")
async def country(name: str, request: Request):
    await rate_limit(get_ip(request))
    ensure_ready()

    name = name.strip()
    if len(name) > 100:
        raise HTTPException(400, "Invalid input")

    r = ENGINE_CACHE["country_index"].get(name.lower().strip())
    if not r:
        raise HTTPException(404, "Not found")

    return r

@app.get("/meta")
async def meta(request: Request):
    await rate_limit(get_ip(request))
    ensure_ready()

    return {
        "records": len(ENGINE_CACHE["data"]),
        "run_id": ENGINE_CACHE["run_id"],
        "dataset_hash": ENGINE_CACHE.get("dataset_hash")
    }

@app.get("/health")
async def health():
    try:
        await asyncio.wait_for(redis_client.ping(), timeout=1)
        redis_ok = True
    except:
        redis_ok = False

    return {
        "status": "ok" if ENGINE_CACHE.get("data") else "init",
        "redis": "ok" if redis_ok else "degraded"
    }

@app.post("/refresh")
async def refresh(x_api_key: str = Header(None, alias="X-API-KEY")):
    verify_key(x_api_key)

    if getattr(app.state, "refreshing", False):
        return {"status": "already_running"}

    app.state.refreshing = True

    async def _run():
        try:
            await refresh_cache()
        finally:
            app.state.refreshing = False

    asyncio.create_task(_run())

    return {"status": "refresh_started"}
