# QSSI™ — Quantum Sovereign Security Index System

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19375967.svg)](https://doi.org/10.5281/zenodo.19375967)
[![Canonical Release](https://img.shields.io/badge/Canonical%20Release-2026.1.0--A-black.svg)](#integrity--version-discipline)
[![Live Build](https://img.shields.io/badge/Live%20Build-v2026.1.1-brightgreen.svg)](#integrity--version-discipline)
[![API](https://img.shields.io/badge/API-live-success.svg)](https://qvp-global-system-production.up.railway.app/)
[![Dashboard](https://img.shields.io/badge/Dashboard-live-success.svg)](https://qvp-global-system-production.up.railway.app/dashboard)
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](./PROPRIETARY_LICENSE.md)

---

## Executive Summary

QSSI™ (Quantum Sovereign Security Index System) is a **sovereign-grade computational benchmarking platform** designed to evaluate and rank national security readiness through a deterministic, multi-dimensional index model.

The system integrates:

- formal mathematical modeling  
- live computational execution  
- machine-readable API outputs  
- interactive dashboard visualization  
- version-controlled reproducibility  
- DOI-bound scholarly anchoring  

QSSI™ functions as a **deployable governance-grade analytical system**, bridging theoretical modeling with real-world computational infrastructure.

---

## Live Access

**API Base**  
https://qvp-global-system-production.up.railway.app/

**Dashboard**  
https://qvp-global-system-production.up.railway.app/dashboard

**Rankings (JSON)**  
https://qvp-global-system-production.up.railway.app/rankings

---

## Live Demonstration

**Primary Demonstration (Latest Build)**  
▶ https://drive.google.com/file/d/1eWq_lMJGfRbwSP8s7wRjJTXAaYmqQaWl/view  

**Archive Demonstration**  
▶ https://drive.google.com/file/d/1AKQ2ZeNlJoG9VE7if_hypskUP1KHmGiA/view  

**System Note**  
The demonstration videos provide verified execution snapshots of the deployed system, ensuring transparency and reproducibility.

---

## Deployment Status Notice

The system is deployed on a cloud-based infrastructure environment.

While the API and dashboard are publicly accessible, uptime may vary depending on infrastructure constraints.

System validity does not depend on continuous uptime. It remains verifiable through:

- deterministic computation  
- reproducible codebase  
- archived demonstrations  
- DOI-bound canonical release  

This ensures audit-level integrity independent of deployment state.

---

## Scholarly Relevance

This repository provides a combination of:

- formalized index methodology  
- live computational implementation  
- machine-readable outputs  
- reproducible version-controlled architecture  

It serves as a bridge between theoretical sovereign modeling and deployable computational governance systems.

---

## Methodological Core

QSSI™ evaluates sovereign security readiness across four normalized dimensions:

- **PQC** — Post-Quantum Cryptographic Readiness  
- **AI** — AI Defense and Cyber Capability  
- **LEGAL** — Regulatory and Legal Preparedness  
- **RES** — Systemic Resilience Capacity  

Each dimension satisfies:

M ∈ [0,1]

---

## Mathematical Model

The QSSI™ score is defined as:

QSSI = Σ (wᵢ · Mᵢ)

QSSI_scaled = 100 · QSSI  

QSSI_adj = QSSI_scaled · (1 − Risk)

Uncertainty bound:

ε = √(Σ (wᵢ² · σᵢ²)) · 100  

Final score:

Scoreᵢ = QSSI_adjᵢ − ε  

---

## Formal System Definition

F : (M, Risk, σ) → (QSSI_adj, ε, Rank, Cert)

Where:

- M ∈ [0,1]^4  
- Risk ∈ [0,1]  
- σ ∈ ℝ⁺⁴  

Outputs:

- QSSI_adj → risk-adjusted score  
- ε → uncertainty bound  
- Rank → ordinal ranking  
- Cert → probabilistic validity flag  

---

## Formal Properties

The QSSI™ system satisfies:

- **Determinism** → identical input produces identical output  
- **Boundedness** → QSSI ∈ [0,100]  
- **Continuity** → bounded sensitivity to input variation  
- **Reproducibility** → version-bound and hash-verifiable outputs  

---

## Validation & Data Integrity

The system incorporates:

- structured data normalization  
- bounded metric constraints  
- cross-dimensional consistency checks  
- probabilistic validation (`Cert_VALID`)  
- cryptographic hashing (SHA3-256)  

Ensuring outputs remain:

> computationally consistent  
> structurally valid  
> audit-verifiable  

---

## Reproducibility Statement

All QSSI™ outputs are reproducible under:

- fixed input dataset  
- defined weight vector  
- declared canonical version  

System outputs are deterministic, hash-verifiable, and version-bound.

---

## Architecture

UI Layer  
→ API Layer  
→ Compute Engine  
→ Dataset Layer  
→ Validation Logic  
→ Output Surface  

A full-stack sovereign intelligence architecture integrating computation, validation, and presentation.

---

## Public API

| Endpoint      | Type        | Description                |
|--------------|------------|----------------------------|
| `/`          | Root       | Base service entry         |
| `/rankings`  | Data API   | QSSI rankings (JSON)       |
| `/dashboard` | Interface  | Interactive dashboard      |

### Example Request

```bash
curl https://qvp-global-system-production.up.railway.app/rankings
```

---

## Institutional Use Cases

- sovereign cyber readiness benchmarking  
- comparative resilience analysis  
- policy simulation and stress testing  
- strategic intelligence visualization  
- academic reproducibility research  
- governance infrastructure demonstration  

---

## Limitations

- relies on modeled public-domain inputs  
- does not include classified intelligence  
- simplifies complex sovereign systems  
- sensitive to data quality  

Intended strictly for analytical benchmarking.

---

## Documentation

- `README.md` — overview  
- `DATA_SOURCES.md` — data provenance  
- `docs/` — technical documentation  
- `reports/` — outputs  

---

## Installation

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

## Integrity & Version Discipline

**Canonical Release (DOI-bound)**  
2026.1.0-A  

**Live Build**  
v2026.1.1  

### Governance Rule

- methodological changes → canonical increment  
- deployment changes → live build increment  

### Integrity Logic

Hash = SHA3-256(Input)  
System_ID = SHA3-256(System || Version || Timestamp)  

---

## DOI & Citation

DOI: https://doi.org/10.5281/zenodo.19375967  

Mazumdar, B. (2026).  
*Quantum Veil Protocol (QVP) — Global System 2026: Sovereign Digital Security Index (QSSI)*  
Zenodo. https://doi.org/10.5281/zenodo.19375967  

---

## Author

Dr. B. Mazumdar  
Independent Researcher — Macro-Financial Systems, AI Governance, Sovereign Risk  

Founder, FAIR+D Canon™  
ORCID: https://orcid.org/0009-0007-5615-3558  

Publication Repository: Zenodo  

---

## License

Proprietary License — All Rights Reserved  

---

## Status

PUBLIC / LIVE / VERSIONED / DEPLOYED  

- API active  
- Dashboard live  
- DOI registered  
- Repository maintained  

---

## Repository

https://github.com/BidyutMazumdar/QVP-Global-System

© 2026 Dr. B. Mazumdar
