from typing import Dict, List

# =========================
# ⚙️ CONFIG
# =========================
WEIGHTS = {
    "PQC": 0.30,
    "AI": 0.25,
    "LEGAL": 0.25,
    "RES": 0.20
}

METRIC_LABELS = {
    "PQC": "Post-Quantum Readiness",
    "AI": "AI & Cyber Capability",
    "LEGAL": "Legal & Regulatory Preparedness",
    "RES": "Systemic Resilience",
    "RISK": "Systemic Risk"
}


# =========================
# 🛡️ SAFE FLOAT HANDLING
# =========================
def safe_float(x) -> float:
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


# =========================
# 📊 METRIC BREAKDOWN ENGINE
# =========================
def metric_breakdown(record: Dict) -> Dict:
    """
    Returns a structured, analysis-ready breakdown of all metrics.

    Output:
        - normalized values
        - labels
        - weights
        - contribution (impact)
        - sorted importance ranking
    """

    # =========================
    # 📥 SAFE METRICS LOAD
    # =========================
    metrics = {
        "PQC": safe_float(record.get("PQC")),
        "AI": safe_float(record.get("AI")),
        "LEGAL": safe_float(record.get("LEGAL")),
        "RES": safe_float(record.get("RES")),
        "RISK": safe_float(record.get("RISK"))
    }

    breakdown: List[Dict] = []

    # =========================
    # 📊 CONTRIBUTION ANALYSIS
    # =========================
    for key in ["PQC", "AI", "LEGAL", "RES"]:
        value = metrics[key]
        weight = WEIGHTS[key]
        impact = round(value * weight, 4)

        breakdown.append({
            "metric": key,
            "label": METRIC_LABELS[key],
            "value": round(value, 3),
            "weight": weight,
            "impact": impact
        })

    # =========================
    # 📊 SORT BY IMPACT
    # =========================
    breakdown.sort(key=lambda x: x["impact"], reverse=True)

    # =========================
    # ⚠️ RISK LAYER
    # =========================
    risk_value = metrics["RISK"]

    if risk_value >= 0.5:
        risk_level = "High"
    elif risk_value >= 0.25:
        risk_level = "Moderate"
    else:
        risk_level = "Low"

    risk = {
        "metric": "RISK",
        "label": METRIC_LABELS["RISK"],
        "value": round(risk_value, 3),
        "level": risk_level
    }

    # =========================
    # 📦 FINAL OUTPUT
    # =========================
    return {
        "metrics": breakdown,
        "risk": risk
    }
