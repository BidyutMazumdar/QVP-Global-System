# QSSI™ — Quantum Sovereign Security Index System

---

## 🌍 Overview

QSSI™ (Quantum Sovereign Security Index System) is a sovereign-grade global security intelligence platform designed to compute, benchmark, and visualize national security performance across countries using a structured, multi-dimensional index model.

The system establishes a **deterministic, mathematically rigorous, and computationally reproducible foundation** for real-time security evaluation, strategic risk assessment, and policy-grade decision intelligence across sovereign systems.

---

## 🔗 DOI (Canonical Record)

**https://doi.org/10.5281/zenodo.19375967**

---

## 🧾 Citation

**Bidyut, M. (2026). Quantum Veil Protocol (QVP) — Global System 2026: Sovereign Digital Security Index (QSSI), Methodology, Mathematical Architecture, and Platform Framework (2026.1.0). Zenodo. https://doi.org/10.5281/zenodo.19375967**

---

## 🆔 ORCID

**https://orcid.org/0009-0007-5615-3558**

---

## ⚙️ Core Mathematical Framework

**M = (PQC, AI, LEGAL, RES) ∈ [0,1]⁴**  
**w = (0.30, 0.25, 0.25, 0.20), Σ wᵢ = 1**  
**Risk ∈ [0,1]**

---

## 📐 Deterministic Model

**QSSI = Σ (wᵢ · Mᵢ)**  
**QSSI_scaled = 100 × QSSI**  
**QSSI_adj = QSSI_scaled × (1 − Risk)**  
**ΔQSSI = QSSI_scaled − QSSI_adj**

---

## 📊 Uncertainty Model

**σᵢ² = Var(Mᵢ)**  
**ε = √(Σ (wᵢ² · σᵢ²)) × 100**  
**QSSI_final = QSSI_adj ± ε**  
**0 ≤ ε ≤ 5**

---

## 📈 Probabilistic Framework

**QSSIᵢ ~ 𝒩(μᵢ, ε²)**  
**μᵢ = QSSI_adjᵢ**

**P(i ≻ j) = Φ((μᵢ − μⱼ) / √(ε² + ε²))**

**E[Rankᵢ] = 1 + Σⱼ≠ᵢ P(j ≻ i)**

**Scoreᵢ = μᵢ − ε**

**Rank = sort_desc(Scoreᵢ)**

---

## 🧩 Tier Classification

**Tier A: QSSI_adj ≥ 85**  
**Tier B: 75 ≤ QSSI_adj < 85**  
**Tier C: 50 ≤ QSSI_adj < 75**  
**Tier D: QSSI_adj < 50**

---

## 🔀 Multi-Data Fusion

**QSSI_fused = Σ (αₖ · QSSI^(k)), Σ αₖ = 1**

**σ_fused² = Σ (αₖ² σₖ²) + 2 Σ_{k<l} αₖ αₗ Cov(k,l)**

**QSSI_fused_final = QSSI_fused ± σ_fused**

---

## 🏅 Certification Model

**μ_global = mean(QSSI_adj)**  
**σ_global = std(QSSI_adj)**

**Cert_VALID ⇔ (QSSI_adj − ε) ≥ μ_global − 0.5·σ_global ∧ Audit_PASS**

**P(QSSI_adj ≥ Threshold) = 1 − Φ((Threshold − μ) / ε)**

**ID_cert = SHA3-256(System ∥ Dataset ∥ Version ∥ Timestamp)**

---

## 🔍 Audit System

**S100 ⇔ Data Integrity**  
**S200 ⇔ Computation Consistency**  
**S300 ⇔ Ranking Verification**  
**S400 ⇔ Certification Validation**

**Audit_PASS ⇔ S100 ∧ S200 ∧ S300 ∧ S400**

---

## 🏗️ System Architecture

**System = Frontend ∧ API ∧ Engine ∧ Data ∧ Certification ∧ Audit**

**Flow = UI → API → Engine → Data → Certification → Audit**

**Deploy = Data ∧ Compute ∧ Validate ∧ Publish**

