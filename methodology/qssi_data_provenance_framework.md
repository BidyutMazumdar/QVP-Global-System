# DATA_SOURCES.md

# QSSI™ — DATA SOURCES & PROVENANCE FRAMEWORK
## Quantum Sovereign Security Index System (QSSI™)
### FAIR+D Canon™ Sovereign Intelligence Architecture

---

# OVERVIEW

This document defines the official data provenance, methodological sourcing architecture, normalization framework, integration logic, integrity discipline, and reproducibility standards for the QSSI™ (Quantum Sovereign Security Index System).

QSSI™ is a deterministic, reproducible, sovereign-grade computational benchmarking framework designed to evaluate national security readiness, cyber capability, AI governance maturity, legal-institutional resilience, and macro-systemic stability through structured multi-source integration.

The framework combines internationally recognized datasets, institutional indicators, bounded normalization logic, probabilistic uncertainty estimation, and cryptographic integrity verification into a unified analytical architecture.

QSSI™ is designed as a computational governance system rather than a conventional static index.

---

# STRATEGIC OBJECTIVES

The QSSI™ framework is designed to support:

- sovereign cyber readiness benchmarking
- AI governance capability assessment
- institutional resilience evaluation
- systemic macroeconomic stability analysis
- strategic governance simulation
- comparative sovereign modeling
- computational policy research
- deterministic analytical reproducibility

---

# FOUNDATIONAL DESIGN PRINCIPLES

The QSSI™ architecture follows six foundational principles:

| Principle | Description |
|---|---|
| Determinism | Identical inputs produce identical outputs |
| Transparency | All data sources and transformations remain publicly declared |
| Reproducibility | Outputs remain version-bound and computationally reproducible |
| Auditability | Inputs, transformations, and outputs remain traceable |
| Cross-Domain Integration | Sovereign capability modeled across multiple institutional domains |
| Institutional Neutrality | No geopolitical weighting or ideological preference applied |

---

# SYSTEM ARCHITECTURE

QSSI™ integrates four major sovereign capability layers:

| Layer | Domain | Purpose |
|---|---|---|
| PQC | Post-Quantum & Cybersecurity Readiness | Cyber defense capability |
| AI | Artificial Intelligence Governance | AI strategic readiness |
| LEGAL | Institutional & Regulatory Integrity | Governance and rule-of-law resilience |
| RES | Economic & Systemic Resilience | Macroeconomic and structural stability |

---

# DATA DIRECTORY STRUCTURE

```text
/data/
├── PQC_NCSI_2026.csv
├── AI_OECD_2026.csv
├── AI_OXFORD_2026.csv
├── wjp_clean.csv
├── RES_IMF_2026.csv
├── RES_NDGAIN_2026_FINAL.csv
├── RES_GLOBAL_RESILIENCE_INDEX_v1.0_STRICT.csv
└── QSSI_RESILIENCE_INSTITUTIONAL_2026_FAIRD_CANON_v2026.1.0.csv
```

---

# DATA GOVERNANCE MODEL

The QSSI™ data governance model enforces:

- source traceability
- deterministic transformation
- bounded normalization
- integrity preservation
- reproducible computation
- version discipline
- institutional transparency

Every dataset integrated into QSSI™ must satisfy:

1. identifiable provenance
2. institutional credibility
3. public accessibility
4. stable schema structure
5. reproducible transformation capability

---

# PQC LAYER — POST-QUANTUM & CYBERSECURITY READINESS

## Primary Dataset

### National Cyber Security Index (NCSI)

| Attribute | Description |
|---|---|
| File | PQC_NCSI_2026.csv |
| Source | National Cyber Security Index |
| Domain | National cybersecurity capability |
| Coverage | Multi-country sovereign benchmarking |
| Type | Composite cybersecurity readiness dataset |

---

## Functional Role

The PQC layer functions as a bounded proxy representation of:

- sovereign cybersecurity maturity
- cyber defense coordination
- digital infrastructure preparedness
- national incident response capability
- operational cyber governance
- post-quantum transition preparedness proxy

---

## Methodological Justification

Direct internationally standardized datasets for sovereign post-quantum readiness remain limited.

Therefore, QSSI™ employs structured cybersecurity maturity indicators as bounded proxy variables for sovereign PQC preparedness estimation.

This proxy-based approach preserves:

- international comparability
- reproducibility
- deterministic integration
- cross-country scalability

