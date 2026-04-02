# QSSI™ — Quantum Sovereign Security Index System

![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19375967-blue)
![Canonical Release](https://img.shields.io/badge/Canonical%20Release-2026.1.0--A-black)
![Live Build](https://img.shields.io/badge/Live%20Build-v2026.1.1-success)
![API](https://img.shields.io/badge/API-Live-success)
![Dashboard](https://img.shields.io/badge/Dashboard-Live-success)
![License](https://img.shields.io/badge/License-Proprietary-red)

**Sovereign-grade global security benchmarking platform for deterministic scoring, risk-adjusted ranking, and live comparative security intelligence across nations.**

---

## 🌍 Overview

**QSSI™ (Quantum Sovereign Security Index System)** is a structured sovereign security benchmarking platform for computing, ranking, and visualizing national security readiness through a reproducible, weighted, multi-dimensional index model.

It is designed as a **research-grade and platform-grade** framework for:

- deterministic sovereign scoring
- risk-adjusted comparative ranking
- uncertainty-aware interpretation
- API-delivered machine-readable outputs
- live dashboard-based public intelligence visualization
- version-disciplined methodological reproducibility

---

## 🚀 Live Access

- **API Base:** `https://qvp-global-system-production.up.railway.app/`
- **Dashboard:** `https://qvp-global-system-production.up.railway.app/dashboard`
- **Rankings (JSON):** `https://qvp-global-system-production.up.railway.app/rankings`

---

## ⭐ Why This Repository Matters

QSSI™ is presented not merely as a conceptual doctrine, but as a **deployable computational system**.

It provides a public, versioned reference architecture that is:

- **deterministic** — fixed inputs yield reproducible outputs
- **structured** — explicit weighted dimensions govern scoring
- **risk-aware** — adjusted outputs reflect modeled exposure
- **machine-consumable** — rankings are exposed via live API
- **platform-ready** — operational as a service, not only a paper model
- **audit-oriented** — version and integrity discipline are built into the framework

---

## ⚙️ Methodology at a Glance

QSSI™ uses four normalized dimensions:

- **PQC** — post-quantum readiness
- **AI** — AI defense and cyber capability
- **LEGAL** — legal and regulatory preparedness
- **RES** — systemic resilience capacity

### Canonical Inputs

- `M = (PQC, AI, LEGAL, RES)`, each in `[0,1]`
- `w = (0.30, 0.25, 0.25, 0.20)`, where `sum(w) = 1`
- `Risk ∈ [0,1]`

### Core Scoring Logic

```text
QSSI = sum(w_i * M_i)
QSSI_scaled = 100 * QSSI
QSSI_adj = QSSI_scaled * (1 - Risk)
epsilon = sqrt(sum((w_i^2) * (sigma_i^2))) * 100
Score_i = QSSI_adj_i - epsilon
```

### Tier Model

- **Tier A** — `QSSI_adj >= 85`
- **Tier B** — `75 <= QSSI_adj < 85`
- **Tier C** — `50 <= QSSI_adj < 75`
- **Tier D** — `QSSI_adj < 50`

> The README provides an executive mathematical summary only. Detailed methodology should remain in repository documentation and source files.

---

## 📡 Public API Surface

| Endpoint | Type | Description |
|---|---|---|
| `/` | Service Root | Base service entry point |
| `/rankings` | Data API | Live QSSI rankings (JSON) |
| `/dashboard` | UI Layer | Interactive dashboard interface |

### Example Request

```bash
curl https://qvp-global-system-production.up.railway.app/rankings
```

---

## 🧠 Computational Reference (Python)

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

## 🏗️ Repository Structure

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

## 🧱 Formal System Definition

QSSI™ may be represented as:

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

## 🏛️ Architecture

```text
UI Layer -> API Layer -> Compute Engine -> Dataset Layer -> Validation Logic -> Output Surface
```

Operationally, QSSI™ is structured as a **deployable sovereign intelligence platform** with:

- dashboard interface
- machine-readable API outputs
- deterministic scoring engine
- structured dataset layer
- reproducibility-aware validation logic

---

## 🔐 Integrity & Version Discipline

### Version Declaration

- **Canonical Scholarly Release (DOI):** `2026.1.0-A`
- **Current Live Deployment Build:** `v2026.1.1`
- **Canonical State:** `IMMUTABLE`

### Governance Rule

- substantive methodological or computational changes require a **canonical version increment**
- non-substantive UI, deployment, or infrastructure changes may increment the **live build** without altering the DOI-bound canonical release

### Integrity Logic

```text
Hash = SHA3-256(Input)
System_ID = SHA3-256(System || Canonical_Release || Timestamp)
```

---

## 📂 Core Documentation

- `README.md` — institutional public overview
- `DATA_SOURCES.md` — source provenance discipline
- `PROPRIETARY_LICENSE.md` — governing legal instrument
- `docs/` — methodology and technical support materials
- `reports/` — generated outputs and publication artifacts

---

## 🧪 Local Installation

```bash
git clone https://github.com/BidyutMazumdar/QVP-Global-System.git
cd QVP-Global-System
python -m venv .venv
```

Activate environment:

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the platform (adjust if your real entrypoint differs):

```bash
python api/app.py
```

---

## 📊 Intended Use

QSSI™ may be used for:

- sovereign digital security benchmarking
- comparative resilience analysis
- policy-grade exploratory evaluation
- live ranking demonstrations
- research and methodological presentation
- public platform architecture showcase

> QSSI™ is a structured benchmarking and analytical platform. It does **not** claim to replace classified state systems, intelligence agencies, or sovereign defense apparatus.

---

## 🧾 Canonical DOI Record

- **DOI:** `https://doi.org/10.5281/zenodo.19375967`
- **ORCID:** `https://orcid.org/0009-0007-5615-3558`

### Canonical Citation

```text
Bidyut, M. (2026). Quantum Veil Protocol (QVP) — Global System 2026: Sovereign Digital Security Index (QSSI), Methodology, Mathematical Architecture, and Platform Framework (Version 2026.1.0-A). Zenodo. https://doi.org/10.5281/zenodo.19375967
```

> For operational references, the live deployment build may additionally be noted as `v2026.1.1`.

---

## 👤 Author

**Dr. B. Mazumdar, D.Sc. (Hon.), D.Litt. (Hon.)**  
Architect of Modern Statehood  
Founder & Principal Architect, FAIR+D Canon™

---

## 📜 License

This repository is governed by a **proprietary license**.

- See: `PROPRIETARY_LICENSE.md`

**High-level summary:**

- all rights reserved unless expressly granted
- no unauthorized commercial reuse
- no derivative republication without permission
- no institutional repackaging without express authorization

> Attribution alone does **not** create usage rights.

---

## ⚠️ Institutional Notice

QSSI™, Quantum Sovereign Security Index System, and related doctrinal expressions are presented as part of a proprietary sovereign systems architecture and computational governance framework.

Consistency should be maintained across:

- repository contents
- DOI deposits
- documentation files
- reports
- public deployment surfaces
- canonical scholarly release declarations
- live deployment build declarations

---

## 🌐 Repository

**GitHub:** `https://github.com/BidyutMazumdar/QVP-Global-System`

---

## ✅ Status

**Current State:** `PUBLIC / LIVE / VERSIONED / DEPLOYED`

- Canonical DOI release: `2026.1.0-A`
- Current live deployment build: `v2026.1.1`
- Repository active
- API reachable
- Dashboard published
- DOI minted
- Documentation active

---

© 2026 Dr. B. Mazumdar. All Rights Reserved.
