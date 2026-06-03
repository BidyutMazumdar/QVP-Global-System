DATA_PIPELINE.md

QSSI 2026 Computational Data Pipeline

FAIR+D Canon™ Global Framework

---

Purpose

This document defines the official computational workflow used to generate QSSI 2026.

---

Pipeline Overview

Source Data

↓

Data Harmonization

↓

Country Matching

↓

Data Validation

↓

Normalization

↓

Indicator Construction

↓

PCA Analysis

↓

Weight Extraction

↓

QSSI Computation

↓

Ranking Generation

↓

Tier Classification

↓

Statistical Validation

↓

Final Publication

---

Stage 1 — Source Data Acquisition

Datasets:

- AI_INDEX_2026_v1_MC_Canon.csv
- LEGAL_WGI_2026_v1_MC_Canon.csv
- RES_INDEX_2026_MC_Canon.csv
- PQC_NCSI_2026_MC_Canon.csv

---

Stage 2 — Data Harmonization

Procedures:

- country-name standardization
- duplicate removal
- schema verification
- variable alignment

---

Stage 3 — Coverage Filtering

Eligibility Criteria:

Country must possess:

- AI_INDEX
- LEGAL_WGI_SCORE
- RES_INDEX
- PQC

Coverage:

87 countries

Coverage Rate:

40.85%

---

Stage 4 — Normalization

Method:

Min-Max Scaling

Formula:

x' = (x − min(x)) / (max(x) − min(x))

Range:

0–1

---

Stage 5 — Indicator Construction

AI_INDEX

LEGAL_WGI_SCORE

RES_INDEX

PQC

---

Stage 6 — Principal Component Analysis

Input Variables:

- AI_INDEX
- LEGAL_WGI_SCORE
- RES_INDEX
- PQC

Explained Variance:

PC1 = 77.93%

PC2 = 14.22%

PC3 = 4.12%

PC4 = 3.73%

---

Stage 7 — Weight Extraction

Official Weights:

AI_INDEX = 0.287931

LEGAL_WGI_SCORE = 0.275993

RES_INDEX = 0.152758

PQC = 0.283319

---

Stage 8 — QSSI Computation

QSSI =
(0.287931 × AI_INDEX)
+
(0.275993 × LEGAL_WGI_SCORE)
+
(0.152758 × RES_INDEX)
+
(0.283319 × PQC)

---

Stage 9 — Ranking

Countries ranked in descending order of QSSI score.

---

Stage 10 — Tier Classification

Tier I — Quantum Sovereignty Leaders

Tier II — Advanced Sovereignty States

Tier III — Emerging Strategic Powers

Tier IV — Developing Sovereignty Systems

Tier V — Capacity-Constrained States

---

Stage 11 — Statistical Validation

Correlation Analysis

PCA Diagnostics

Spearman Robustness

Descriptive Statistics

---

Output Products

- QSSI Ranking
- Country Profiles
- Regional Analysis
- Tier Analysis
- Statistical Report

---

Status:
Official Computational Pipeline

DOI:
10.5281/zenodo.20385492