---

# AI LAYER — ARTIFICIAL INTELLIGENCE GOVERNANCE

## OECD AI Policy Observatory

| Attribute | Description |
|---|---|
| File | AI_OECD_2026.csv |
| Source | OECD AI Policy Observatory |
| Domain | AI governance and policy readiness |
| Coverage | International AI policy benchmarking |

---

## Coverage Includes

- AI policy maturity
- institutional AI coordination
- ethical AI governance
- public-sector AI strategy
- AI regulatory preparedness
- national AI deployment frameworks

---

## Oxford Government AI Readiness Index

| Attribute | Description |
|---|---|
| File | AI_OXFORD_2026.csv |
| Source | Oxford Insights |
| Domain | Government AI readiness |
| Coverage | Sovereign AI institutional readiness |

---

## Coverage Includes

- digital governance maturity
- public-sector AI deployment readiness
- infrastructure preparedness
- data governance capability
- AI operational capacity
- institutional implementation readiness

---

# LEGAL LAYER — RULE OF LAW & INSTITUTIONAL QUALITY

## World Justice Project (WJP)

| Attribute | Description |
|---|---|
| File | wjp_clean.csv |
| Source | World Justice Project |
| Domain | Rule of law and institutional integrity |
| Coverage | Cross-national institutional benchmarking |

---

## Coverage Includes

- judicial effectiveness
- regulatory enforcement
- corruption constraints
- institutional accountability
- legal system reliability
- governance stability
- procedural transparency

---

## Functional Role

The LEGAL layer evaluates institutional reliability and governance resilience through structured rule-of-law indicators.

The layer acts as a stabilizing governance dimension within the broader sovereign security architecture.

---

# RES LAYER — SYSTEMIC RESILIENCE

The RES layer integrates multiple macroeconomic, structural, and resilience-oriented datasets.

This layer evaluates sovereign stability under conditions of institutional, economic, infrastructural, and systemic stress.

---

# IMF WORLD ECONOMIC OUTLOOK (WEO)

| Attribute | Description |
|---|---|
| File | RES_IMF_2026.csv |
| Source | International Monetary Fund (IMF) |
| Domain | Macroeconomic resilience |
| Coverage | Global macroeconomic indicators |

---

# INTEGRATED IMF INDICATORS

| Indicator | Functional Purpose |
|---|---|
| GDP (Current Prices) | Economic scale |
| GDP Per Capita | Economic capacity |
| Unemployment Rate | Labor market stress |
| Inflation | Monetary stability |
| Current Account Balance | External resilience |

---

# INSTITUTIONAL PIPELINE OUTPUT

```text
QSSI_RESILIENCE_INSTITUTIONAL_2026_FAIRD_CANON_v2026.1.0.csv
```

---

# IMF PIPELINE METHODOLOGY

Indicators are:

- normalized to bounded scale
- reverse-normalized where appropriate
- weighted deterministically
- aggregated reproducibly
- hash-verified for integrity

Negative indicators include:

- unemployment
- inflation
- instability-sensitive variables

---

# ND-GAIN RESILIENCE DATASET

| Attribute | Description |
|---|---|
| File | RES_NDGAIN_2026_FINAL.csv |
| Source | Notre Dame Global Adaptation Initiative |
| Domain | Climate and structural resilience |

---

# COVERAGE INCLUDES

- adaptive capacity
- infrastructure resilience
- climate vulnerability
- institutional preparedness
- long-term sustainability
- systemic adaptation capability

---

# GLOBAL RESILIENCE INDEX

| Attribute | Description |
|---|---|
| File | RES_GLOBAL_RESILIENCE_INDEX_v1.0_STRICT.csv |
| Domain | Composite sovereign resilience |

---

# FUNCTIONAL PURPOSE

Provides systemic robustness calibration across:

- governance continuity
- institutional adaptability
- infrastructure stability
- macroeconomic resilience
- long-term systemic survivability

---

# DATA NORMALIZATION FRAMEWORK

QSSI™ employs bounded min-max normalization.

Canonical transformation:

```math
M_i = \frac{X_i - X_{min}}{X_{max} - X_{min}}
```

Where:

- \( M_i \in [0,1] \)
- \( X_i \) = raw observed value
- \( X_{min} \) = minimum observed value
- \( X_{max} \) = maximum observed value

---

# REVERSE NORMALIZATION

Negative indicators are reverse-normalized.

