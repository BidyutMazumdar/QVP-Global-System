# Statistical Tables and Empirical Validation Results

## QSSI™ 2026
### Sovereign Intelligence, Security and Stability Index
### FAIR+D Canon Research Series

**Author:** Dr. B. Mazumdar  
**ORCID:** 0009-0007-5615-3558  
**All Versions DOI:** 10.5281/zenodo.17302169  
**Current Edition DOI:** 10.5281/zenodo.20385492  

---

# 1. Source Dataset Coverage

| Dataset | Countries |
|----------|-----------:|
| AI_INDEX_2026_v1_MC_Canon | 195 |
| LEGAL_WGI_2026_v1_MC_Canon | 213 |
| RES_INDEX_2026_MC_Canon | 181 |
| PQC_NCSI_2026_MC_Canon | 124 |

---

# 2. Cross-Dataset Harmonization Matrix

| Dataset | AI | LEGAL | RES | PQC |
|----------|----:|------:|----:|----:|
| AI | 195 | 172 | 128 | 118 |
| LEGAL | 172 | 213 | 136 | 117 |
| RES | 128 | 136 | 181 | 94 |
| PQC | 118 | 117 | 94 | 124 |

---

# 3. Canonical Coverage Outcome

| Metric | Value |
|----------|------:|
| AI Coverage | 195 |
| LEGAL Coverage | 213 |
| RES Coverage | 181 |
| PQC Coverage | 124 |
| Excluded Due to PQC Coverage Constraints | 36 |
| Definitive Final N | 90 |

---

# 4. Final Harmonized Variables

| Variable | Coverage |
|-----------|---------:|
| AI_INDEX | 90 |
| LEGAL_WGI_SCORE | 90 |
| RES_INDEX | 90 |
| PQC | 90 |

---

# 5. Data Integrity Verification

```text
Final Dataset Shape
(90, 5)

Missing Values
country            0
AI_INDEX           0
LEGAL_WGI_SCORE    0
RES_INDEX          0
PQC                0
dtype: int64
```

No missing observations remain after harmonization and canonical filtering.

---

# 6. Country Coverage

## Included Countries (N = 90)

```text
0   Albania
1   Algeria
2   Angola
3   Antigua and Barbuda
4   Argentina
...
85  United Arab Emirates
86  United Kingdom
87  United States
88  Uruguay
89  Zimbabwe
```

Total Countries Included: **90**

---

# 7. Descriptive Statistics

| Statistic | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|------------|----------:|----------------:|-----------:|----:|
| Count | 90.000000 | 90.000000 | 90.000000 | 90.000000 |
| Mean | 0.566620 | 0.540517 | 0.394125 | 0.595676 |
| Std. Dev. | 0.250973 | 0.228008 | 0.140781 | 0.272357 |
| Minimum | 0.050407 | 0.108866 | 0.150195 | 0.000000 |
| 25th Percentile | 0.393117 | 0.359012 | 0.298129 | 0.376115 |
| Median | 0.633618 | 0.504046 | 0.371685 | 0.641621 |
| 75th Percentile | 0.766077 | 0.697156 | 0.459482 | 0.827448 |
| Maximum | 1.000000 | 0.966323 | 0.808925 | 0.982370 |

---

# 8. Correlation Matrix

| Variable | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|------------|----------:|----------------:|-----------:|----:|
| AI_INDEX | 1.000000 | 0.783568 | 0.517254 | 0.840634 |
| LEGAL_WGI_SCORE | 0.783568 | 1.000000 | 0.664976 | 0.730088 |
| RES_INDEX | 0.517254 | 0.664976 | 1.000000 | 0.380787 |
| PQC | 0.840634 | 0.730088 | 0.380787 | 1.000000 |

---

# 9. Distribution Diagnostics

## AI_INDEX

| Metric | Value |
|----------|------:|
| Skewness | -0.395939 |
| Kurtosis | -0.913245 |

## LEGAL_WGI_SCORE

| Metric | Value |
|----------|------:|
| Skewness | 0.183835 |
| Kurtosis | -0.892587 |

## RES_INDEX

| Metric | Value |
|----------|------:|
| Skewness | 0.780795 |
| Kurtosis | 0.498641 |

## PQC

