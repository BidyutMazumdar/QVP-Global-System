# QSSI™ Methodology (v2026.1.1)

This document defines the mathematical and computational framework of the QSSI™ model.

---

## 1. Core Model

QSSI = w₁·PQC + w₂·AI + w₃·LEGAL + w₄·RES

QSSI_scaled = 100 × QSSI

QSSI_adj = QSSI_scaled × (1 − Risk)

ΔQSSI = QSSI_scaled − QSSI_adj

---

## 2. Weights

Default weights:

w₁ (PQC)   = 0.30  
w₂ (AI)    = 0.25  
w₃ (LEGAL) = 0.25  
w₄ (RES)   = 0.20  

Constraint:
w₁ + w₂ + w₃ + w₄ = 1

---

## 3. Variable Constraints

0 ≤ PQC ≤ 1  
0 ≤ AI ≤ 1  
0 ≤ LEGAL ≤ 1  
0 ≤ RES ≤ 1  
0 ≤ Risk ≤ 1  

---

## 4. Normalization

AI = Score / 100  
LEGAL = (Value + 2.5) / 5  

All variables are normalized to [0,1]

---

## 5. Ranking Rule

Countries are ranked based on:

QSSI_adj (descending order)

---

## 6. Tier Classification

Tier A: QSSI_adj ≥ 85  
Tier B: 75 ≤ QSSI_adj < 85  
Tier C: 50 ≤ QSSI_adj < 75  
Tier D: QSSI_adj < 50  

---

## 7. Risk Adjustment

QSSI_adj reduces score based on systemic risk.

Higher risk → lower adjusted score

---

## 8. Determinism Condition

QSSI(t) = QSSI(t′) ⇔ Input(t) = Input(t′)

---

## 9. System Properties

The QSSI system satisfies:

Complete  
Consistent  
Deterministic  
Reproducible  
Verifiable  

---

## 10. Notes

- No hidden parameters
- No stochastic variation in base model
- Fully reproducible with identical input data
