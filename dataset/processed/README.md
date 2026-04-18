## QSSI™ Processed Dataset (v2026.1.0 — Canonical Locked Edition)

## File Path
dataset/processed/processed_data.csv

---

## Schema Definition (Processed Layer)

Indicator,Country,Year,PQC,AI,LEGAL,RES,RISK,QSSI,QSSI_scaled,QSSI_adj,Uncertainty_ε,Score,Rank,Tier

---

## Processing Protocol (Canonical)

### Normalization
All raw inputs transformed to:
M_i ∈ [0,1]

### Aggregation
Indicator-level weighted aggregation after normalization:
- PQC → (0.6 NIST + 0.4 NCSI)
- AI → (0.55 OECD + 0.45 Oxford)
- LEGAL → (0.6 WGI + 0.4 WJP)
- RES → (0.6 IMF + 0.4 ND-GAIN)
- RISK → (0.5 GPR + 0.5 DBIR)

### Missing Data Handling
- Domain-wise Mean Imputation
- LOCF (time-series)
- Temporal interpolation (AI domain)

### Processing Order
Normalization → Aggregation → Risk Adjustment → Scaling → Uncertainty → Ranking

---

## Core Computation

w = {PQC: 0.30, AI: 0.25, LEGAL: 0.25, RES: 0.20}

QSSI = Σ(w_i · M_i)

QSSI_scaled = 100 × QSSI

QSSI_adj = QSSI_scaled × (1 − Risk)

ε = √( Σ (w_i² · σ_{M_i}²) ) × 100

Score = QSSI_adj − ε

Rank = sort_desc(Score)

---

## Output Fields Description

### Core Indicators
- PQC → Post-Quantum Readiness
- AI → AI Capability & Governance
- LEGAL → Rule of Law Strength
- RES → Economic & Climate Resilience
- RISK → Composite Risk Index

### Derived Metrics
- QSSI → Base Index [0–1]
- QSSI_scaled → Scaled Score [0–100]
- QSSI_adj → Risk-adjusted Score
- ε → Propagated Uncertainty
- Score → Conservative ranking metric
- Rank → Final global position
- Tier → Classification band

---

## Tier Classification

- Tier A → QSSI_adj ≥ 85
- Tier B → 75 ≤ QSSI_adj < 85
- Tier C → 50 ≤ QSSI_adj < 75
- Tier D → QSSI_adj < 50

---

## Data Integrity Guarantees

- Deterministic computation
- Fully reproducible pipeline
- No hidden parameters
- Version-locked inputs
- Cross-source validation applied

---

## Version Control

Dataset_Version = 2026.1.0  
Model_Version = v2026.1.0  
State = IMMUTABLE  

---

## Reproducibility Condition

Dataset ∧ Weights ∧ Normalization ∧ Aggregation ∧ Computation ∧ Version = FIXED

---

## Validation Constraints

- 0 ≤ M_i ≤ 1
- 0 ≤ QSSI ≤ 1
- 0 ≤ QSSI_adj ≤ 100
- 0 ≤ ε ≤ 5

---

## System Properties

- Complete
- Consistent
- Deterministic
- Verifiable
- Audit-proof

---

## Canonical Statement

All variables are normalized to [0,1] prior to aggregation.  
Aggregation is performed at the indicator level after grouping all relevant sources.  
Uncertainty is propagated deterministically and applied uniformly as a global proxy in ranking.  
ε is used as a uniform proxy for σ_i in ranking (σ_i ≈ ε).  
Risk is pre-aggregated and normalized to [0,1] prior to application in the adjustment function.  
All computations are performed at country-year granularity.

---

## License

© 2026 QVP — Quantum Veil Protocol Framework  
All Rights Reserved
