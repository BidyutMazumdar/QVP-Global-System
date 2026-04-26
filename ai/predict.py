"""
QVP™ Global System — AI Prediction Layer
Version: 2026.10 (Absolute Final Lock 🔒)

Features:
✔ Deterministic predictions
✔ Input validation & sanitization
✔ Explainable AI output (API-friendly)
✔ Stable weighted scoring model
✔ Confidence estimation (interpretable)
✔ Full transparency (raw + scaled output)
✔ Zero-crash safe wrapper
✔ Production + Research grade
"""

import logging
from typing import Dict, Any


# =========================
# 🔧 UTILS
# =========================
def _safe_float(x) -> float:
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def _clamp(value: float, min_v: float = 0.0, max_v: float = 100.0) -> float:
    return max(min_v, min(value, max_v))


def _normalize(x: float) -> float:
    return _clamp(x) / 100.0


# =========================
# 🧠 CORE MODEL
# =========================
def _weighted_model(pqc, ai, legal, res, risk) -> float:
    """
    Deterministic weighted scoring model
    """

    # 🔒 Balanced, interpretable weights
    w = {
        "pqc": 0.30,
        "ai": 0.25,
        "legal": 0.20,
        "res": 0.15,
        "risk": -0.10
    }

    return (
        pqc * w["pqc"] +
        ai * w["ai"] +
        legal * w["legal"] +
        res * w["res"] +
        risk * w["risk"]
    )


# =========================
# 📊 MAIN PREDICTION
# =========================
def predict_qssi(
    pqc: float,
    ai: float,
    legal: float,
    res: float,
    risk: float
) -> Dict[str, Any]:

    # =========================
    # 🔐 INPUT SANITIZATION
    # =========================
    pqc = _clamp(_safe_float(pqc))
    ai = _clamp(_safe_float(ai))
    legal = _clamp(_safe_float(legal))
    res = _clamp(_safe_float(res))
    risk = _clamp(_safe_float(risk))

    # =========================
    # 📈 NORMALIZATION
    # =========================
    pqc_n = _normalize(pqc)
    ai_n = _normalize(ai)
    legal_n = _normalize(legal)
    res_n = _normalize(res)
    risk_n = _normalize(risk)

    # =========================
    # 🧠 MODEL EXECUTION
    # =========================
    raw_score = _weighted_model(pqc_n, ai_n, legal_n, res_n, risk_n)

    # 🔒 Transparent scaling
    scaled_score = raw_score * 100
    predicted_score = _clamp(scaled_score)

    # =========================
    # 🎯 CONFIDENCE MODEL
    # =========================
    variance = (
        abs(pqc_n - ai_n) +
        abs(legal_n - res_n) +
        abs(risk_n)
    ) / 3.0

    confidence = _clamp((1 - variance) * 100)

    # =========================
    # 🏷️ TIER CLASSIFICATION
    # =========================
    if predicted_score >= 80:
        tier = "A"
    elif predicted_score >= 60:
        tier = "B"
    elif predicted_score >= 40:
        tier = "C"
    else:
        tier = "D"

    # =========================
    # 📊 EXPLAINABILITY
    # =========================
    drivers_sorted = sorted(
        {
            "PQC": pqc,
            "AI": ai,
            "LEGAL": legal,
            "RES": res
        }.items(),
        key=lambda x: x[1],
        reverse=True
    )[:2]

    explanation = {
        "positive_drivers": [
            {"factor": k, "value": v} for k, v in drivers_sorted
        ],
        "risk_impact": risk,
        "balance_index": round(1 - variance, 6),

        # 🔒 transparency upgrade
        "model_output_raw": round(scaled_score, 6)
    }

    # =========================
    # 📦 FINAL OUTPUT
    # =========================
    return {
        "PredictedScore": round(predicted_score, 6),
        "Confidence": round(confidence, 6),
        "Tier": tier,
        "Explainability": explanation
    }


# =========================
# 🧪 SAFE WRAPPER
# =========================
def safe_predict(*args, **kwargs) -> Dict[str, Any]:
    """
    Zero-crash production wrapper
    """
    try:
        return predict_qssi(*args, **kwargs)
    except Exception as e:
        logging.error(f"Prediction failed: {e}")
        return {
            "PredictedScore": 0.0,
            "Confidence": 0.0,
            "Tier": "D",
            "Explainability": {},
            "error": "prediction_failed"
        }
