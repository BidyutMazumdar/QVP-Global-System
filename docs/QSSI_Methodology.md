# QSSI™ Methodology (v2026.1.0-CX — Canonical Locked Edition)

This document defines the formal mathematical, probabilistic, and computational framework of the Quantum Veil Protocol (QVP) — Sovereign Digital Security Index (QSSI).

---

## 1. Core Model (Canonical Form)

QSSI_adj = 100 · ( Σ_{i=1}^{4} w_i M_i ) · (1 − Risk)

Where:

QSSI = Σ_{i=1}^{4} (w_i · M_i)  
QSSI_scaled = 100 × QSSI  
QSSI_adj = QSSI_scaled × (1 − Risk)  
ΔQSSI = QSSI_scaled − QSSI_adj  

---

## 2. Domain Definition

M_i ∈ [0,1]  
Risk ∈ [0,1]  
QSSI ∈ [0,1]  
QSSI_adj ∈ [0,100]  
ε ∈ [0,5]  

---

## 3. Weights

Default weights:

w₁ (PQC) = 0.30  
w₂ (AI) = 0.25  
w₃ (LEGAL) = 0.25  
w₄ (RES) = 0.20  

Constraint:

Σ_{i=1}^{4} w_i = 1  
w_i ≥ 0  

---

## 4. Variable Constraints

0 ≤ PQC ≤ 1  
0 ≤ AI ≤ 1  
0 ≤ LEGAL ≤ 1  
0 ≤ RES ≤ 1  
0 ≤ Risk ≤ 1  

---

## 5. Normalization

AI = Score / 100  
LEGAL = (Value + 2.5) / 5  

All variables are normalized such that:

M_i ∈ [0,1]

---

## 6. Uncertainty Model (Deterministic Propagation)

ε = √( Σ_{i=1}^{4} (w_i² · σ_{M_i}²) ) × 100  

Where:

σ_{M_i} = uncertainty of normalized variable M_i  

Constraint:

0 ≤ ε ≤ 5  

Final representation:

QSSI_adj ± ε  

---

## 7. Probabilistic Ranking Model (Corrected)

Pairwise dominance probability:

P(i ≻ j) = Φ((μ_i − μ_j) / √(σ_i² + σ_j²))

Where:

μ_i = QSSI_adj (country i)  
σ_i ≈ ε (global uncertainty proxy applied uniformly across entities)  

Φ = cumulative distribution function (CDF) of the standard normal distribution  

Expected rank:

Rank_i = 1 + Σ_{j≠i} P(j ≻ i)

Risk-adjusted score:

Score_i = μ_i − σ_i  

Final ranking:

Rank = sort_desc(Score_i)

---

## 8. Ranking Rule (Deterministic Layer)

Primary ranking:

QSSI_adj (descending)

Tie-break hierarchy:

QSSI_adj ↓ → QSSI_scaled ↓ → PQC ↓ → Country ↑  

---

## 9. Tier Classification

Tier A: QSSI_adj ≥ 85  
Tier B: 75 ≤ QSSI_adj < 85  
Tier C: 50 ≤ QSSI_adj < 75  
Tier D: QSSI_adj < 50  

---

## 10. Risk Modeling Assumption

Risk is treated as an exogenous proxy variable (first-order approximation),  
acknowledging partial dependency with system variables (PQC, AI, LEGAL, RES).

---

## 11. Determinism Condition

QSSI(t) = QSSI(t′) ⇔ Input(t) = Input(t′)

---

## 12. System Properties

The QSSI system satisfies:

• Complete  
• Consistent  
• Deterministic  
• Reproducible  
• Verifiable  

---

## 13. Reproducibility Condition

Reproducible ⇔  

Dataset ∧ Weights ∧ Normalization ∧ Computation ∧ Version are fixed  

---

## 14. Mathematical Conditions

Monotonicity:

∂QSSI / ∂M_i = w_i > 0  

Risk Sensitivity:

∂QSSI_adj / ∂Risk < 0  

Boundedness:

0 ≤ QSSI ≤ 1  
0 ≤ QSSI_adj ≤ 100  

Continuity:

QSSI is continuous over domain [0,1]^4  

---

## 15. Model Scope

• No hidden parameters  
• No stochastic variation in core model  
• Probabilistic layer applied only in ranking  

---

## 16. Version Lock Condition

Version = v2026.1.0-CX  
State = IMMUTABLE  

Any modification ⇒ Version increment required  

---

© 2026 QVP — Quantum Veil Protocol Framework  
All Rights Reserved
