import csv
from typing import List, Dict, Any

# ============================================================
# QSSI™ Engine v2026.1.1
# Deterministic, Reproducible, Audit-Ready
# ============================================================

# Weight configuration
# Constraint: Sum of weights must equal 1.0
WEIGHTS = {
    "PQC": 0.30,
    "AI": 0.25,
    "LEGAL": 0.25,
    "RES": 0.20
}


def validate_weights(weights: Dict[str, float]) -> None:
    """
    Ensures the total weight equals 1.0
    """
    total = sum(weights.values())
    if round(total, 5) != 1.0:
        raise ValueError(
            f"Invalid weight configuration. Sum of weights = {total}, expected 1.0"
        )


def validate_range(value: float, field_name: str) -> None:
    """
    Ensures normalized variables remain within [0,1]
    """
    if not 0 <= value <= 1:
        raise ValueError(
            f"{field_name} must be between 0 and 1. Received: {value}"
        )


def qssi_score(pqc: float, ai: float, legal: float, res: float) -> float:
    """
    Computes raw QSSI score scaled to 100
    """
    validate_range(pqc, "PQC")
    validate_range(ai, "AI")
    validate_range(legal, "LEGAL")
    validate_range(res, "RES")

    score = (
        WEIGHTS["PQC"] * pqc +
        WEIGHTS["AI"] * ai +
        WEIGHTS["LEGAL"] * legal +
        WEIGHTS["RES"] * res
    )

    return 100 * score


def risk_adjust(score: float, risk: float) -> float:
    """
    Applies systemic risk adjustment
    """
    validate_range(risk, "Risk")
    return score * (1 - risk)


def classify_tier(qssi_adj: float) -> str:
    """
    Assigns country tier based on adjusted QSSI score
    """
    if qssi_adj >= 85:
        return "Tier A"
    elif qssi_adj >= 75:
        return "Tier B"
    elif qssi_adj >= 50:
        return "Tier C"
    else:
        return "Tier D"


def process(input_file: str, output_file: str) -> None:
    """
    Reads input CSV, computes QSSI rankings,
    applies risk adjustment, classifies tiers,
    and exports final ranked results.
    """
    validate_weights(WEIGHTS)

    results: List[Dict[str, Any]] = []

    with open(input_file, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)

        required_columns = ["Country", "PQC", "AI", "LEGAL", "RES", "Risk"]

        for column in required_columns:
            if column not in reader.fieldnames:
                raise ValueError(f"Missing required column: {column}")

        for row in reader:
            pqc = float(row["PQC"])
            ai = float(row["AI"])
            legal = float(row["LEGAL"])
            res = float(row["RES"])
            risk = float(row["Risk"])

            qssi_scaled = qssi_score(pqc, ai, legal, res)
            qssi_adj = risk_adjust(qssi_scaled, risk)
            delta_qssi = qssi_scaled - qssi_adj
            tier = classify_tier(qssi_adj)

            results.append({
                "Country": row["Country"],
                "QSSI": round(qssi_scaled, 2),
                "QSSI_adj": round(qssi_adj, 2),
                "Delta_QSSI": round(delta_qssi, 2),
                "Tier": tier
            })

    ranked = sorted(
        results,
        key=lambda x: x["QSSI_adj"],
        reverse=True
    )

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        fieldnames = [
            "Rank",
            "Country",
            "QSSI",
            "QSSI_adj",
            "Delta_QSSI",
            "Tier"
        ]

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for rank, row in enumerate(ranked, start=1):
            row["Rank"] = rank
            writer.writerow(row)


if __name__ == "__main__":
    process(
        "../dataset/qssi_data.csv",
        "../output/qssi_ranking.csv"
    )
