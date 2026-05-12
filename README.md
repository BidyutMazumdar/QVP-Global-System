# QSSI™ — Quantum Sovereign Security Index System  
## A Sovereign-Grade Computational Architecture for Deterministic Security Scoring, Risk-Adjusted Ranking, and Reproducible Global Benchmarking

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20127955.svg)](https://doi.org/10.5281/zenodo.20127955)
[![Canonical Release](https://img.shields.io/badge/Canonical%20Release-2026.2.0--A-black)](#integrity--version-discipline)
[![Live Build](https://img.shields.io/badge/Live%20Build-v2026.2.0-blue)](#integrity--version-discipline)
[![License](https://img.shields.io/badge/License-Proprietary-red)](PROPRIETARY_LICENSE.md)

---

# Executive Summary

**QSSI™ (Quantum Sovereign Security Index System)** is a sovereign-grade computational benchmarking architecture engineered for deterministic evaluation, risk-adjusted ranking, and reproducible comparative analysis of national security readiness across global jurisdictions.

The system integrates formal mathematical modeling, machine-learning assisted interpretability, structured validation logic, deterministic computational execution, and deployable public infrastructure into a unified governance-grade analytical framework.

QSSI™ functions simultaneously as:

- a formal computational index system  
- a deployable sovereign analytics platform  
- a machine-readable public API  
- an interactive strategic intelligence dashboard  
- a DOI-bound scholarly artifact  
- a reproducible governance architecture  

---

# Live Access

### API Base

https://qvp-global-system-production.up.railway.app/

### Interactive Dashboard

https://qvp-global-system-production.up.railway.app/dashboard

### Rankings (JSON)

https://qvp-global-system-production.up.railway.app/rankings

### GitHub Repository

https://github.com/BidyutMazumdar/QVP-Global-System

---

# Canonical DOI

**Primary DOI**

https://doi.org/10.5281/zenodo.20127955

**Versioned Scholarly Archive**

Zenodo Canon Release — Immutable and DOI-bound

---

# System Purpose

QSSI™ was developed to provide a formalized computational framework for evaluating sovereign digital security preparedness using deterministic multi-factor scoring and bounded uncertainty estimation.

The architecture enables:

- sovereign cybersecurity benchmarking  
- post-quantum readiness assessment  
- AI defense capability evaluation  
- legal-regulatory preparedness measurement  
- resilience capacity analysis  
- comparative strategic intelligence modeling  
- policy stress-testing and scenario simulation  

---

# Methodological Core

QSSI™ evaluates sovereign security readiness across four normalized dimensions:

| Dimension | Description |
|-----------|-------------|
| **PQC** | Post-Quantum Cryptographic Readiness |
| **AI** | AI Defense and Cyber Capability |
| **LEGAL** | Regulatory and Legal Preparedness |
| **RES** | Systemic Resilience Capacity |

Each metric satisfies:

```math
M_i \in [0,1]
```

---

# Formal Mathematical Model

## Base Index

```math
QSSI = \sum_{i=1}^{n} (w_i \cdot M_i)
```

---

## Scaled Score

```math
QSSI_{scaled}=100\cdot QSSI
```

---

## Risk-Adjusted Score

```math
QSSI_{adj}=QSSI_{scaled}\cdot(1-Risk)
```

---

## Uncertainty Bound

```math
\epsilon=
\sqrt{
\sum_{i=1}^{n}
(w_i^2\sigma_i^2)
}
\cdot100
```

---

## Final Sovereign Score

```math
Score_i=QSSI_{adj,i}-\epsilon_i
```

---

# Formal System Definition

```math
F:(M,Risk,\sigma)\rightarrow(QSSI_{adj},\epsilon,Rank,Cert)
```

Where:

```math
M\in[0,1]^4
```

```math
Risk\in[0,1]
```

```math
\sigma\in\mathbb{R}_+^4
```

Outputs:

- **QSSI_adj** → risk-adjusted score  
- **ε** → uncertainty bound  
- **Rank** → ordinal ranking  
- **Cert** → probabilistic validity indicator  

---

# Formal Properties

QSSI™ satisfies the following theoretical guarantees:

## Determinism

Identical input produces identical output.

## Boundedness

```math
QSSI\in[0,100]
```

## Continuity

Bounded sensitivity under controlled perturbation.

## Reproducibility

Version-bound and hash-verifiable outputs.

## Auditability

Complete computational traceability.

## Structural Validity

Constraint-preserving score generation.

---

# Computational Architecture

```text
UI Layer
   ↓
API Layer
   ↓
Compute Engine
   ↓
Validation Logic
   ↓
Risk Adjustment Layer
   ↓
Interpretability Layer (SHAP/PCA)
   ↓
Output Surface
```

---

# Validation & Integrity Framework

QSSI™ incorporates:

- structured data normalization  
- min-max scaling  
- deterministic weight application  
- bounded metric validation  
- consistency verification  
- uncertainty propagation  
- probabilistic certification (`Cert_VALID`)  
- SHA3-256 cryptographic hashing  
- reproducibility manifest generation  

Ensuring outputs remain:

- computationally consistent  
- structurally valid  
- scientifically interpretable  
- audit-verifiable  

---

# Explainability Layer

The system includes machine-learning interpretability modules:

- **Feature Importance Analysis**
- **SHAP Value Attribution**
- **Principal Component Analysis**
- **Correlation Matrix Diagnostics**
- **Prediction Validation Engine**

Artifacts generated:

- `feature_importance.csv`
- `feature_importance.png`
- `QSSI_SHAP_SUMMARY.png`
- `QSSI_PCA_MAP.png`
- `actual_vs_predicted.png`
- `validation_results.csv`

---

# Public API

| Endpoint | Type | Description |
|----------|------|-------------|
| `/` | Root | Base service entry |
| `/rankings` | JSON API | QSSI rankings |
| `/dashboard` | Interface | Interactive dashboard |

### Example Request

```bash
curl https://qvp-global-system-production.up.railway.app/rankings
```

---

# Repository Structure

```text
AI/
Animation/
COMPUTATIONAL SYSTEM/
Core_Theory/
POLICY_APPLICATION/
RESULTS/
ROBUSTNESS LAYER/
SCIENTIFIC INTERPRETATION/
THEORETICAL EXTENSIONS/
```

---

# Results Package

Generated reproducible artifacts include:

- QSSI_GLOBAL_RANKINGS_2026.csv
- QSSI_TOP40.csv
- QSSI_GLOBAL_MAP.html
- QSSI_PCA_MAP.png
- QSSI_TOP40_HEATMAP.png
- QSSI_REPORT.tex
- QSSI_MANIFEST.json
- best_model.joblib
- qssi_random_forest.joblib
- scaler.joblib
- minmax_scaler.joblib
- pca_model.joblib
- model_metrics.json
- shap_values.csv
- prediction_output.csv

---

# Reproducibility Statement

All QSSI™ outputs are reproducible under:

- fixed input dataset  
- declared weight vector  
- deterministic execution  
- canonical release version  
- immutable DOI archive  

System outputs remain:

- deterministic  
- version-bound  
- cryptographically hash-verifiable  

---

# Deployment Status

**PUBLIC / LIVE / VERSIONED / DEPLOYED**

Current status:

- API active  
- Dashboard live  
- DOI registered  
- Repository maintained  
- Results reproducible  

System validity does not depend on continuous uptime.

Verification remains possible through:

- deterministic computation  
- archived repository state  
- DOI-bound canonical release  
- result manifests  
- execution artifacts  

---

# Installation

```bash
git clone https://github.com/BidyutMazumdar/QVP-Global-System.git

cd QVP-Global-System

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt

python api/app.py
```

---

# Integrity & Version Discipline

## Canonical Release (DOI-Bound)

```text
2026.2.0-A
```

## Live Build

```text
v2026.2.0
```

### Governance Rule

- methodological changes → canonical increment  
- deployment changes → live build increment  

---

# Integrity Logic

```math
Hash=SHA3\text{-}256(Input)
```

```math
System\_ID=
SHA3\text{-}256(System||Version||Timestamp)
```

---

# Citation

Mazumdar, B. (2026).  
**Quantum Veil Protocol (QVP) — Global System 2026: Sovereign Digital Security Index (QSSI).**  
Zenodo.

DOI:

https://doi.org/10.5281/zenodo.20127955

---

# Author

## Dr. B. Mazumdar, D.Sc. (Hon.), D.Litt. (Hon.)

**Architect of Modern Statehood**  
**Founder & Principal Architect, FAIR+D Canon™**  
**Proprietary Sovereign Systems Architecture & Governance Framework**

Independent Researcher  
Macro-Financial Systems  
AI Governance  
Sovereign Risk Modeling  
Computational Policy Optimization  
Global Systems Architecture

ORCID:

https://orcid.org/0009-0007-5615-3558

Publication Repository:

Zenodo

---

# License

**Proprietary License — All Rights Reserved**

Unauthorized reproduction, derivative deployment, or institutional redistribution prohibited without explicit permission.

---

# Status

```text
PUBLIC
LIVE
VERSIONED
DEPLOYED
DOI-BOUND
REPRODUCIBLE
```

---

© 2026 Dr. B. Mazumdar
All Rights Reserved.
