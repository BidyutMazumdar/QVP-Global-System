import csv
import hashlib
import json
import math
import statistics
from typing import List, Dict, Any

# ============================================================
# QSSI™ Engine v2026.2.3
# FINAL LOCKED • Deterministic • Audit-Ready • Crash-Safe
# ============================================================

WEIGHTS = {
    "PQC": 0.30,
    "AI": 0.25,
    "LEGAL": 0.25,
    "RES": 0.20
}

REQUIRED_COLUMNS = ["Country", "PQC", "AI", "LEGAL", "RES", "Risk"]

# ---------------------------
# VALIDATION
# ---------------------------

def validate_weights(weights: Dict[str, float]) -> None:
    total = sum(weights.values())
    if not math.isclose(total, 1.0, rel_tol=1e-9):
        raise ValueError(f"Invalid weights: sum = {total}, expected 1.0")


def validate_range(value: float, name: str) -> None:
    if value is None or isinstance(value, str) or math.isnan(value):
        raise ValueError(f"{name} is invalid (None/NaN/string)")
    if not 0 <= value <= 1:
        raise ValueError(f"{name} must be in [0,1], got {value}")

# ---------------------------
# SAFE PARSER (FINAL HARDENING)
# ---------------------------

def safe_float(x: Any, name: str) -> float:
    try:
        v = float(x)
    except:
        raise ValueError(f"{name} cannot be converted to float: {x}")
    validate_range(v, name)
    return v

# ---------------------------
# CORE ENGINE
# ---------------------------

def qssi_score(pqc: float, ai: float, legal: float, res: float) -> float:
    return 100 * (
        WEIGHTS["PQC"] * pqc +
        WEIGHTS["AI"] * ai +
        WEIGHTS["LEGAL"] * legal +
        WEIGHTS["RES"] * res
    )


def risk_adjust(score: float, risk: float) -> float:
    validate_range(risk, "RISK")
    return score * (1 - risk)

# ---------------------------
# SAFE VARIANCE
# ---------------------------

def safe_variance(values: List[float]) -> float:
    clean = [v for v in values if v is not None and not math.isnan(v)]
    if len(clean) < 2:
        return 0.0
    return statistics.variance(clean)


def compute_variances(df: List[Dict[str, Any]]) -> Dict[str, float]:
    domains = ["PQC", "AI", "LEGAL", "RES"]
    return {
        d: safe_variance([float(x[d]) for x in df if x[d] is not None])
        for d in domains
    }


def uncertainty_epsilon(weights: Dict[str, float], variances: Dict[str, float]) -> float:
    eps = sum((weights[k] ** 2) * variances[k] for k in weights)
    eps = math.sqrt(eps) * 100

    # 🔐 HARD BOUND (FINAL SAFETY)
    return min(eps, 50.0)

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
# HASH LAYER
# ---------------------------

def dataset_hash(df: List[Dict[str, Any]]) -> str:
    raw = json.dumps(df, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode()).hexdigest()


def system_hash(df: List[Dict[str, Any]]) -> str:
    meta = {
        "engine": "QSSI",
        "version": "2026.2.3",
        "rows": len(df)
    }
    return hashlib.sha256(
        json.dumps(meta, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def file_hash(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

# ---------------------------
# OUTPUT
# ---------------------------

def system_output(df: List[Dict[str, Any]], input_file: str) -> Dict[str, Any]:
    return {
        "data": df,
        "dataset_hash": dataset_hash(df),
        "system_hash": system_hash(df),
        "input_hash": file_hash(input_file),
        "version": "2026.2.3"
    }

# ---------------------------
# PIPELINE
# ---------------------------

def process(input_file: str, output_file: str) -> Dict[str, Any]:
    validate_weights(WEIGHTS)

    raw_rows: List[Dict[str, Any]] = []
    results: List[Dict[str, Any]] = []

    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if not reader.fieldnames:
            raise ValueError("Empty dataset")

        for col in REQUIRED_COLUMNS:
            if col not in reader.fieldnames:
                raise ValueError(f"Missing column: {col}")

        for row in reader:
            raw_rows.append(row)

    variances = compute_variances(raw_rows)
    eps = uncertainty_epsilon(WEIGHTS, variances)

    for row in raw_rows:
        pqc = safe_float(row["PQC"], "PQC")
        ai = safe_float(row["AI"], "AI")
        legal = safe_float(row["LEGAL"], "LEGAL")
        res = safe_float(row["RES"], "RES")
        risk = safe_float(row["Risk"], "RISK")

        qssi = qssi_score(pqc, ai, legal, res)
        qssi_adj = risk_adjust(qssi, risk)

        score = qssi_adj - eps

        # 🔐 HARD BOUND (FINAL LOCK)
        score = max(0.0, min(score, qssi_adj))

        tier = classify_tier(score)

        results.append({
            "Country": row["Country"],
            "QSSI": round(qssi, 4),
            "QSSI_adj": round(qssi_adj, 4),
            "ε": round(eps, 4),
            "Score": round(score, 4),
            "Tier": tier
        })

    ranked = sorted(results, key=lambda x: (-x["Score"], x["Country"]))

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["Rank", "Country", "QSSI", "QSSI_adj", "ε", "Score", "Tier"]
        )
        writer.writeheader()

        for i, r in enumerate(ranked, start=1):
            r["Rank"] = i
            writer.writerow(r)

    return system_output(ranked, input_file)


if __name__ == "__main__":
    process(
        "../dataset/processed/processed_data.csv",
        "../output/qssi_ranking.csv"
    )
