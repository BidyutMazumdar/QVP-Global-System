# QSSI 2026 Comparative Analysis

## FAIR+D Canon™ Global Framework

### Current Edition DOI
10.5281/zenodo.20385492

### All Versions DOI
10.5281/zenodo.17302169

### Author
Dr. B. Mazumdar

### ORCID
https://orcid.org/0009-0007-5615-3558

---

## Citation

You can cite all versions of the Quantum Sovereign Security Index (QSSI) framework using the DOI:

**10.5281/zenodo.17302169**

Current canonical edition:

**10.5281/zenodo.20385492**

---

## Overview

The Quantum Sovereign Security Index (QSSI) 2026 is a multidimensional sovereign benchmarking framework designed to evaluate national preparedness across artificial intelligence governance, legal and regulatory quality, post-quantum cybersecurity readiness, and sovereign resilience.

The framework integrates four independently validated dimensions into a unified composite architecture using Entropy, CRITIC, and Principal Component Analysis methodologies. The resulting index provides a globally comparable assessment of sovereign security readiness under emerging technological, cyber, governance, and resilience conditions.

---

## Framework Architecture

| Dimension | Description |
|------------|------------|
| AI | Artificial Intelligence Governance and Readiness |
| LEGAL | Rule of Law and Regulatory Quality |
| PQC | Post-Quantum Cybersecurity Readiness |
| RES | Sovereign Economic and Financial Resilience |

---

## Coverage

| Metric | Value |
|----------|----------|
| Countries Evaluated | 195 |
| Total Archived Files | 270 |
| Composite Dimensions | 4 |
| Monte Carlo Simulations | 1000 |
| Validation Frameworks | Multiple |
| Reproducibility Status | PASS |
| FAIR+D Compliance | PASS |

---

## Final Composite Weights

| Dimension | Entropy | CRITIC | PCA | Final Weight |
|------------|------------|------------|------------|------------|
| AI | 0.395579 | 0.300079 | 0.360168 | 0.351942 |
| LEGAL | 0.237359 | 0.208429 | 0.270896 | 0.238895 |
| PQC | 0.153593 | 0.259712 | 0.234829 | 0.216045 |
| RES | 0.213469 | 0.231780 | 0.134107 | 0.193119 |

### Weight Distribution

| Dimension | Weight (%) |
|------------|------------|
| AI | 35.194224 |
| LEGAL | 23.889468 |
| PQC | 21.604454 |
| RES | 19.311854 |

---

## Comparative Importance Analysis

| Dimension | Framework Weight | Average Rank Shift | Relative Importance |
|------------|------------|------------|------------|
| AI | 0.351942 | 10.3538 | 0.356210 |
| LEGAL | 0.238895 | 7.0718 | 0.243296 |
| PQC | 0.216045 | 5.8205 | 0.200247 |
| RES | 0.193119 | 5.8205 | 0.200247 |

---

## Leave-One-Dimension-Out Comparative Analysis

| Removed Dimension | Average Rank Shift | Maximum Rank Shift | Spearman with QSSI |
|-------------------|-------------------|-------------------|-------------------|
| AI | 10.3538 | 47 | 0.968106 |
| LEGAL | 7.0718 | 37 | 0.983962 |
| PQC | 5.8205 | 31 | 0.989257 |
| RES | 5.8205 | 27 | 0.990631 |

---

## Robustness Comparison

| Scenario | Top10 Common | Top25 Common | Top50 Common | Spearman | Kendall |
|------------|------------|------------|------------|------------|------------|
| AI_REMOVED | 9 | 23 | 43 | 0.968106 | 0.856508 |
| LEGAL_REMOVED | 9 | 24 | 47 | 0.983962 | 0.900074 |
| PQC_REMOVED | 10 | 23 | 48 | 0.989257 | 0.919953 |
| RES_REMOVED | 7 | 24 | 47 | 0.990631 | 0.919636 |

---

## Weight Sensitivity Assessment

| Perturbation | Spearman | Average Rank Shift | Maximum Rank Shift |
|------------|------------|------------|------------|
| 5% | 0.999935 | 0.30000 | 4 |
| 10% | 0.999823 | 0.63075 | 5 |
| 15% | 0.999673 | 0.91280 | 6 |

---

## Incremental Validity Analysis

