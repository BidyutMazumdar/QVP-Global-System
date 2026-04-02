# QSSI™ — Quantum Sovereign Security Index System

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19375967.svg)](https://doi.org/10.5281/zenodo.19375967)  
[![Canonical Release](https://img.shields.io/badge/Canonical%20Release-2026.1.0--A-black.svg)](#integrity--version-discipline)  
[![Live Build](https://img.shields.io/badge/Live%20Build-v2026.1.1-brightgreen.svg)](#integrity--version-discipline)  
[![API](https://img.shields.io/badge/API-live-success.svg)](https://qvp-global-system-production.up.railway.app/)  
[![Dashboard](https://img.shields.io/badge/Dashboard-live-success.svg)](https://qvp-global-system-production.up.railway.app/dashboard)  
[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](./PROPRIETARY_LICENSE.md)

> **A sovereign-grade, computationally deployable national security benchmarking platform for deterministic scoring, risk-adjusted ranking, and live comparative intelligence across nations.**

---

## Executive Summary

**QSSI™ (Quantum Sovereign Security Index System)** is a **research-grade and platform-grade sovereign security benchmarking architecture** designed to compute, rank, and visualize national security readiness through a reproducible, weighted, multi-dimensional index model.

It is presented not merely as a conceptual framework, but as a **live, versioned computational system** with:

- deterministic scoring
- risk-adjusted sovereign ranking
- machine-readable API outputs
- public dashboard deployment
- version-disciplined computational integrity
- formal scholarly anchoring via DOI

QSSI™ is structured for:

- institutional review
- computational governance demonstration
- policy-facing analytical interpretation
- reproducible public benchmarking
- infrastructure-grade platform presentation

---

## Live Access

- **API Base:** [https://qvp-global-system-production.up.railway.app/](https://qvp-global-system-production.up.railway.app/)
- **Dashboard:** [https://qvp-global-system-production.up.railway.app/dashboard](https://qvp-global-system-production.up.railway.app/dashboard)
- **Rankings (JSON):** [https://qvp-global-system-production.up.railway.app/rankings](https://qvp-global-system-production.up.railway.app/rankings)

---

## Why This Repository Matters

QSSI™ is designed as a **deployable sovereign systems reference** rather than a static white-paper artifact.

It combines:

- formal methodological structure
- live computational execution
- publicly inspectable outputs
- version-bound reproducibility
- integrity-aware release discipline
- institutional documentation architecture

This repository may be relevant for:

- academic and scholarly reviewers
- public policy and strategic analysis observers
- computational governance audiences
- infrastructure and platform evaluators
- grant, award, and institutional screening contexts

---

## Methodological Core

QSSI™ evaluates sovereign security readiness across four normalized dimensions:

- **PQC** — post-quantum readiness
- **AI** — AI defense and cyber capability
- **LEGAL** — legal and regulatory preparedness
- **RES** — systemic resilience capacity

### Canonical Scoring Model

```text
QSSI = sum(w_i * M_i)
QSSI_scaled = 100 * QSSI
QSSI_adj = QSSI_scaled * (1 - Risk)
epsilon = sqrt(sum((w_i^2) * (sigma_i^2))) * 100
Score_i = QSSI_adj_i - epsilon
```

### Tier Structure

- **Tier A** — `QSSI_adj >= 85`
- **Tier B** — `75 <= QSSI_adj < 85`
- **Tier C** — `50 <= QSSI_adj < 75`
- **Tier D** — `QSSI_adj < 50`

> This README provides an executive mathematical summary only. Detailed implementation and methodological controls should be maintained in the source code and technical documentation.

---

## Public API Surface

| Endpoint | Type | Function |
|---|---|---|
| `/` | Service Root | Base service entry point |
| `/rankings` | Data API | Live QSSI rankings in JSON |
| `/dashboard` | Presentation Layer | Interactive dashboard interface |

### Example Request

```bash
curl https://qvp-global-system-production.up.railway.app/rankings
```

---

## Computational Reference (Python)

```python
import pandas as pd
import numpy as np
import hashlib
from scipy.stats import norm

WEIGHTS = np.array([0.30, 0.25, 0.25, 0.20])
SIGMA = np.array([0.05, 0.06, 0.04, 0.05])

CANONICAL_RELEASE = "2026.1.0-A"
LIVE_BUILD = "v2026.1.1"

def compute_qssi(df):
    M = df[["PQC", "AI", "LEGAL", "RES"]].values
    df["QSSI"] = np.dot(M, WEIGHTS)
    df["QSSI_scaled"] = df["QSSI"] * 100
    df["QSSI_adj"] = df["QSSI_scaled"] * (1 - df["Risk"])
    df["epsilon"] = np.sqrt(np.sum((WEIGHTS ** 2) * (SIGMA ** 2))) * 100
    df["Score"] = df["QSSI_adj"] - df["epsilon"]
    df = df.sort_values(by="Score", ascending=False).reset_index(drop=True)
    df["Rank"] = np.arange(1, len(df) + 1)

    threshold = df["QSSI_adj"].mean() - 0.5 * df["QSSI_adj"].std()
    prob = 1 - norm.cdf((threshold - df["QSSI_adj"]) / df["epsilon"])
    df["Cert_VALID"] = prob >= 0.5
    return df

def system_hash(df):
    raw = f"{df.to_csv(index=False)}_{WEIGHTS}_{CANONICAL_RELEASE}".encode()
    return hashlib.sha3_256(raw).hexdigest()
```

---

## Formal System Definition

```text
F : (M, Risk, sigma) -> (QSSI_adj, epsilon, Rank, Cert)
```

Where:

- `M ∈ [0,1]^4`
- `Risk ∈ [0,1]`
- `sigma ∈ R_+^4`

Core properties:

- **deterministic**
- **bounded**
- **continuous**
- **reproducible**
- **version-bound**

---

## Architecture

```text
UI Layer -> API Layer -> Compute Engine -> Dataset Layer -> Validation Logic -> Output Surface
```

QSSI™ is structured as a **live sovereign intelligence platform** with:

- dashboard presentation
- machine-readable API output
- deterministic scoring engine
- structured dataset layer
- reproducibility-aware validation logic

---

## Repository Structure

```text
QVP-Global-System/
├── api/
├── dataset/
├── docs/
├── engine/
├── reports/
├── .gitignore
├── DATA_SOURCES.md
├── PROPRIETARY_LICENSE.md
├── README.md
└── requirements.txt
```

---

## Integrity & Version Discipline

### Version Declaration

- **Canonical Scholarly Release (DOI):** `2026.1.0-A`
- **Current Live Deployment Build:** `v2026.1.1`
- **Canonical State:** `IMMUTABLE`

### Governance Rule

- substantive methodological or computational changes require a **canonical version increment**
- deployment, interface, or infrastructure refinements may increment the **live build** without altering the DOI-bound canonical release

### Integrity Logic

```text
Hash = SHA3-256(Input)
System_ID = SHA3-256(System || Canonical_Release || Timestamp)
```

---

## Documentation

- [`README.md`](./README.md) — public institutional overview
- [`DATA_SOURCES.md`](./DATA_SOURCES.md) — data provenance discipline
- [`PROPRIETARY_LICENSE.md`](./PROPRIETARY_LICENSE.md) — governing legal instrument
- [`docs/`](./docs/) — technical and methodological documentation
- [`reports/`](./reports/) — generated outputs and publication artifacts

---

## Local Installation

```bash
git clone https://github.com/BidyutMazumdar/QVP-Global-System.git
cd QVP-Global-System
python -m venv .venv
```

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
python api/app.py
```

> Adjust the runtime entrypoint if your production app is wired differently.

---

## Intended Use

QSSI™ may be used for:

- sovereign digital security benchmarking
- comparative resilience analysis
- policy-oriented exploratory assessment
- live ranking demonstrations
- research and methodological presentation
- public platform architecture showcase

> QSSI™ is a structured benchmarking and analytical platform. It does **not** claim to replace classified state systems, intelligence agencies, or sovereign defense apparatus.

---

## Canonical DOI Record

- **DOI:** [https://doi.org/10.5281/zenodo.19375967](https://doi.org/10.5281/zenodo.19375967)
- **ORCID:** [https://orcid.org/0009-0007-5615-3558](https://orcid.org/0009-0007-5615-3558)

### Canonical Citation

```text
Bidyut, M. (2026). Quantum Veil Protocol (QVP) — Global System 2026: Sovereign Digital Security Index (QSSI), Methodology, Mathematical Architecture, and Platform Framework (Version 2026.1.0-A). Zenodo. https://doi.org/10.5281/zenodo.19375967
```

---

## Author

**Dr. B. Mazumdar, D.Sc. (Hon.), D.Litt. (Hon.)**  
Architect of Modern Statehood  
Founder & Principal Architect, FAIR+D Canon™

---

## License

This repository is governed by a **proprietary license**.

- See: [`PROPRIETARY_LICENSE.md`](./PROPRIETARY_LICENSE.md)

**High-level summary:**

- all rights reserved unless expressly granted
- no unauthorized commercial reuse
- no derivative republication without permission
- no institutional repackaging without express authorization

> Attribution alone does **not** create usage rights.

---

## Status

**Current State:** `PUBLIC / LIVE / VERSIONED / DEPLOYED`

- Canonical DOI release: `2026.1.0-A`
- Current live deployment build: `v2026.1.1`
- Repository active
- API reachable
- Dashboard published
- DOI minted
- Documentation active

---

## Repository

- **GitHub:** [https://github.com/BidyutMazumdar/QVP-Global-System](https://github.com/BidyutMazumdar/QVP-Global-System)

---

© 2026 Dr. B. Mazumdar. All Rights Reserved.
