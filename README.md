# QSSI™ — Quantum Sovereign Security Index System

![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19375967-blue)
![Version](https://img.shields.io/badge/Version-2026.1.0--A-black)
![API](https://img.shields.io/badge/API-Live-success)
![Dashboard](https://img.shields.io/badge/Dashboard-Live-success)
![License](https://img.shields.io/badge/License-Proprietary-red)

**Sovereign-grade global security benchmarking platform for deterministic scoring, risk-adjusted ranking, and live comparative security intelligence across nations.**

---

## 🌍 Overview

QSSI™ (Quantum Sovereign Security Index System) is a structured national-security benchmarking platform designed to compute, rank, and visualize sovereign security performance across countries using a reproducible, weighted, multi-dimensional index model.

It combines:

- deterministic scoring
- risk-adjusted ranking
- uncertainty-aware interpretation
- API-delivered outputs
- live dashboard access
- versioned methodological discipline

QSSI™ is intended as a research-grade and platform-grade framework for:

- comparative sovereign security analysis
- structured resilience benchmarking
- policy-oriented strategic interpretation
- reproducible national score generation
- extensible audit and certification-oriented system design

---

## 🚀 Live Access

**API Base:**  
https://qvp-global-system-production.up.railway.app/

**Dashboard:**  
https://qvp-global-system-production.up.railway.app/dashboard

**Rankings (JSON):**  
https://qvp-global-system-production.up.railway.app/rankings

---

## ⭐ Why This Repository Matters

This repository provides a public, versioned, computational reference for a sovereign-grade security scoring system that is:

- **deterministic** — fixed inputs produce reproducible outputs
- **structured** — scoring is defined over explicit weighted dimensions
- **risk-aware** — final scores are adjusted by modeled risk exposure
- **machine-consumable** — rankings are exposed via live API endpoints
- **platform-ready** — the system is deployable as a service, not only a paper framework
- **audit-oriented** — integrity signaling and version discipline are part of the design logic

For reviewers, institutions, developers, and researchers, the value of QSSI™ is that it is not presented only as a conceptual doctrine — it is presented as a computationally framed, operationally deployable benchmark system.

---

## ⚙️ Methodology at a Glance

QSSI™ uses four normalized scoring dimensions:

- **PQC** — post-quantum readiness
- **AI** — AI defense and cyber capability
- **LEGAL** — legal and regulatory preparedness
- **RES** — systemic resilience capacity

### Canonical Inputs

- `M = (PQC, AI, LEGAL, RES)`, each in `[0,1]`
- `w = (0.30, 0.25, 0.25, 0.20)`, `sum(w) = 1`
- `Risk ∈ [0,1]`

### Core Score

    QSSI = sum(w_i * M_i)
    QSSI_scaled = 100 * QSSI
    QSSI_adj = QSSI_scaled * (1 - Risk)

### Uncertainty Layer

    epsilon = sqrt(sum((w_i^2) * (sigma_i^2))) * 100
    QSSI_final = QSSI_adj ± epsilon

### Ranking Rule

    Score_i = QSSI_adj_i - epsilon
    Rank = descending sort by Score_i

### Tier Model

- **Tier A** — `QSSI_adj >= 85`
- **Tier B** — `75 <= QSSI_adj < 85`
- **Tier C** — `50 <= QSSI_adj < 75`
- **Tier D** — `QSSI_adj < 50`

> The README intentionally presents an executive mathematical summary.  
> Detailed methodology, formal structure, and supporting technical materials should remain in the repository documentation and source files.

---

## 📡 Public API Surface

### Current Public Endpoints

| Endpoint | Type | Description |
|---|---|---|
| `/` | Service Root | Base service entry point |
| `/rankings` | Data API | Live QSSI rankings in JSON format |
| `/dashboard` | UI Layer | Interactive dashboard interface |

### Example Request

    curl https://qvp-global-system-production.up.railway.app/rankings

> Future releases may expose additional versioned service endpoints such as `/health`, `/version`, `/audit/hash`, `/docs`, or `/openapi.json` depending on deployment evolution.

---

## 🧠 Computational Reference (Python)

    import pandas as pd
    import numpy as np
    import hashlib
    from scipy.stats import norm

    WEIGHTS = np.array([0.30, 0.25, 0.25, 0.20])
    SIGMA = np.array([0.05, 0.06, 0.04, 0.05])

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
        raw = f"{df.to_csv(index=False)}_{WEIGHTS}_2026.1.0-A".encode()
        return hashlib.sha3_256(raw).hexdigest()

---

## 🏗️ Repository Structure

    QVP-Global-System/
    ├── api/                # API layer and service interfaces
    ├── dataset/            # Source data and structured scoring inputs
    ├── docs/               # Documentation, methodology, and support materials
    ├── engine/             # Core scoring and ranking computation logic
    ├── reports/            # Output artifacts, rankings, and report materials
    ├── .gitignore
    ├── DATA_SOURCES.md
    ├── PROPRIETARY_LICENSE.md
    ├── README.md
    └── requirements.txt

> This structure is aligned to the current public repository layout.

---

## 🧱 Formal System Definition

QSSI™ can be expressed as a deterministic sovereign scoring function:

    F : (M, Risk, sigma) -> (QSSI_adj, epsilon, Rank, Cert)

Where:

- `M ∈ [0,1]^4`
- `Risk ∈ [0,1]`
- `sigma ∈ R_+^4`

Domain and range framing:

- **Input Domain (D)** = normalized sovereign capability vector + risk + uncertainty parameters
- **Output Range (R)** = adjusted score + uncertainty band + rank + certification state

Core properties:

- **Closure** — all valid inputs produce bounded valid outputs
- **Determinism** — fixed inputs under fixed version produce fixed outputs
- **Continuity** — the scoring function is continuous over its bounded input domain
- **Boundedness** — adjusted scores remain in `[0,100]`
- **Reproducibility** — fixed dataset + fixed weights + fixed version => same result

---

## 🏛️ System Architecture

The platform is structured as a deployable sovereign intelligence system rather than only a static scoring paper.

### Canonical Architecture

    UI Layer -> API Layer -> Compute Engine -> Dataset Layer -> Validation Logic -> Output / Ranking Surface

### Operational Interpretation

- **Frontend / Dashboard Layer** — renders live comparative sovereign rankings
- **API Layer** — exposes machine-readable ranking outputs
- **Engine Layer** — executes weighted scoring and deterministic rank generation
- **Dataset Layer** — stores normalized sovereign scoring inputs
- **Validation Layer** — supports consistency and version-bound reproducibility
- **Output Layer** — rankings, reports, and publication-ready artifacts

### Platform Characteristics

- stateless deployment model
- cloud-hosted service exposure
- deterministic compute pathway
- version-disciplined methodology
- public-facing ranking endpoint
- dashboard-accessible output layer

---

## 🔐 Integrity, Reproducibility & Version Discipline

QSSI™ is designed around **methodological stability**.

### Release Discipline

- **Current Version:** `2026.1.0-A`
- **State:** `IMMUTABLE`
- **Rule:** Any substantive methodological or computational change requires a **version increment**

### Integrity Logic

    Hash = SHA3-256(Input)
    System_ID = SHA3-256(System || Version || Timestamp)

Interpretive principles:

- **Integrity** ⇔ hash-consistent content
- **Authenticity** ⇔ version-bound deterministic identity
- **Tamper Signal** ⇔ hash mismatch or undocumented methodological divergence

### Reproducibility Condition

A result is considered reproducible when:

- the dataset is fixed
- the weighting vector is fixed
- the model logic is fixed
- the release version is fixed

---

## 📂 Data & Documentation Files

This repository already includes critical institutional files:

- `DATA_SOURCES.md` — source provenance and data origin discipline
- `PROPRIETARY_LICENSE.md` — governing proprietary usage restrictions
- `README.md` — public-facing institutional repository overview
- `docs/` — methodology, explanatory, and support documentation
- `reports/` — generated outputs and publication artifacts

> For institutional credibility, the repository should preserve consistency between the README, the data source file, the codebase, and any published DOI record.

---

## 🧪 Local Installation (Reference)

### 1) Clone the repository

    git clone https://github.com/BidyutMazumdar/QVP-Global-System.git
    cd QVP-Global-System

### 2) Create virtual environment (recommended)

    python -m venv .venv

Windows:

    .venv\Scripts\activate

Linux / macOS:

    source .venv/bin/activate

### 3) Install dependencies

    pip install -r requirements.txt

### 4) Run the platform (adjust to actual entrypoint if needed)

    python api/app.py

> If your actual API entrypoint differs (for example `main.py`, `server.py`, `run.py`, or FastAPI/Uvicorn boot commands), keep this README aligned to the real implementation.

---

## 📊 Intended Use Cases

QSSI™ may be used as a structured framework for:

- sovereign digital security benchmarking
- comparative resilience assessment
- policy-grade exploratory analysis
- ranking demonstrations and live API visualization
- educational and methodological presentation
- platform architecture demonstration for public research communication

> This repository does **not** claim to replace classified national security systems, sovereign intelligence agencies, or formal state defense apparatus. It is a structured benchmarking and analytical platform.

---

## 🧾 Canonical DOI Record

**DOI:**  
https://doi.org/10.5281/zenodo.19375967

**Recommended canonical citation record:**  
Bidyut, M. (2026). *Quantum Veil Protocol (QVP) — Global System 2026: Sovereign Digital Security Index (QSSI), Methodology, Mathematical Architecture, and Platform Framework (2026.1.0).* Zenodo. https://doi.org/10.5281/zenodo.19375967

---

## 🆔 ORCID

**ORCID:**  
https://orcid.org/0009-0007-5615-3558

---

## 📚 Citation

If referencing this repository in academic, institutional, policy, or technical contexts, use the Zenodo DOI record as the **canonical scholarly citation**.

Suggested format:

    Bidyut, M. (2026). Quantum Veil Protocol (QVP) — Global System 2026: Sovereign Digital Security Index (QSSI), Methodology, Mathematical Architecture, and Platform Framework (Version 2026.1.0). Zenodo. https://doi.org/10.5281/zenodo.19375967

---

## 👤 Author

**Dr. B. Mazumdar, D.Sc. (Hon.), D.Litt. (Hon.)**  
Architect of Modern Statehood  
Founder & Principal Architect, FAIR+D Canon™

---

## 📜 License

This repository is governed by a **proprietary license**.

See:

- `PROPRIETARY_LICENSE.md`

### High-Level License Summary

- All rights reserved unless explicitly granted
- No unauthorized commercial reuse
- No derivative republication without permission
- No institutional repackaging without express authorization
- Attribution alone does **not** create usage rights

> Always rely on the full text of `PROPRIETARY_LICENSE.md` as the controlling legal instrument.

---

## ⚠️ Institutional Notice

QSSI™, Quantum Sovereign Security Index System, and related doctrinal expressions are presented as part of a proprietary sovereign systems architecture and computational governance framework.

All naming, framework architecture, documentation structure, and release discipline should remain internally consistent across:

- repository contents
- DOI deposits
- documentation files
- reports
- public deployment surfaces

---

## 🌐 Repository

**GitHub Repository:**  
https://github.com/BidyutMazumdar/QVP-Global-System

---

## ✅ Status

**Current Release State:** `PUBLIC / LIVE / VERSIONED / DEPLOYED`

- Public repository active
- Live API reachable
- Dashboard published
- DOI minted
- Version fixed
- Documentation active

---

© 2026 Dr. B. Mazumdar. All Rights Reserved.
