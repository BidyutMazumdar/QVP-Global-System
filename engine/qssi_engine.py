import math

WEIGHTS = {
    "PQC": 0.30,
    "AI": 0.25,
    "LEGAL": 0.25,
    "RES": 0.20,
}

SIGMA = 0.02
UNCERTAINTY_BOUND = 5.0


# ---------------------------
# VALIDATION
# ---------------------------

def validate(value: float) -> float:
    v = float(value)
    if v < 0 or v > 1:
        raise ValueError("Value out of bounds [0,1]")
    return v


# ---------------------------
# TIER SYSTEM
# ---------------------------

def classify_tier(score: float) -> str:
    if score >= 85:
        return "Tier A"
    elif score >= 75:
        return "Tier B"
    elif score >= 50:
        return "Tier C"
    return "Tier D"


# ---------------------------
# UNCERTAINTY MODEL
# ---------------------------

def compute_uncertainty() -> float:
    eps = (sum((w * SIGMA) ** 2 for w in WEIGHTS.values())) ** 0.5 * 100
    return round(min(eps, UNCERTAINTY_BOUND), 2)


# ---------------------------
# CORE ENGINE (ABSOLUTE LOCK)
# ---------------------------

def compute_qssi(pqc, ai, legal, res, risk):
    pqc = validate(pqc)
    ai = validate(ai)
    legal = validate(legal)
    res = validate(res)
    risk = validate(risk)

    # 🔒 BASE SCORE (normalized)
    qssi = (
        WEIGHTS["PQC"] * pqc +
        WEIGHTS["AI"] * ai +
        WEIGHTS["LEGAL"] * legal +
        WEIGHTS["RES"] * res
    )

    # 🔒 FLOAT NORMALIZATION (cross-env deterministic)
    qssi_scaled = round(100 * qssi, 6)

    # 🔒 RISK ADJUSTMENT
    qssi_adj = round(qssi_scaled * (1 - risk), 6)

    # 🔒 UNCERTAINTY ADJUSTMENT
    eps = compute_uncertainty()
    score = max(0.0, round(qssi_adj - eps, 6))  # bounded & deterministic

    return {
        "QSSI": round(qssi, 4),
        "QSSI_scaled": round(qssi_scaled, 2),
        "QSSI_adj": round(qssi_adj, 2),
        "ε": eps,
        "Score": round(score, 2),
        "Tier": classify_tier(score)
    }
