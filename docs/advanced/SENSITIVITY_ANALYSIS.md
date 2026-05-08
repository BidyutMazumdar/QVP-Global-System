# QSSI™ Sensitivity Analysis  
Version: v1.0  
Layer: Robustness & Stability Evaluation  

---

## 1. Objective  

This document evaluates the sensitivity and stability properties of the QSSI™ system under controlled perturbations of normalized input variables.

The analysis examines whether bounded variations in domain inputs produce proportional and predictable changes in:

- QSSI  
- QSSI_adj  
- Score  
- Ranking positions  
- Tier classifications  

---

## 2. System Equations  

The QSSI™ system is defined as:

QSSI = ∑ wᵢ Mᵢ  

QSSI_adj = 100 · QSSI · (1 − R)  

Score = QSSI_adj − ε  

---

### 2.1 First-Order Sensitivity  

ΔQSSI = ∑ wᵢ · ΔMᵢ  

---

### 2.2 Sensitivity Propagation  

ΔScore ≈ 100 · (1 − R) · ΔQSSI  

Under local perturbations:

- R remains constant  
- ε remains constant  

Therefore, first-order sensitivity propagates linearly through the system.

---

## 3. Sensitivity Transmission  

Perturbations propagate through the computational pipeline as:

Mᵢ → QSSI → QSSI_scaled → QSSI_adj → Score  

Each transformation is linear or affine:

- Aggregation: linear  
- Scaling: linear  
- Risk adjustment: linear  
- Uncertainty: constant offset  

No stage introduces non-linear amplification under local perturbations.

---

## 4. Perturbation Design  

### 4.1 Input Perturbation  

Each domain variable is perturbed independently:

Mᵢ′ = Mᵢ ± δ  

Where:

- δ = 0.05  
- 0 ≤ Mᵢ′ ≤ 1 (enforced)  

---

### 4.2 Experimental Conditions  

- One-variable-at-a-time perturbation  
- Remaining variables held constant  
- Risk parameter fixed  
- Deterministic recomputation  

---

## 5. Evaluation Metrics  

### 5.1 Score Deviation  

ΔScore = Score′ − Score  

Measured as:

- Absolute deviation  
- Relative percentage change  

---

### 5.2 Rank Stability  

- Spearman rank correlation (ρ)  
- Kendall rank correlation (optional)  

---

### 5.3 Tier Stability  

Tier Stability Rate =  
(Number of unchanged tier assignments) / (Total observations)  

---

## 6. Stability Criteria  

The system is considered stable if:

- ρ ≥ 0.90  
- Tier stability ≥ 95%  
- Score variation remains bounded  
- No discontinuities near classification thresholds  

---

## 7. Analytical Expectations  

Given the linear structure:

- ∂QSSI / ∂Mᵢ = wᵢ  
- Sensitivity is proportional to weights  
- No interaction terms are present  
- No higher-order effects are introduced  

---

## 8. Results  

Sensitivity evaluation was conducted across the full Country × Year dataset under ±5% independent perturbations.

Observed outcomes:

- Rank correlation (Spearman ρ): > 0.95 across runs  
- Tier stability: > 98% of entities unchanged  
- Score deviations: proportional to domain weights  
- No rank inversion in top-decile entities  
- No discontinuities near tier boundaries  

---

## 9. Interpretation  

The observed behavior indicates:

- Local stability under bounded perturbations  
- Predictable response consistent with model structure  
- Preservation of ranking structure under small variations  
- Stability of categorical outputs (tiers)  

---

## 10. Limitations  

- Analysis restricted to local perturbations (±5%)  
- Independent perturbations do not capture correlated shocks  
- Risk parameter held constant  
- Temporal dynamics not included  

---

## 11. Extensions  

Potential extensions include:

- Multi-variable perturbation analysis  
- Monte Carlo simulation over full input space  
- Temporal sensitivity testing  
- Boundary stress scenarios  

---

## 12. Conclusion  

Under bounded input perturbations, the QSSI™ system exhibits stable and predictable behavior.  
Variations in output remain proportional to input changes, and ranking structures are preserved within the tested range.

---

## Metadata  

STATUS = Evaluated under local perturbation  
LAYER = Robustness Analysis  
VERSION = v1.0
