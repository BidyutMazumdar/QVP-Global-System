QSSI 2026 Data Validation Report

Quantum-Veil Sovereignty Security Index (QSSI)

FAIR+D Canon™ Global Framework

---

Current Definitive Edition DOI

10.5281/zenodo.20385492

Canonical DOI (All Versions)

10.5281/zenodo.17302169

Author

Dr. B. Mazumdar

ORCID

https://orcid.org/0009-0007-5615-3558

Framework Classification

Data Validation, Statistical Verification, Computational Integrity Assessment, Reproducibility Evaluation, Robustness Analysis, Audit Verification, and Sovereign Capability Analytics

Framework Status

QSSI 2026 Definitive World Edition

---

Abstract

This report presents the complete validation, verification, integrity assessment, statistical diagnostics, robustness evaluation, reproducibility verification, and audit-traceable quality assurance framework underlying the Quantum-Veil Sovereignty Security Index (QSSI) 2026 Definitive World Edition.

The validation process evaluates dataset coverage, sovereign harmonization consistency, complete-case analytical universe construction, missing-data diagnostics, dimensional adequacy, distributional behavior, reliability assessment, principal component structure, weighting robustness, ranking stability, computational reproducibility, and cryptographic integrity verification.

All reported outputs originate directly from the canonical FAIR+D Canon™ implementation used to construct the QSSI 2026 Definitive World Edition.

---

1. Dataset Coverage Validation

Source Dataset Coverage

Dimension| Dataset| Coverage
Artificial Intelligence Capability| AI_INDEX_2026| 195
Governance & Legal Quality| LEGAL_WGI_2026| 213
National Resilience Capacity| RES_INDEX_2026| 181
Post-Quantum Cybersecurity Readiness| PQC_NCSI_2026| 124

---

2. Cross-Domain Coverage Validation

Coverage Summary

Dataset| Coverage
AI| 195
LEGAL| 213
RES| 181
PQC| 124

Cross-Domain Overlap Matrix

| AI| LEGAL| RES| PQC
AI| 195| 172| 128| 118
LEGAL| 172| 213| 136| 117
RES| 128| 136| 181| 94
PQC| 118| 117| 94| 124

---

3. Harmonized Sovereign Analytical Universe Validation

Definitive Final Analytical Sample

FINAL N = 90

Validation Summary

Metric| Value
Countries Included| 90
Countries Excluded Due To PQC Coverage Constraints| 36
Missing Values| 0
Final Observations| 90

Dataset Shape

(90, 5)

Coverage Range

Albania
Algeria
Angola
Antigua and Barbuda
Argentina
...
United Arab Emirates
United Kingdom
United States
Uruguay
Zimbabwe

Missing Value Validation

country              0
AI_INDEX             0
LEGAL_WGI_SCORE      0
RES_INDEX            0
PQC                  0
dtype: int64

Validation Result

Complete-case intersection filtering successfully generated a fully populated analytical universe with zero missing observations.

---

4. Harmonized Dataset Verification Sample

Country| AI_INDEX| LEGAL_WGI_SCORE| RES_INDEX| PQC
Albania| 0.446322| 0.487651| 0.270189| 0.955820
Algeria| 0.449950| 0.358597| 0.275554| 0.345157
Angola| 0.227441| 0.297740| 0.300972| 0.292056
Antigua and Barbuda| 0.204852| 0.607289| 0.454614| 0.150382
Argentina| 0.700634| 0.455790| 0.348677| 0.575191

---

5. Statistical Adequacy Validation

Eigenvalue Structure

[0.74561879 0.17028181 0.04806765 0.03603175]

Eigenvalue Sum

0.9999999999999999

Kaiser-Meyer-Olkin (KMO)

Statistic| Value
KMO| 0.7355868518654463

Validation Result

Good sampling adequacy for multivariate dimensionality assessment.

Bartlett's Test of Sphericity

Statistic| Value
Chi-Square| 249.83379389196242
P-Value| 4.450885068086372e-51

Validation Result

Highly significant correlation structure suitable for principal component analysis.

---

6. Descriptive Statistical Validation