| Metric | Value |
|----------|------:|
| Skewness | -0.443125 |
| Kurtosis | -1.006802 |

---

# 10. Sampling Adequacy and Factorability Tests

## Kaiser–Meyer–Olkin (KMO)

| Statistic | Value |
|------------|------:|
| KMO Score | 0.735587 |

Interpretation: Good sampling adequacy for multivariate dimensionality reduction.

---

## Bartlett's Test of Sphericity

| Statistic | Value |
|------------|------:|
| Chi-Square | 249.833794 |
| p-value | 4.450885068086372e-51 |

Interpretation: Correlation structure is highly significant and suitable for PCA.

---

# 11. Principal Component Analysis

## Eigenvalue Contribution

| Component | Variance Explained |
|------------|------------------:|
| PC1 | 0.74561879 |
| PC2 | 0.17028181 |
| PC3 | 0.04806765 |
| PC4 | 0.03603175 |

Total Explained Variance = 1.000000

---

## PCA Loading Matrix

| Variable | PC1 | PC2 | PC3 | PC4 |
|------------|------:|------:|------:|------:|
| AI_INDEX | 0.534197 | -0.272778 | -0.351497 | 0.718802 |
| LEGAL_WGI_SCORE | 0.536276 | 0.105185 | 0.835959 | 0.050156 |
| RES_INDEX | 0.416053 | 0.816887 | -0.359197 | -0.174850 |
| PQC | 0.503926 | -0.497216 | -0.220453 | -0.670996 |

---

## PCA-Derived Indicator Weights

| Variable | Weight |
|-----------|-------:|
| AI_INDEX | 0.268380 |
| LEGAL_WGI_SCORE | 0.269424 |
| RES_INDEX | 0.209024 |
| PQC | 0.253172 |

Weight Sum = 1.000000

---

# 12. Reliability Assessment

## Bootstrap Reliability Estimate

| Statistic | Value |
|------------|------:|
| Reliability Coefficient | 0.878569 |
| Lower 95% CI | 0.832 |
| Upper 95% CI | 0.915 |

---

# 13. CRITIC Objective Weights

| Variable | CRITIC Weight |
|-----------|--------------:|
| AI_INDEX | 0.241936 |
| LEGAL_WGI_SCORE | 0.210281 |
| RES_INDEX | 0.227146 |
| PQC | 0.320637 |

---

# 14. Entropy Weights

| Variable | Entropy Weight |
|-----------|---------------:|
| AI_INDEX | 0.290727 |
| LEGAL_WGI_SCORE | 0.234477 |
| RES_INDEX | 0.155500 |
| PQC | 0.319295 |

---

# 15. Weighting Robustness Assessment

## Equal Weight vs PCA

```text
Spearman Correlation
ρ = 0.9992427048606825

p-value
7.153803172038685e-126
```

---

## PCA vs Entropy

```text
Spearman Correlation
ρ = 0.9972671523233321

p-value
2.290322902718063e-101
```

---

## Additional Robustness Validation

```text
ρ = 0.998304317405441

p-value
1.776061187692281e-110
```

---

# 16. QSSI™ 2026 Top 20 Rankings

| Rank | Country | QSSI |
|------:|----------|------:|
| 1 | Denmark | 0.883898 |
| 2 | Norway | 0.854815 |
| 3 | Singapore | 0.846803 |
| 4 | United States | 0.826602 |
| 5 | Australia | 0.822180 |
| 6 | Germany | 0.819843 |
| 7 | Finland | 0.814612 |
| 8 | Ireland | 0.805977 |
| 9 | Canada | 0.804139 |
| 10 | Luxembourg | 0.798930 |
| 11 | France | 0.779162 |
| 12 | Sweden | 0.775481 |
| 13 | Japan | 0.769431 |
| 14 | Belgium | 0.762393 |
| 15 | Switzerland | 0.761517 |
| 16 | Austria | 0.755492 |
| 17 | United Kingdom | 0.749018 |
| 18 | United Arab Emirates | 0.747201 |
| 19 | Spain | 0.745928 |
| 20 | Iceland | 0.728642 |

---

# 17. QSSI™ 2026 Bottom 20 Rankings

