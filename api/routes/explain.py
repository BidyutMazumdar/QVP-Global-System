from fastapi import APIRouter, HTTPException, Query
from typing import Dict, Any
from datetime import datetime, timezone

from api.explain import explain_country
from engine.cache import ENGINE_CACHE

router = APIRouter()


# =========================
# 🧠 NORMALIZATION UTILITY
# =========================
def normalize_country_name(name: str) -> str:
    return name.strip().lower()


# =========================
# 📡 EXPLAIN ENDPOINT
# =========================
@router.get("/explain/{country}", response_model=Dict[str, Any])
async def explain(
    country: str,
    debug: bool = Query(False, description="Include raw record for debugging")
):
    """
    Explain a country's QSSI ranking.

    Returns:
        - structured explanation
        - strengths / weaknesses
        - risk analysis
        - interpretation narrative
    """

    # =========================
    # 🔍 INPUT NORMALIZATION
    # =========================
    key = normalize_country_name(country)

    # =========================
    # 📦 FETCH RECORD (SAFE)
    # =========================
    country_index = ENGINE_CACHE.get("country_index")

    if not country_index:
        raise HTTPException(
            status_code=500,
            detail="Engine cache not initialized"
        )

    record = country_index.get(key)

    if not record:
        raise HTTPException(
            status_code=404,
            detail={
                "error": "Country not found",
                "input": country,
                "normalized": key
            }
        )

    # =========================
    # 🧠 GENERATE EXPLANATION
    # =========================
    explanation = explain_country(record)

    # =========================
    # 📊 METADATA LAYER (UTC FIX)
    # =========================
    response = {
        "meta": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "system": "QSSI Explain API",
            "version": "v1",
            "country": key
        },
        "data": explanation
    }

    # =========================
    # 🧪 DEBUG MODE (SAFE)
    # =========================
    if debug:
        response["debug"] = {
            "raw_record": record
        }

    return response
