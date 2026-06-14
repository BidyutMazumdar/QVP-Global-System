Paper 1: Mathematical Foundations of QSSI

Sovereign Intelligence, Security and Stability Index (QSSI)

A Hybrid Entropy–CRITIC–PCA Framework for Sovereign Assessment

---

Author Information

Dr. B. Mazumdar
Independent Researcher and Founder, FAIR+D Canon

ORCID
https://orcid.org/0009-0007-5615-3558

---

DOI References

Canonical DOI
https://doi.org/10.5281/zenodo.19188944

Latest DOI
https://doi.org/10.5281/zenodo.20345444

---

Abstract

The Sovereign Intelligence, Security and Stability Index (QSSI) is a multidimensional composite framework designed to evaluate sovereign readiness across artificial intelligence capability, legal-institutional governance, post-quantum security preparedness, and national resilience capacity. The framework integrates objective weighting methodologies through Entropy Weighting, CRITIC Weighting, and Principal Component Analysis (PCA), producing a hybrid weighting architecture that minimizes subjective bias while maximizing statistical robustness.

The mathematical structure of QSSI is constructed upon normalized sovereign indicators, hybrid weighting fusion, composite score aggregation, reliability adjustment, and validation through Monte Carlo simulation and sensitivity analysis. The framework provides a reproducible methodology for comparative sovereign assessment across countries and institutional environments.

---

1. Introduction

Contemporary sovereign competitiveness increasingly depends upon the interaction of technological capability, institutional quality, cybersecurity preparedness, and resilience capacity. Traditional single-domain indices fail to capture these multidimensional interactions.

QSSI addresses this limitation through an integrated mathematical framework that combines:

- Artificial Intelligence Readiness
- Legal and Institutional Governance
- Post-Quantum Security Preparedness
- National Resilience Capacity

The framework employs objective statistical weighting procedures to ensure methodological transparency, reproducibility, and cross-country comparability.

---

2. Mathematical Architecture

The QSSI framework consists of five sequential stages:

1. Data Harmonization
2. Min-Max Normalization
3. Hybrid Weight Construction
4. Composite Score Aggregation
5. Reliability Adjustment

---

3. Data Harmonization Framework

The harmonized sovereign dataset contains four core dimensions:

Variable| Description
AI_INDEX| Artificial Intelligence Readiness
LEGAL_WGI_SCORE| Legal and Institutional Governance
PQC| Post-Quantum Cryptographic Preparedness
RES_INDEX| National Resilience Capacity

---

4. Min-Max Normalization

All variables are normalized onto a common [0,1] scale.

Normalization Equation

[
z_{ij}=\frac{x_{ij}-\min(x_i)}
{\max(x_i)-\min(x_i)}
]

Where:

Symbol| Definition
x_{ij}| Raw value
z_{ij}| Normalized value
\min(x_i)| Minimum value of indicator
\max(x_i)| Maximum value of indicator

This transformation ensures comparability across heterogeneous sovereign indicators.

---

5. Objective Weight Construction

Three independent weighting methodologies are employed.

5.1 Entropy Weighting

Entropy weighting measures informational diversity and indicator discrimination power.

Recovered Entropy Weights:

Indicator| Entropy Weight
AI_NORM| 0.395579
LEGAL_NORM| 0.237359
PQC_NORM| 0.153593
RES_NORM| 0.213469

---

5.2 CRITIC Weighting

CRITIC weighting incorporates both indicator variability and inter-indicator conflict.

Recovered CRITIC Weights:

Indicator| CRITIC Weight
AI_NORM| 0.300079
LEGAL_NORM| 0.208429
PQC_NORM| 0.259712
RES_NORM| 0.231780

---

5.3 Principal Component Analysis (PCA)

PCA weighting captures latent variance structures within the sovereign indicator space.

Recovered PCA Weights:

Indicator| PCA Weight
AI_NORM| 0.360168
LEGAL_NORM| 0.270896
PQC_NORM| 0.234829
RES_NORM| 0.134107

---

6. Hybrid Weight Fusion