| Rank | Country | QSSI |
|------:|----------|------:|
| 71 | Antigua and Barbuda | 0.351695 |
| 72 | Bosnia and Herzegovina | 0.342012 |
| 73 | Maldives | 0.339315 |
| 74 | Uganda | 0.332203 |
| 75 | Burkina Faso | 0.315858 |
| 76 | Cambodia | 0.303576 |
| 77 | Angola | 0.278110 |
| 78 | Guatemala | 0.255819 |
| 79 | Myanmar | 0.247054 |
| 80 | Chad | 0.239890 |
| 81 | Honduras | 0.230823 |
| 82 | Nicaragua | 0.220457 |
| 83 | Iraq | 0.220278 |
| 84 | Guinea | 0.219293 |
| 85 | Libya | 0.213475 |
| 86 | Zimbabwe | 0.213106 |
| 87 | Mali | 0.192921 |
| 88 | Burundi | 0.150303 |
| 89 | Liberia | 0.141950 |
| 90 | Haiti | 0.098629 |

---

# 18. Final Ranking Summary

## Top 10

| Rank | Country | QSSI |
|------:|----------|------:|
| 1 | Denmark | 0.883898 |
| 2 | Norway | 0.854815 |
| 3 | Singapore | 0.846803 |
| 4 | United States | 0.826602 |
| 5 | Australia | 0.822180 |
| 6 | Germany | 0.819843 |
| 7 | Finland | 0.814612 |
| 8 | Ireland | 0.805977 |
| 9 | Canada | 0.804139 |
| 10 | Luxembourg | 0.798930 |

---

## Bottom 10

| Rank | Country | QSSI |
|------:|----------|------:|
| 81 | Honduras | 0.230823 |
| 82 | Nicaragua | 0.220457 |
| 83 | Iraq | 0.220278 |
| 84 | Guinea | 0.219293 |
| 85 | Libya | 0.213475 |
| 86 | Zimbabwe | 0.213106 |
| 87 | Mali | 0.192921 |
| 88 | Burundi | 0.150303 |
| 89 | Liberia | 0.141950 |
| 90 | Haiti | 0.098629 |

---

# 19. Reproducibility and Computational Environment

| Parameter | Value |
|------------|--------|
| Timestamp | 2026-06-05T16:11:24.057391 |
| Python Version | 3.12.13 |
| Platform | Linux-6.6.122+-x86_64-with-glibc2.35 |
| Countries | 90 |
| Final N | 90 |

---

# 20. Data Integrity and SHA-256 Audit Ledger

| File | SHA-256 |
|--------|---------|
| AI_INDEX_2026_v1_MC_Canon.csv | 16656947ff8486b896640a00d05deccee086e52358f6614472ad38929af0b776 |
| LEGAL_WGI_2026_v1_MC_Canon.csv | 13e5310373fc4104b70b0eb410ccb1628099336f21fe705545b472290cc7b4e7 |
| RES_INDEX_2026_MC_Canon.csv | 4e936fa81a2fa2d491b897313ac136d38af431cb72f55b3adb85006bded88c9d |
| PQC_NCSI_2026_MC_Canon.csv | a421685fedadd3fb3b0b9ffbdb3822401ea4ab98098853b104f54397631cda8d |
| QSSI_MASTER_DATASET.csv | 6ac531236999faa3680978cbe09eb8c93e9ebc85e1881f937d257f873b727931 |
| QSSI_RANKINGS_2026.csv | 56681c6fcc4c89a89982b9e117beedde76f02ef4c1c473bd86079e66542d8215 |

---

# 21. Final Validation Statement

The finalized QSSI™ 2026 dataset comprises 90 sovereign entities with complete coverage across AI capability, legal-institutional governance quality, national resilience capacity, and post-quantum cybersecurity preparedness dimensions. Harmonization procedures produced a fully balanced dataset with zero missing observations. Multivariate diagnostics demonstrate strong suitability for composite index construction, including satisfactory sampling adequacy (KMO = 0.735587), highly significant Bartlett's test (p < 0.001), high internal reliability (0.878569), and exceptionally strong robustness across alternative weighting methodologies. The resulting QSSI framework provides a statistically validated, reproducible, auditable, and internationally comparable sovereign assessment architecture grounded in transparent computational procedures and complete data integrity verification.

---
