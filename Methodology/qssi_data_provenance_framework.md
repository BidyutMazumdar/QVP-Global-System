# QSSI Data Provenance Framework
## Quantum-Veil Sovereignty Security Index (QSSI™) 2026 Definitive World Edition
### FAIR+D Canon™ Global Framework

### Current Edition DOI
10.5281/zenodo.20385492

### All Versions DOI
10.5281/zenodo.17302169

### Author
Dr. B. Mazumdar

### ORCID
https://orcid.org/0009-0007-5615-3558

### Founder
FAIR+D Canon™ (India, 2025)

### Framework Classification
International Sovereign Capability Assessment Framework

### Document Classification
Official Data Provenance, Auditability, Integrity, Reproducibility, and Traceability Framework

---

# 1. Executive Summary

The Quantum-Veil Sovereignty Security Index (QSSI™) is a multidimensional sovereign capability assessment framework designed to evaluate national preparedness across four analytically distinct but interconnected dimensions:

- Artificial Intelligence Capability
- Governance and Legal Quality
- National Resilience Capacity
- Post-Quantum Cybersecurity Readiness

The framework integrates heterogeneous international datasets through a deterministic, reproducible, audit-traceable, and statistically validated methodology consistent with the FAIR+D Canon™ principles.

This provenance framework documents the complete lifecycle of data acquisition, validation, harmonization, transformation, integration, statistical verification, reproducibility assessment, integrity auditing, and archival preservation associated with the QSSI™ 2026 Definitive World Edition.

---

# 2. Provenance Objectives

The provenance architecture was established to ensure:

- Full data traceability
- Transparent methodological documentation
- Reproducible computational workflows
- Dataset integrity verification
- Audit-ready evidence preservation
- Long-term archival sustainability
- Independent verification capability
- FAIR+D Canon™ compliance

---

# 3. Source Data Architecture

## Core Sovereign Capability Components

| Dimension | Dataset | Coverage |
|------------|------------|------------|
| Artificial Intelligence Capability | AI_INDEX_2026_v1_MC_Canon.csv | 195 Countries |
| Governance and Legal Quality | LEGAL_WGI_2026_v1_MC_Canon.csv | 213 Countries |
| National Resilience Capacity | RES_INDEX_2026_MC_Canon.csv | 181 Countries |
| Post-Quantum Cybersecurity Readiness | PQC_NCSI_2026_MC_Canon.csv | 124 Countries |

---

# 4. Dataset Coverage Audit

## Coverage Matrix

| Dataset | Coverage |
|----------|----------|
| AI | 195 |
| LEGAL | 213 |
| RES | 181 |
| PQC | 124 |

---

## Pairwise Intersection Audit

| | AI | LEGAL | RES | PQC |
|------|------|------|------|------|
| AI | 195 | 172 | 128 | 118 |
| LEGAL | 172 | 213 | 136 | 117 |
| RES | 128 | 136 | 181 | 94 |
| PQC | 118 | 117 | 94 | 124 |

---

## Definitive Harmonized Universe

| Metric | Value |
|----------|----------|
| Definitive Final N | 90 |
| Countries Included | 90 |
| Countries Excluded Due To PQC Coverage Constraints | 36 |
| Missing Values | 0 |
| Final Dataset Rows | 90 |
| Final Dataset Columns | 5 |

---

# 5. Country Coverage Boundary

## First Country

Albania

## Last Country

Zimbabwe

## Country Coverage Range

Albania, Algeria, Angola, Antigua and Barbuda, Argentina, Australia, Austria, Belgium, Bosnia and Herzegovina, Burkina Faso, Burundi, Cambodia, Canada, Chad, Denmark, Finland, France, Germany, Guatemala, Guinea, Haiti, Honduras, Iceland, Iraq, Ireland, Japan, Liberia, Libya, Luxembourg, Mali, Maldives, Myanmar, Nicaragua, Norway, Singapore, Spain, Sweden, Switzerland, Uganda, United Arab Emirates, United Kingdom, United States, Uruguay, Zimbabwe

---

# 6. Data Quality Validation

## Missing Value Audit