| Metric | Value |
|----------|----------|
| Countries | 195 |
| RES Framework Weight Percent | 19.3119 |
| Average Absolute Rank Shift | 5.8205 |
| Maximum Rank Improvement | 27 |
| Maximum Rank Penalty | -19 |

---

## External Benchmark Comparison

| Benchmark | Pearson r | Spearman r | Kendall Tau | Convergent Validity |
|------------|------------|------------|------------|------------|
| SCI | 0.985837 | 0.983078 | 0.896718 | Possible Redundancy |
| SCI_PLUS | 0.986295 | 0.987751 | 0.912806 | Possible Redundancy |
| SCI_ULTRA | 0.998136 | 0.997788 | 0.970077 | Possible Redundancy |
| SCI_ULTRA_ADJUSTED | 0.953030 | 0.947723 | 0.850386 | Very Strong |

---

## Confidence Tier Distribution

| Tier | Countries |
|--------|--------|
| A | 87 |
| B | 59 |
| C | 27 |
| D | 22 |

---

## Monte Carlo Stability Summary

| Metric | Value |
|----------|----------|
| Countries | 195 |
| Simulations | 1000 |
| Mean Rank SD | 3.5037 |
| Median Rank SD | 1.9825 |
| Maximum Rank SD | 13.5572 |

---

## Top 20 Countries

| Rank | Country | QSSI Score |
|--------|--------|--------|
| 1 | Denmark | 0.967511 |
| 2 | Republic of Korea | 0.933336 |
| 3 | Norway | 0.928291 |
| 4 | Singapore | 0.922490 |
| 5 | United Kingdom | 0.910206 |
| 6 | Netherlands | 0.909125 |
| 7 | Ireland | 0.887083 |
| 8 | Australia | 0.886142 |
| 9 | Germany | 0.880332 |
| 10 | Luxembourg | 0.869261 |
| 11 | Finland | 0.851911 |
| 12 | Canada | 0.847574 |
| 13 | Estonia | 0.846844 |
| 14 | Sweden | 0.836995 |
| 15 | France | 0.833090 |
| 16 | United States of America | 0.833090 |
| 17 | Japan | 0.821052 |
| 18 | Switzerland | 0.810304 |
| 19 | United Arab Emirates | 0.807638 |
| 20 | Taiwan | 0.800727 |

---

## Reproducibility Assessment

| Validation Component | Status |
|----------------------|--------|
| Dataset Integrity | PASS |
| Hash Registry | PASS |
| Artifact Registry | PASS |
| Environment Capture | PASS |
| Metadata Capture | PASS |
| Reproducibility Validation | PASS |

---

## FAIR+D Compliance Assessment

| Requirement | Status |
|------------|--------|
| Findable | PASS |
| Accessible | PASS |
| Interoperable | PASS |
| Reusable | PASS |
| Deterministic Reproducibility | PASS |

---

## Audit Summary

| Criterion | Status |
|------------|--------|
| Dataset Integrity | PASS |
| Metadata Validation | PASS |
| Framework Validation | PASS |
| Robustness Validation | PASS |
| Reproducibility Validation | PASS |
| FAIR+D Compliance | PASS |
| Publication Readiness | PASS |

---

## Primary Research Artifacts

- QSSI_2026_MASTER_FINAL.csv
- QSSI_2026_Final_Rankings.csv
- QSSI_2026_Weights.csv
- QSSI_2026_Robustness_Validation.csv
- QSSI_2026_MonteCarlo_Validation.csv
- QSSI_2026_External_Validation.csv
- QSSI_2026_Shapley_LODO.csv
- QSSI_2026_Incremental_Validity.csv
- QSSI_2026_Dominance_Analysis.csv
- QSSI_2026_Weight_Sensitivity_Summary.csv
- QSSI_2026_Reproducibility_Audit.csv
- QSSI_2026_FAIRD_Compliance_Report.csv
- QSSI_2026_Final_Audit_Report.csv
- QSSI_2026_Manifest.json
- QSSI_2026_Journal_Submission_Package.json

---

## Archival Metadata

| Field | Value |
|---------|---------|
| Framework | Quantum Sovereign Security Index |
| Edition | QSSI 2026 |
| Countries | 195 |
| Archived Files | 270 |
| Current Edition DOI | 10.5281/zenodo.20385492 |
| All Versions DOI | 10.5281/zenodo.17302169 |
| ORCID | https://orcid.org/0009-0007-5615-3558 |

---

Version: QSSI 2026 Definitive World Edition