**Scale(System) ∝ Nodes × Throughput**

**Distributed Nodes ∧ Load Balancing ∧ Parallel Execution ∧ Stateless Architecture**

---

## 🔐 Security Model

**Hash = SHA3-256(Input)**  
**System_ID = SHA3-256(System ∥ Version ∥ Timestamp)**

**Integrity ⇔ Hash Valid**  
**Authenticity ⇔ Deterministic ID**  
**Tamper ⇔ Hash Mismatch**

---

## 🧠 Computational Core (Python)

```python
import pandas as pd
import numpy as np
import hashlib
from scipy.stats import norm

WEIGHTS = np.array([0.30, 0.25, 0.25, 0.20])
SIGMA = np.array([0.05, 0.06, 0.04, 0.05])

def compute_qssi(df):
    M = df[["PQC","AI","LEGAL","RES"]].values
    df["QSSI"] = np.dot(M, WEIGHTS)
    df["QSSI_scaled"] = df["QSSI"] * 100
    df["QSSI_adj"] = df["QSSI_scaled"] * (1 - df["Risk"])

    df["ε"] = np.sqrt(np.sum((WEIGHTS**2)*(SIGMA**2))) * 100

    df["Score"] = df["QSSI_adj"] - df["ε"]
    df = df.sort_values(by="Score", ascending=False).reset_index(drop=True)
    df["Rank"] = np.arange(1, len(df)+1)

    threshold = df["QSSI_adj"].mean() - 0.5 * df["QSSI_adj"].std()
    prob = 1 - norm.cdf((threshold - df["QSSI_adj"]) / df["ε"])

    df["Cert_VALID"] = prob >= 0.5
    return df

def system_hash(df):
    raw = f"{df.to_csv(index=False)}_{WEIGHTS}_2026.1.0-A".encode()
    return hashlib.sha3_256(raw).hexdigest()


---

🧱 Formal System Definition

F : (M, Risk, σ) → (QSSI_adj, ε, Rank, Cert)

D = [0,1]⁴ × [0,1] × ℝ⁴₊
R = [0,100] × [0,5] × ℝ × {0,1}

Closure ⇔ ∀ input ∈ D ⇒ output ∈ R
Determinism ⇔ F(x₁) = F(x₂) ⇔ x₁ = x₂
Continuity ⇔ F continuous over D
Boundedness ⇔ QSSI_adj ∈ [0,100], ε ∈ [0,5]
Reproducibility ⇔ Dataset ∧ Model ∧ Weights ∧ Version Fixed


---

🧩 System Composition

QVP_System = Architecture ∧ Computation ∧ Probability ∧ Certification ∧ Audit ∧ Security ∧ Deployment

∀ t ≥ t₀ : System(t) = Deterministic ∧ Probabilistic ∧ Secure ∧ Scalable ∧ Verifiable


---

🔒 Version Control

Version = 2026.1.0-A
State = IMMUTABLE
Modification ⇒ Version Increment Required


---

👤 Author

Dr. B. Mazumdar, D.Sc. (Hon.), D.Litt. (Hon.)
Architect of Modern Statehood
Founder & Principal Architect, FAIR+D Canon™
Proprietary Sovereign Systems Architecture & Governance Framework


---

© Copyright

© 2026 Dr. B. Mazumdar. All Rights Reserved.
Proprietary Sovereign Digital Security Infrastructure Framework


---

🌐 System Access Layer

🔗 Core Endpoints

API Base
https://qvp-global-system-production.up.railway.app/

Live Dashboard (UI Layer)
https://qvp-global-system-production.up.railway.app/dashboard

Ranking Data Endpoint (JSON API)
https://qvp-global-system-production.up.railway.app/rankings


---

📡 Endpoint Description

Endpoint	Type	Description

/	Status	API service health check
/rankings	Data API	Real-time QSSI rankings (JSON)
/dashboard	UI Layer	Live interactive dashboard



---

⚙️ Access Characteristics

Real-time computed data (no static caching)
API-driven frontend architecture
Cloud-native deployment (Railway)
Stateless service design
Direct integration ready (REST API)


---
