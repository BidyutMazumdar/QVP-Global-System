DATA_PIPELINE.md

Quantum-Veil Sovereignty Security Index (QSSI) 2026

FAIR+D Canon™ Global Framework

Computational Data Pipeline

---

Current Definitive Edition DOI

10.5281/zenodo.20385492

Canonical DOI (All Versions)

10.5281/zenodo.17302169

Author

Dr. B. Mazumdar

ORCID

https://orcid.org/0009-0007-5615-3558

---

Overview

This document describes the complete computational workflow underlying the Quantum-Veil Sovereignty Security Index (QSSI) 2026 Definitive World Edition.

The pipeline integrates heterogeneous international datasets through deterministic preprocessing, sovereign-country harmonization, statistical validation, dimensionality assessment, weighting derivation, robustness evaluation, ranking generation, integrity verification, and reproducible archival publication.

All procedures are fully deterministic and designed to support transparency, auditability, reproducibility, and long-term preservation.

---

Pipeline Architecture

Source Datasets
       │
       ▼
Data Validation
       │
       ▼
Country Harmonization
       │
       ▼
Coverage Verification
       │
       ▼
Complete-Case Validation
       │
       ▼
Min-Max Normalization
       │
       ▼
Descriptive Statistics
       │
       ▼
Correlation Analysis
       │
       ▼
Distribution Diagnostics
       │
       ▼
KMO Assessment
       │
       ▼
Bartlett's Test
       │
       ▼
Reliability Diagnostics
       │
       ▼
Principal Component Analysis
       │
       ▼
Weight Derivation
       │
       ▼
QSSI Score Construction
       │
       ▼
Ranking Generation
       │
       ▼
Robustness Benchmarking
       │
       ▼
Integrity Verification
       │
       ▼
Audit Artifact Generation
       │
       ▼
Archival Publication

---

Stage 1 — Source Dataset Acquisition

Canonical Input Datasets

Dimension| Dataset| Coverage
Artificial Intelligence Capability| AI_INDEX_2026| 195
Governance and Legal Quality| LEGAL_WGI_2026| 213
National Resilience Capacity| RES_INDEX_2026| 181
Post-Quantum Cybersecurity Readiness| PQC_NCSI_2026| 124

---

Stage 2 — Country Harmonization

Country names are standardized using deterministic sovereign-name harmonization procedures.

Validation operations include:

- Country normalization
- Canonical naming
- Duplicate detection
- Sovereign matching
- Merge validation
- Coverage verification

Output:

Country Harmonization Status = PASSED

---

Stage 3 — Coverage Verification

Cross-Domain Coverage Matrix

Dataset| AI| LEGAL| RES| PQC
AI| 195| 172| 128| 118
LEGAL| 172| 213| 136| 117
RES| 128| 136| 181| 94
PQC| 118| 117| 94| 124

---

Stage 4 — Final Analytical Universe Construction

Countries possessing complete observations across all four constituent dimensions are retained within the final analytical universe.

Final Universe

Metric| Value
Countries Included| 90
Countries Excluded| 36
Final Analytical Sample| 90
Missing Values| 0

Dataset Shape:

(90, 5)

Variables:

country
AI_INDEX
LEGAL_WGI_SCORE
RES_INDEX
PQC

---

Stage 5 — Data Normalization

All constituent variables are transformed to a common scale using Min-Max normalization.

Normalization Formula:

X_norm = (X - X_min) / (X_max - X_min)

Resulting scale:

0 ≤ X ≤ 1

---

Stage 6 — Descriptive Statistical Analysis

For each variable the pipeline computes:

- Count
- Mean
- Standard Deviation
- Minimum
- First Quartile
- Median
- Third Quartile
- Maximum

Variables analyzed:

- AI_INDEX
- LEGAL_WGI_SCORE
- RES_INDEX
- PQC

---

Stage 7 — Correlation Analysis

Pairwise Pearson correlation coefficients are calculated across all constituent dimensions.

Purpose:

- Dependency assessment
- Structural consistency validation
- Multivariate suitability evaluation

Output:

Correlation Matrix

---

Stage 8 — Distribution Diagnostics

For every constituent dimension the following diagnostics are calculated:

- Skewness
- Kurtosis

Purpose:

- Distribution assessment
- Shape diagnostics
- Outlier sensitivity evaluation

---

Stage 9 — Sampling Adequacy Assessment

Kaiser-Meyer-Olkin Test

Result:

KMO = 0.7355868518654463

Interpretation:

Good Sampling Adequacy

---

Stage 10 — Correlation Structure Validation

Bartlett's Test of Sphericity

Result:

Chi-Square = 249.83379389196242
P-Value    = 4.450885068086372e-51

