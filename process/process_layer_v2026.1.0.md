PROCESS LAYER :: QSSI™ v2026.1.0 :: METHODOLOGICAL ENGINE 🔒


---

PURPOSE

Defines the operational procedure of the QSSI system.

👉 This layer does NOT define mathematics
👉 This layer defines how the model is executed step-by-step


---

INPUT PIPELINE

Raw Inputs

PQC indicators (NIST, NCSI)

AI indicators (OECD, Oxford)

Legal indicators (WGI, WJP)

Resilience indicators (IMF, ND-GAIN)

Risk indicators (GPR, DBIR)



---

PROCESSING FLOW

Step 1: Data Ingestion

Collect multi-source global datasets

Align by Country × Year keys



---

Step 2: Normalization

All variables converted to:

Mᵢ ∈ [0,1]

Methods:

Min-Max scaling

Index normalization (0–100 → 0–1)

Linear shift scaling (-2.5 to +2.5 → 0–1)



---

Step 3: Domain Aggregation

PQC = 0.6·NIST + 0.4·NCSI

AI = 0.55·OECD + 0.45·Oxford

LEGAL = 0.6·WGI + 0.4·WJP

RES = 0.6·IMF + 0.4·ND-GAIN

RISK = 0.5·GPR + 0.5·DBIR



---

Step 4: Vector Construction

M = (PQC, AI, LEGAL, RES, RISK)


---

Step 5: Core Computation

QSSI = ∑(wᵢ · Mᵢ)
QSSI_scaled = 100 · QSSI


---

Step 6: Risk Adjustment

QSSI_adj = QSSI_scaled × (1 − R)

RISK DEFINITION

R is derived from normalized aggregation of GPR and DBIR indicators and bounded to [0,1]


---

Step 7: Uncertainty Propagation

ε = √(∑(wᵢ² · σᵢ²)) · 100

Where:
σᵢ = cross-country temporal variance per domain


---

Step 8: Scoring Function

Score = QSSI_adj − ε


---

Step 9: Ranking Procedure

Rank = descending sort of Score across all Country × Year entities


---

Step 10: Tier Assignment

Tier A: ≥ 85

Tier B: 75–84.99

Tier C: 50–74.99

Tier D: < 50



---

OUTPUT STRUCTURE

F(Country, Year) → (QSSI, QSSI_adj, ε, Score, Rank, Tier)


---

PROCESS PROPERTIES

Deterministic execution

Reproducible pipeline

No stochastic sampling

Version-controlled transformations

Fully traceable computation chain



---

ROLE DEFINITION

👉 “Defines HOW the model is executed step-by-step”


---

END STATE

PROCESS LAYER = OPERATIONAL ENGINE
STATE = FIXED PROCEDURE
VERSION = v2026.1.0 🔒


---