| Variable | Missing |
|------------|------------|
| country | 0 |
| AI_INDEX | 0 |
| LEGAL_WGI_SCORE | 0 |
| RES_INDEX | 0 |
| PQC | 0 |

### Missing Data Status

Verified Clean Dataset

---

# 7. Statistical Suitability Assessment

## PCA Explained Variance

| Component | Variance |
|------------|------------|
| PC1 | 0.74561879 |
| PC2 | 0.17028181 |
| PC3 | 0.04806765 |
| PC4 | 0.03603175 |

### Total Explained Variance

0.9999999999999999

---

## Kaiser-Meyer-Olkin (KMO)

| Statistic | Value |
|------------|------------|
| KMO | 0.7355868518654463 |

Interpretation:

Good sampling adequacy for multivariate dimensionality analysis.

---

## Bartlett's Test of Sphericity

| Statistic | Value |
|------------|------------|
| Chi-Square | 249.83379389196242 |
| P-Value | 4.450885068086372e-51 |

Interpretation:

Highly significant correlation structure suitable for principal component analysis.

---

# 8. Reliability Assessment

## Cronbach's Alpha

| Metric | Value |
|------------|------------|
| Alpha | 0.8785685555594794 |

### 95% Confidence Interval

| Lower | Upper |
|------------|------------|
| 0.832 | 0.915 |

Interpretation:

Excellent internal consistency across sovereign capability dimensions.

---

# 9. Correlation Structure

| Variable | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|------------|------------|------------|------------|------------|
| AI_INDEX | 1.000000 | 0.783568 | 0.517254 | 0.840634 |
| LEGAL_WGI_SCORE | 0.783568 | 1.000000 | 0.664976 | 0.730088 |
| RES_INDEX | 0.517254 | 0.664976 | 1.000000 | 0.380787 |
| PQC | 0.840634 | 0.730088 | 0.380787 | 1.000000 |

---

# 10. Distribution Diagnostics

## AI_INDEX

- Skewness: -0.39593851843313316
- Kurtosis: -0.9132445811266638

## LEGAL_WGI_SCORE

- Skewness: 0.18383490244953005
- Kurtosis: -0.8925871305381747

## RES_INDEX

- Skewness: 0.7807954023495343
- Kurtosis: 0.49864057599433886

## PQC

- Skewness: -0.4431250138665039
- Kurtosis: -1.0068022159176826

---

# 11. Principal Component Validation

## PCA Loadings

| Variable | PC1 | PC2 | PC3 | PC4 |
|------------|------------|------------|------------|------------|
| AI_INDEX | 0.534197 | -0.272778 | -0.351497 | 0.718802 |
| LEGAL_WGI_SCORE | 0.536276 | 0.105185 | 0.835959 | 0.050156 |
| RES_INDEX | 0.416053 | 0.816887 | -0.359197 | -0.174850 |
| PQC | 0.503926 | -0.497216 | -0.220453 | -0.670996 |

---

## PCA Canonical Weights

| Variable | Weight |
|------------|------------|
| AI_INDEX | 0.26837950 |
| LEGAL_WGI_SCORE | 0.26942446 |
| RES_INDEX | 0.20902441 |
| PQC | 0.25317163 |

---

# 12. Alternative Weight Validation

## CRITIC Weights

| Variable | Weight |
|------------|------------|
| AI_INDEX | 0.241936 |
| LEGAL_WGI_SCORE | 0.210281 |
| RES_INDEX | 0.227146 |
| PQC | 0.320637 |

---

## Entropy Weights

| Variable | Weight |
|------------|------------|
| AI_INDEX | 0.290727 |
| LEGAL_WGI_SCORE | 0.234477 |
| RES_INDEX | 0.155500 |
| PQC | 0.319295 |

---

# 13. Robustness Assessment

## Rank Stability Verification

| Comparison | Spearman ρ | P-Value |
|------------|------------|------------|
| Equal Weight vs PCA | 0.9992427048606825 | 7.153803172038685e-126 |
| PCA vs Entropy | 0.9972671523233321 | 2.290322902718063e-101 |
| PCA vs CRITIC | 0.998304317405441 | 1.776061187692281e-110 |

Interpretation:

Extremely high rank persistence across independent weighting methodologies demonstrates strong methodological robustness and stability.

