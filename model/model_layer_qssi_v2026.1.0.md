# MODEL LAYER :: QSSI™ v2026.1.0 :: CANONICAL MATHEMATICAL CORE


---

## AXIOMATIC SPACE

## Normalized Domain

Mᵢ ∈ [0,1]

## Observation Space

Country × Year → vector space ℝⁿ (n = 5 domains)


---

## CORE STATE VECTOR

## System State

S = {PQC, AI, LEGAL, RES, RISK}

## Normalized Representation

M = (M₁, M₂, M₃, M₄, M₅)


---

## WEIGHT STRUCTURE

## Deterministic Weights

w = { PQC: 0.30, AI: 0.25, LEGAL: 0.25, RES: 0.20 }

## Constraint

∑ wᵢ = 1


---

## PRIMARY INDEX FUNCTION

## QSSI Definition

QSSI = ∑ (wᵢ · Mᵢ)


---

## SCALING OPERATOR

QSSI_scaled = 100 · QSSI


---

## RISK TRANSFORMATION OPERATOR

R ∈ [0,1]

QSSI_adj = QSSI_scaled · (1 − R)


---

## UNCERTAINTY FIELD

σᵢ = intrinsic variance of Mᵢ

## VARIANCE DEFINITION

σᵢ is computed as cross-country temporal variance of Mᵢ within each domain

## Propagation Law

ε = √(∑ (wᵢ² · σᵢ²)) · 100


---

## DECISION FUNCTION

Score = QSSI_adj − ε

Rank = arg sort ↓ (Score)


---

## NORMALIZATION LAWS

∀ Mᵢ: 0 ≤ Mᵢ ≤ 1

∀ outputs: 0 ≤ QSSI ≤ 1
0 ≤ QSSI_scaled ≤ 100
0 ≤ QSSI_adj ≤ 100
0 ≤ ε ≤ 5


---

## SYSTEM PROPERTIES

Deterministic Mapping

Closed Form Computation

No External Stochastic Dependency

Fully Reproducible State Transition

Version Locked Mathematics



---

## STATE TRANSITION MODEL

Sₜ → Sₜ₊₁ via:

Normalization → Aggregation → Scaling → Risk Adjustment → Uncertainty Propagation → Ranking


---

## CANONICAL INVARIANCE

QSSI is invariant under:

Dataset reordering

Country permutation

Time-index shift (within fixed Year slice)



---

## OUTPUT MANIFOLD

F(Country, Year) → (QSSI, QSSI_adj, ε, Score, Tier)


---

## END STATE

MODEL LAYER = CLOSED MATHEMATICAL SYSTEM
STATE = IMMUTABLE
VERSION = v2026.1.0 🔒