Examples include:

- unemployment
- inflation
- instability indicators
- stress-sensitive macroeconomic variables

Canonical reverse transformation:

```math
M_i^{rev} = 1 - M_i
```

---

# WEIGHTING FRAMEWORK

Canonical QSSI™ layer weights:

| Layer | Weight |
|---|---|
| PQC | 0.30 |
| AI | 0.25 |
| LEGAL | 0.25 |
| RES | 0.20 |

Constraint:

```math
\sum w_i = 1
```

---

# CORE COMPUTATIONAL MODEL

Canonical QSSI™ formulation:

```math
QSSI = \sum (w_i \cdot M_i)
```

Scaled score:

```math
QSSI_{scaled} = 100 \times QSSI
```

---

# RISK-ADJUSTED FRAMEWORK

Risk-adjusted sovereign score:

```math
QSSI_{adj} = QSSI_{scaled} \times (1 - Risk)
```

Where:

- \( Risk \in [0,1] \)

Purpose:

- systemic vulnerability adjustment
- sovereign instability correction
- stress-aware scoring

---

# UNCERTAINTY MODEL

Uncertainty estimation:

```math
\varepsilon = \sqrt{\sum (w_i^2 \cdot \sigma_i^2)} \times 100
```

Purpose:

- bounded probabilistic confidence
- ranking robustness estimation
- deterministic consistency checks
- comparative stability analysis

---

# FORMAL SYSTEM DEFINITION

Canonical system representation:

```math
F : (M, Risk, \sigma) \rightarrow (QSSI_{adj}, \varepsilon, Rank, Cert)
```

Outputs include:

- adjusted sovereign score
- uncertainty bound
- ranking position
- probabilistic validity state

---

# DATA INTEGRITY FRAMEWORK

QSSI™ incorporates cryptographic integrity verification.

---

# DATASET HASH

```math
SHA3\text{-}256(Dataset)
```

---

# SYSTEM HASH

```math
SHA3\text{-}256(System \parallel Version \parallel Timestamp)
```

---

# INTEGRITY OBJECTIVES

- tamper detection
- reproducibility assurance
- audit verification
- canonical consistency
- version authentication

---

# REPRODUCIBILITY PRINCIPLES

QSSI™ outputs remain reproducible under:

- fixed datasets
- declared canonical versions
- deterministic execution logic
- fixed weight vectors
- version-controlled source files
- stable normalization procedures

---

# VALIDATION CHARACTERISTICS

The framework incorporates:

- bounded metric constraints
- deterministic ranking logic
- normalized comparability
- uncertainty estimation
- integrity verification
- cross-layer consistency checks

---

# LIMITATIONS

The framework contains several limitations:

- reliance on proxy indicators
- non-causal modeling assumptions
- public-domain data dependency
- cross-country comparability assumptions
- source revision sensitivity
- incomplete representation of classified capabilities

QSSI™ is intended strictly for:

- analytical benchmarking
- governance research
- sovereign capability comparison
- strategic modeling
- simulation-oriented analysis

It is not intended as classified intelligence assessment.

---

# VERSION DISCIPLINE

| Component | Version |
|---|---|
| Canonical Release | v2026.1.0 |
| Live Build | v2026.1.1 |
| Dataset Layer | 2026 Stable |
| Integrity Status | Hash-Verified |

---

# REPOSITORY

GitHub Repository:

```text
https://github.com/BidyutMazumdar/QVP-Global-System
```

---

# DOI

```text
https://doi.org/10.5281/zenodo.19375967
```

---

# AUTHOR

Dr. B. Mazumdar  
Independent Researcher  
Founder — FAIR+D Canon™

ORCID:

```text
https://orcid.org/0009-0007-5615-3558
```

---

# LICENSE

Creative Commons Attribution–NonCommercial–NoDerivatives 4.0 International (CC BY-NC-ND 4.0)

```text
https://creativecommons.org/licenses/by-nc-nd/4.0/
```

---

# STATUS

PUBLIC / VERSIONED / REPRODUCIBLE / AUDITABLE / INSTITUTIONAL

---

# FINAL POSITIONING

QSSI™ represents a deterministic, reproducible, sovereign-grade computational benchmarking architecture integrating cybersecurity readiness, AI governance maturity, institutional integrity, and macro-systemic resilience into a unified analytical framework suitable for comparative governance analysis, strategic simulation, and computational policy research.

---