Interpretation:

Highly Significant Correlation Structure

---

Stage 11 — Reliability Diagnostics

Cronbach's Alpha

Result:

Alpha = 0.8785685555594794

95% Confidence Interval:

[0.832, 0.915]

Interpretation:

Excellent Internal Consistency

---

Stage 12 — Principal Component Analysis

Principal Component Analysis is applied to identify the dominant latent structure underlying sovereign capability dimensions.

Eigenvalues

[0.74561879, 0.17028181, 0.04806765, 0.03603175]

Eigenvalue Sum:

1.000000

---

Stage 13 — PCA Loading Estimation

Variable| PC1| PC2| PC3| PC4
AI_INDEX| 0.534197| -0.272778| -0.351497| 0.718802
LEGAL_WGI_SCORE| 0.536276| 0.105185| 0.835959| 0.050156
RES_INDEX| 0.416053| 0.816887| -0.359197| -0.174850
PQC| 0.503926| -0.497216| -0.220453| -0.670996

---

Stage 14 — Weight Derivation

PCA-Derived Canonical Weights

Variable| Weight
AI_INDEX| 0.26837950
LEGAL_WGI_SCORE| 0.26942446
RES_INDEX| 0.20902441
PQC| 0.25317163

Weight Sum:

1.000000

---

Stage 15 — QSSI Score Construction

QSSI scores are generated through weighted aggregation of normalized dimensions using PCA-derived canonical weights.

Framework:

QSSI =
(AI × w1)
+
(LEGAL × w2)
+
(RES × w3)
+
(PQC × w4)

Output:

QSSI Score

Range:

0 ≤ QSSI ≤ 1

---

Stage 16 — Ranking Generation

Countries are ranked according to final QSSI scores.

Outputs:

- QSSI_RANKINGS_2026.csv
- Top 20 Sovereign Performers
- Bottom 20 Sovereign Performers

---

Stage 17 — Robustness Benchmarking

Three independent weighting architectures are compared.

PCA Weights

Canonical framework.

CRITIC Weights

Objective information-content weighting.

Entropy Weights

Information-diversity weighting.

---

Stage 18 — Rank Stability Validation

Spearman Rank Correlations

Equal Weight vs PCA

ρ = 0.9992427048606825
p = 7.153803172038685e-126

PCA vs Entropy

ρ = 0.9972671523233321
p = 2.290322902718063e-101

PCA vs CRITIC

ρ = 0.998304317405441
p = 1.776061187692281e-110

Interpretation:

Extremely High Ranking Stability

---

Stage 19 — Integrity Verification

Cryptographic integrity validation is performed using SHA256 hashing.

Generated Registry:

- QSSI_SHA256_AUDIT.csv

Purpose:

- File authenticity verification
- Reproducibility validation
- Archival preservation

---

Stage 20 — Audit Artifact Generation

Generated Artifacts:

- QSSI_MASTER_DATASET.csv
- QSSI_RANKINGS_2026.csv
- QSSI_FINAL_AUDIT.json
- QSSI_SHA256_AUDIT.csv
- QSSI_CRITIC_WEIGHTS.csv
- QSSI_ENTROPY_WEIGHTS.csv

---

Stage 21 — Computational Environment Documentation

Audit Metadata

Variable| Value
Countries| 90
Final N| 90
Missing Values| 0
Python Version| 3.12.13
Platform| Linux-6.6.122+-x86_64-with-glibc2.35

---

Stage 22 — FAIR+D Compliance

The computational architecture is aligned with:

- Findable
- Accessible
- Interoperable
- Reusable
- Defensible

principles.

---

Stage 23 — Reproducibility Architecture

The framework incorporates:

- Deterministic preprocessing
- Canonical harmonization
- Complete-case validation
- Statistical diagnostics
- Reliability assessment
- PCA-based weighting
- Robustness benchmarking
- Cryptographic integrity verification
- Audit-trail preservation
- Computational environment documentation
- Reproducible publication workflow

---

Pipeline Status

Data Validation:

PASSED

Country Harmonization:

PASSED

Statistical Validation:

PASSED

Reliability Diagnostics:

PASSED

Robustness Validation:

PASSED

Integrity Verification:

PASSED

Reproducibility Validation:

PASSED

Final Analytical Universe:

N = 90 Countries

---

Citation

Mazumdar, B. (2026).

Quantum-Veil Sovereignty Security Index (QSSI) 2026 Definitive World Edition.

Zenodo.

Current Definitive Edition DOI:

10.5281/zenodo.20385492

Canonical DOI (All Versions):

10.5281/zenodo.17302169

ORCID:

https://orcid.org/0009-0007-5615-3558

END OF FILE