Variable| Count| Mean| Std| Min| 25%| Median| 75%| Max
AI_INDEX| 90| 0.566620| 0.250973| 0.050407| 0.393117| 0.633618| 0.766077| 1.000000
LEGAL_WGI_SCORE| 90| 0.540517| 0.228008| 0.108866| 0.359012| 0.504046| 0.697156| 0.966323
RES_INDEX| 90| 0.394125| 0.140781| 0.150195| 0.298129| 0.371685| 0.459482| 0.808925
PQC| 90| 0.595676| 0.272357| 0.000000| 0.376115| 0.641621| 0.827448| 0.982370

---

7. Correlation Structure Validation

Variable| AI_INDEX| LEGAL_WGI_SCORE| RES_INDEX| PQC
AI_INDEX| 1.000000| 0.783568| 0.517254| 0.840634
LEGAL_WGI_SCORE| 0.783568| 1.000000| 0.664976| 0.730088
RES_INDEX| 0.517254| 0.664976| 1.000000| 0.380787
PQC| 0.840634| 0.730088| 0.380787| 1.000000

Validation Result

All dimensions demonstrate meaningful positive relationships while preserving distinct analytical contributions.

---

8. Distribution Diagnostics Validation

AI_INDEX

- Skewness = -0.39593851843313316
- Kurtosis = -0.9132445811266638

LEGAL_WGI_SCORE

- Skewness = 0.18383490244953005
- Kurtosis = -0.8925871305381747

RES_INDEX

- Skewness = 0.7807954023495343
- Kurtosis = 0.49864057599433886

PQC

- Skewness = -0.4431250138665039
- Kurtosis = -1.0068022159176826

Validation Result

Observed distributions remain within acceptable ranges for comparative sovereign capability assessment.

---

9. Reliability Validation

Cronbach's Alpha

Metric| Value
Alpha| 0.8785685555594794

95% Confidence Interval

[0.832, 0.915]

Validation Result

Excellent internal consistency across sovereign capability dimensions.

---

10. Principal Component Validation

PCA Loadings

Variable| PC1| PC2| PC3| PC4
AI_INDEX| 0.534197| -0.272778| -0.351497| 0.718802
LEGAL_WGI_SCORE| 0.536276| 0.105185| 0.835959| 0.050156
RES_INDEX| 0.416053| 0.816887| -0.359197| -0.174850
PQC| 0.503926| -0.497216| -0.220453| -0.670996

PCA-Derived Canonical Weights

Variable| Weight
AI_INDEX| 0.26837950
LEGAL_WGI_SCORE| 0.26942446
RES_INDEX| 0.20902441
PQC| 0.25317163

---

11. Alternative Weight Validation

CRITIC Weights

Variable| Weight
AI_INDEX| 0.241936
LEGAL_WGI_SCORE| 0.210281
RES_INDEX| 0.227146
PQC| 0.320637

Entropy Weights

Variable| Weight
AI_INDEX| 0.290727
LEGAL_WGI_SCORE| 0.234477
RES_INDEX| 0.155500
PQC| 0.319295

---

12. Robustness Validation

Rank Correlation Assessment

Equal Weight vs PCA

Spearman ρ = 0.9992427048606825
p-value = 7.153803172038685e-126

PCA vs Entropy

Spearman ρ = 0.9972671523233321
p-value = 2.290322902718063e-101

PCA vs CRITIC

Spearman ρ = 0.998304317405441
p-value = 1.776061187692281e-110

Validation Result

Extremely high rank-order consistency across independent weighting methodologies confirms strong methodological robustness.

---

13. Ranking Validation

Top 20 Sovereign Performers

Rank| Country| QSSI
1| Denmark| 0.883898
2| Norway| 0.854815
3| Singapore| 0.846803
4| United States| 0.826602
5| Australia| 0.822180
6| Germany| 0.819843
7| Finland| 0.814612
8| Ireland| 0.805977
9| Canada| 0.804139
10| Luxembourg| 0.798930
11| France| 0.779162
12| Sweden| 0.775481
13| Japan| 0.769431
14| Belgium| 0.762393
15| Switzerland| 0.761517
16| Austria| 0.755492
17| United Kingdom| 0.749018
18| United Arab Emirates| 0.747201
19| Spain| 0.745928
20| Iceland| 0.728642