---

# 14. Sovereign Ranking Audit

## Top 5 Countries

| Rank | Country | QSSI |
|------------|------------|------------|
| 1 | Denmark | 0.883898 |
| 2 | Norway | 0.854815 |
| 3 | Singapore | 0.846803 |
| 4 | United States | 0.826602 |
| 5 | Australia | 0.822180 |

---

## Bottom 5 Countries

| Rank | Country | QSSI |
|------------|------------|------------|
| 86 | Zimbabwe | 0.213106 |
| 87 | Mali | 0.192921 |
| 88 | Burundi | 0.150303 |
| 89 | Liberia | 0.141950 |
| 90 | Haiti | 0.098629 |

---

# 15. Dataset Integrity Verification

## SHA256 Audit Registry

| File | SHA256 |
|------------|------------|
| AI_INDEX_2026_v1_MC_Canon.csv | 16656947ff8486b896640a00d05deccee086e52358f6614472ad38929af0b776 |
| LEGAL_WGI_2026_v1_MC_Canon.csv | 13e5310373fc4104b70b0eb410ccb1628099336f21fe705545b472290cc7b4e7 |
| RES_INDEX_2026_MC_Canon.csv | 4e936fa81a2fa2d491b897313ac136d38af431cb72f55b3adb85006bded88c9d |
| PQC_NCSI_2026_MC_Canon.csv | a421685fedadd3fb3b0b9ffbdb3822401ea4ab98098853b104f54397631cda8d |
| QSSI_MASTER_DATASET.csv | 6ac531236999faa3680978cbe09eb8c93e9ebc85e1881f937d257f873b727931 |
| QSSI_RANKINGS_2026.csv | 56681c6fcc4c89a89982b9e117beedde76f02ef4c1c473bd86079e66542d8215 |

---

# 16. Generated Audit Artifacts

- QSSI_PAIRWISE_INTERSECTION_AUDIT.csv
- QSSI_MASTER_DATASET.csv
- QSSI_RANKINGS_2026.csv
- QSSI_CRITIC_WEIGHTS.csv
- QSSI_ENTROPY_WEIGHTS.csv
- QSSI_SHA256_AUDIT.csv
- QSSI_FINAL_AUDIT.json

---

# 17. FAIR+D Compliance Framework

- Findable
- Accessible
- Interoperable
- Reusable
- Defensible

---

# 18. Reproducibility Framework

- Deterministic preprocessing pipeline
- Canonical country harmonization
- Explicit intersection constraints
- Fixed PCA-derived weighting system
- Complete audit trail preservation
- Statistical validation documentation
- SHA256 dataset verification
- Reproducible computational environment
- Version-controlled archival publication
- Cross-method robustness validation

---

# 19. Computational Environment Audit

| Variable | Value |
|------------|------------|
| Timestamp | 2026-06-05T16:11:24.057391 |
| Python Version | 3.12.13 |
| Platform | Linux-6.6.122+-x86_64-with-glibc2.35 |
| Countries | 90 |
| Final N | 90 |

---

# 20. Provenance Governance Principles

The provenance framework is governed by the following principles:

- Transparency
- Traceability
- Reproducibility
- Auditability
- Documentation Integrity
- Methodological Consistency
- Evidence Preservation
- FAIR+D Compliance
- Version Governance
- Long-Term Archival Sustainability

---

# 21. Citation

Mazumdar, B. (2026).

*Quantum-Veil Sovereignty Security Index (QSSI™) 2026 Definitive World Edition.*

Zenodo.

Current Edition DOI: 10.5281/zenodo.20385492

All Versions DOI: 10.5281/zenodo.17302169

ORCID: https://orcid.org/0009-0007-5615-3558

---

## Version

**QSSI™ 2026 Definitive World Edition — FAIR+D Canon™ Global Framework — Data Provenance, Dataset Traceability, Coverage Validation, Statistical Adequacy Assessment, Reliability Diagnostics, Principal Component Validation, CRITIC Benchmarking, Entropy Weight Validation, Robustness Assessment, SHA256 Integrity Verification, Audit Traceability, Reproducibility Assessment, and Sovereign Capability Analytics Release.**