The three independent weighting systems are combined through arithmetic averaging.

Hybrid Weight Equation

[
w_i=\frac{E_i+C_i+P_i}{3}
]

Where:

Symbol| Definition
E_i| Entropy Weight
C_i| CRITIC Weight
P_i| PCA Weight
w_i| Final Hybrid Weight

---

7. Final Recovered QSSI Weights

Indicator| Final Weight
AI_NORM| 0.351942
LEGAL_NORM| 0.238895
PQC_NORM| 0.216045
RES_NORM| 0.193119

Weight Sum Verification:

[
0.351942+0.238895+0.216045+0.193119=1.000001
]

Numerical discrepancy is attributable to rounding precision.

---

8. Composite QSSI Score

The final sovereign score is computed as a weighted aggregation of normalized indicators.

QSSI Equation

[
QSSI_j=\sum_i w_i z_{ij}
]

Expanded form:

[
QSSI=
0.351942(AI)+
0.238895(LEGAL)+
0.216045(PQC)+
0.193119(RES)
]

---

9. Reliability Adjustment Framework

To account for data confidence and coverage quality, QSSI incorporates a reliability-adjustment layer.

Reliability Equation

[
RAS_j=QSSI_j \times Conf_j
]

Where:

Symbol| Definition
QSSI| Composite Sovereign Score
Conf| Confidence Coefficient
RAS| Reliability Adjusted Score

---

10. Confidence Architecture

Confidence coefficients are assigned according to data completeness and methodological reliability.

Tier| Confidence
A| 1.00
B| 0.75
C| 0.50
D| 0.25

---

11. Validation Framework

The framework incorporates multiple robustness procedures.

Monte Carlo Validation

Recovered Stability Score:

Metric| Value
Monte Carlo Stability| 0.982032

---

Sensitivity Analysis

Metric| Value
Weight Sensitivity Stability| 0.999810

---

Rank Robustness

Metric| Value
Spearman Robustness| 0.982989
Kendall Robustness| 0.899043

---

External Benchmark Validation

Metric| Value
Benchmark Spearman Correlation| 0.980683

---

12. Indicator Influence Analysis

Recovered Indicator Correlations:

Indicator| Correlation
AI_INDEX| 0.946707
PQC| 0.913711
LEGAL_WGI_SCORE| 0.874468
RES_INDEX| 0.673914

---

13. Methodological Consistency

Correlation between weighting methodologies and final QSSI:

Comparison| Correlation
Entropy vs QSSI| 0.973829
CRITIC vs QSSI| 0.951864
PCA vs QSSI| 0.964681

---

14. Principal Component Structure

Recovered PCA Result:

Metric| Value
PC1 Explained Variance| 78.415099%

The first principal component captures the majority of variance across sovereign indicators, supporting dimensional coherence within the framework.

---

15. Reproducibility and Transparency

The QSSI framework is designed according to principles of:

- Reproducibility
- Transparency
- Cross-country comparability
- Objective weighting
- Statistical robustness
- Computational auditability

All reported mathematical structures, recovered weights, validation outputs, and aggregation procedures are derived from archival reconstruction evidence.

---

16. Conclusion

QSSI establishes a mathematically grounded sovereign assessment framework integrating artificial intelligence capability, governance quality, post-quantum preparedness, and resilience capacity. Through the fusion of Entropy, CRITIC, and PCA methodologies, the framework generates statistically robust composite scores while maintaining interpretability and reproducibility.

The recovered architecture demonstrates a coherent hybrid-weighting system, strong validation performance, and high methodological stability, supporting its application in sovereign benchmarking, strategic assessment, and comparative policy analysis.

---

References

Mazumdar, B. (2026). Sovereign Intelligence, Security and Stability Index (QSSI): Mathematical Foundations and Hybrid Weighting Architecture.

Canonical DOI: https://doi.org/10.5281/zenodo.19188944

Latest DOI: https://doi.org/10.5281/zenodo.20345444

ORCID: https://orcid.org/0009-0007-5615-3558