---

14. Bottom 20 Sovereign Performers

Rank| Country| QSSI
71| Antigua and Barbuda| 0.351695
72| Bosnia and Herzegovina| 0.342012
73| Maldives| 0.339315
74| Uganda| 0.332203
75| Burkina Faso| 0.315858
76| Cambodia| 0.303576
77| Angola| 0.278110
78| Guatemala| 0.255819
79| Myanmar| 0.247054
80| Chad| 0.239890
81| Honduras| 0.230823
82| Nicaragua| 0.220457
83| Iraq| 0.220278
84| Guinea| 0.219293
85| Libya| 0.213475
86| Zimbabwe| 0.213106
87| Mali| 0.192921
88| Burundi| 0.150303
89| Liberia| 0.141950
90| Haiti| 0.098629

---

15. Generated Validation Artifacts

- QSSI_MASTER_DATASET.csv
- QSSI_RANKINGS_2026.csv
- QSSI_FINAL_AUDIT.json
- QSSI_SHA256_AUDIT.csv
- QSSI_CRITIC_WEIGHTS.csv
- QSSI_ENTROPY_WEIGHTS.csv

---

16. Cryptographic Integrity Verification

SHA256 Audit Registry

File| SHA256
AI_INDEX_2026_v1_MC_Canon.csv| 16656947ff8486b896640a00d05deccee086e52358f6614472ad38929af0b776
LEGAL_WGI_2026_v1_MC_Canon.csv| 13e5310373fc4104b70b0eb410ccb1628099336f21fe705545b472290cc7b4e7
RES_INDEX_2026_MC_Canon.csv| 4e936fa81a2fa2d491b897313ac136d38af431cb72f55b3adb85006bded88c9d
PQC_NCSI_2026_MC_Canon.csv| a421685fedadd3fb3b0b9ffbdb3822401ea4ab98098853b104f54397631cda8d
QSSI_MASTER_DATASET.csv| 6ac531236999faa3680978cbe09eb8c93e9ebc85e1881f937d257f873b727931
QSSI_RANKINGS_2026.csv| 56681c6fcc4c89a89982b9e117beedde76f02ef4c1c473bd86079e66542d8215

Validation Result

All archived computational artifacts are verifiable through deterministic SHA256 integrity auditing.

---

17. Audit Metadata Validation

Variable| Value
Timestamp| 2026-06-05T16:11:24.057391
Python Version| 3.12.13
Platform| Linux-6.6.122+-x86_64-with-glibc2.35
Countries| 90
Final N| 90

---

18. FAIR+D Compliance Validation

- Findable
- Accessible
- Interoperable
- Reusable
- Defensible

---

19. Reproducibility Validation Architecture

- Deterministic preprocessing pipeline
- Canonical country harmonization
- Complete-case intersection filtering
- Fixed PCA-derived weighting architecture
- Statistical validation framework
- Reliability diagnostics
- Principal component verification
- Robustness benchmarking
- Ranking stability assessment
- Audit trail preservation
- SHA256 integrity verification
- Computational environment documentation
- Version-controlled publication workflow
- Reproducible sovereign analytics architecture

---

Conclusion

The QSSI 2026 validation framework confirms complete data integrity, zero missing observations, statistically adequate dimensional structure, strong internal reliability, highly stable weighting performance, robust rank persistence, deterministic reproducibility, cryptographic auditability, and full FAIR+D Canon™ compliance across the harmonized sovereign analytical universe.

---

Citation

Mazumdar, B. (2026).

Quantum-Veil Sovereignty Security Index (QSSI) 2026 Definitive World Edition.

Zenodo.

Current Definitive Edition DOI: 10.5281/zenodo.20385492

Canonical DOI (All Versions): 10.5281/zenodo.17302169

ORCID: https://orcid.org/0009-0007-5615-3558

---

END OF FILE
