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

THRESHOLDS = {
    "strength": 0.75,
    "weakness": 0.50
}

METRIC_LABELS = {
    "PQC": "Post-Quantum Readiness",
    "AI": "AI & Cyber Capability",
    "LEGAL": "Legal & Regulatory Preparedness",
    "RES": "Systemic Resilience",
    "RISK": "Systemic Risk"
}


# =========================
# 🛡️ SAFE FLOAT (CRITICAL FIX)
# =========================
def safe_float(x) -> float:
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


# =========================
# 🧠 CORE EXPLAIN FUNCTION
# =========================
def explain_country(record: Dict) -> Dict:
    """
    High-rigor, explainable sovereign intelligence profile.

    Output:
        - Executive Summary
        - Metric Contributions
        - Strengths & Weaknesses
        - Risk Assessment
        - Analytical Interpretation
    """

    country = record.get("Country")
    score = round(safe_float(record.get("Score")), 2)
    tier = record.get("Tier")
    rank = record.get("Rank")

    # =========================
    # 📊 METRICS (SAFE)
    # =========================
    metrics = {
        "PQC": safe_float(record.get("PQC")),
        "AI": safe_float(record.get("AI")),
        "LEGAL": safe_float(record.get("LEGAL")),
        "RES": safe_float(record.get("RES")),
        "RISK": safe_float(record.get("RISK"))
    }

    strengths: List[Dict] = []
    weaknesses: List[Dict] = []
    contributions: List[Dict] = []

    # =========================
    # 📊 METRIC ANALYSIS
    # =========================
    for k, v in metrics.items():
        if k == "RISK":
            continue

        weight = WEIGHTS[k]
        impact = round(v * weight, 4)

        contributions.append({
            "metric": k,
            "label": METRIC_LABELS[k],
            "value": round(v, 3),
            "weight": weight,
            "impact": impact
        })

        if v >= THRESHOLDS["strength"]:
            strengths.append({
                "metric": k,
                "label": METRIC_LABELS[k],
                "value": round(v, 3),
                "impact": impact
            })

        elif v <= THRESHOLDS["weakness"]:
            weaknesses.append({
                "metric": k,
                "label": METRIC_LABELS[k],
                "value": round(v, 3),
                "impact": impact
            })

    # =========================
    # 📊 SORTING (ANALYST FIX)
    # =========================
    contributions.sort(key=lambda x: x["impact"], reverse=True)
    strengths.sort(key=lambda x: x["impact"], reverse=True)
    weaknesses.sort(key=lambda x: x["impact"])

    # =========================
    # ⚠️ RISK ANALYSIS
    # =========================
    risk = metrics["RISK"]

    if risk >= 0.5:
        risk_level = "High"
    elif risk >= 0.25:
        risk_level = "Moderate"
    else:
        risk_level = "Low"

    # =========================
    # 🧾 EXECUTIVE SUMMARY (RANK FIX)
    # =========================
    summary = {
        "country": country,
        "rank": rank,
        "score": score,
        "tier": tier,
        "risk_level": risk_level,
        "global_position": interpret_position(tier)
    }

    # =========================
    # 🧠 INTERPRETATION
    # =========================
    interpretation = generate_interpretation(
        country,
        tier,
        strengths,
        weaknesses,
        risk_level
    )

    # =========================
    # 📦 FINAL OUTPUT
    # =========================
    return {
        "summary": summary,
        "metrics": contributions,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "risk": {
            "value": round(risk, 3),
            "level": risk_level
        },
        "interpretation": interpretation
    }


# =========================
# 🌍 GLOBAL POSITION
# =========================
def interpret_position(tier: str) -> str:
    if tier == "Tier A":
        return "Top-tier sovereign security leader"
    elif tier == "Tier B":
        return "Advanced and stable security architecture"
    elif tier == "Tier C":
        return "Developing but uneven security capability"
    else:
        return "Structurally constrained security environment"


# =========================
# 🧠 HUMAN INTERPRETATION
# =========================
def generate_interpretation(
    country: str,
    tier: str,
    strengths: List[Dict],
    weaknesses: List[Dict],
    risk_level: str
) -> str:

    # Strength narrative
    if strengths:
        strong_metrics = ", ".join([s["label"] for s in strengths[:3]])
        strength_text = f"demonstrates strong performance in {strong_metrics}"
    else:
        strength_text = "does not exhibit dominant strengths across core dimensions"

    # Weakness narrative
    if weaknesses:
        weak_metrics = ", ".join([w["label"] for w in weaknesses[:3]])
        weakness_text = f"while showing relative weaknesses in {weak_metrics}"
    else:
        weakness_text = "with no critical structural weaknesses identified"

    return (
        f"{country} is classified under {tier} and {strength_text}, "
        f"{weakness_text}. The system operates under a {risk_level.lower()} risk profile. "
        f"Overall, its security posture reflects a balance between technological capability, "
        f"institutional readiness, and systemic resilience within a global comparative framework."
    )
