# QSSI 2026 Methodological Appendix

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

# 1. Methodological Overview

The Quantitative Sovereign Sustainability Index (QSSI) 2026 integrates four internationally recognized dimensions of national capability, governance, resilience, and policy quality:

| Dimension | Variable |
|------------|------------|
| Artificial Intelligence Capacity | AI_INDEX |
| Governance and Rule of Law | LEGAL_WGI_SCORE |
| National Resilience | RES_INDEX |
| Policy Quality and Coordination | PQC |

The framework follows the FAIR+D Canon™ methodology and applies strict canonical harmonization, complete-case validation, multivariate diagnostics, Principal Component Analysis (PCA), and TOPSIS aggregation.

---

# 2. Source Dataset Coverage

```text
AI     = 195
LEGAL  = 213
RES    = 181
PQC    = 124
```

---

# 3. Cross-Dataset Intersection Matrix

```text
       AI  LEGAL  RES  PQC

AI     195   172  128  118
LEGAL  172   213  136  117
RES    128   136  181   94
PQC    118   117   94  124
```

---

# 4. Canonical Harmonization Results

```text
Countries = 90

Excluded due to PQC coverage = 36

AI     = 195
LEGAL  = 213
RES    = 181
PQC    = 124

FINAL  = 90
```

---

# 5. Final Harmonized Variables

| Variable | Coverage |
|-----------|-----------|
| AI_INDEX | 90 |
| LEGAL_WGI_SCORE | 90 |
| RES_INDEX | 90 |
| PQC | 90 |

---

# 6. Data Integrity Verification

```text
(90, 5)

country              0
AI_INDEX             0
LEGAL_WGI_SCORE      0
RES_INDEX            0
PQC                  0
dtype: int64
```

No missing observations remained after harmonization and canonical filtering.

---

# 7. Country Coverage

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

---

# 8. Descriptive Statistics

| Statistic | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|------------|------------|------------|------------|------------|
| Count | 90.0 | 90.0 | 90.0 | 90.0 |
| Mean | 0.566620 | 0.540517 | 0.394125 | 0.595676 |
| Std | 0.250973 | 0.228008 | 0.140781 | 0.272357 |
| Min | 0.050407 | 0.108866 | 0.150195 | 0.000000 |
| 25% | 0.393117 | 0.359012 | 0.298129 | 0.376115 |
| 50% | 0.633618 | 0.504046 | 0.371685 | 0.641621 |
| 75% | 0.766077 | 0.697156 | 0.459482 | 0.827448 |
| Max | 1.000000 | 0.966323 | 0.808925 | 0.982370 |

---

# 9. Correlation Matrix

| Variable | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|------------|------------|------------|------------|------------|
| AI_INDEX | 1.000000 | 0.783568 | 0.517254 | 0.840634 |
| LEGAL_WGI_SCORE | 0.783568 | 1.000000 | 0.664976 | 0.730088 |
| RES_INDEX | 0.517254 | 0.664976 | 1.000000 | 0.380787 |
| PQC | 0.840634 | 0.730088 | 0.380787 | 1.000000 |

---

# 10. Distribution Diagnostics

```text
AI_INDEX
Skewness = -0.39593851843313316
Kurtosis = -0.9132445811266638

LEGAL_WGI_SCORE
Skewness = 0.18383490244953005
Kurtosis = -0.8925871305381747

RES_INDEX
Skewness = 0.7807954023495343
Kurtosis = 0.49864057599433886

PQC
Skewness = -0.4431250138665039
Kurtosis = -1.0068022159176826
```

---

# 11. Sampling Adequacy and Factorability

```text
KMO = 0.7355868518654463

Chi-square = 249.83379389196242

p-value = 4.450885068086372e-51
```

The KMO statistic indicates acceptable sampling adequacy, while Bartlett's Test strongly rejects the null hypothesis of an identity correlation matrix, supporting PCA applicability.

---

# 12. PCA Eigenvalue Structure

```text
[0.74561879 0.17028181 0.04806765 0.03603175]

Total Variance Explained

0.9999999999999999
```

---

# 13. PCA Loading Matrix

| Variable | PC1 | PC2 | PC3 | PC4 |
|------------|------------|------------|------------|------------|
| AI_INDEX | 0.534197 | -0.272778 | -0.351497 | 0.718802 |
| LEGAL_WGI_SCORE | 0.536276 | 0.105185 | 0.835959 | 0.050156 |
| RES_INDEX | 0.416053 | 0.816887 | -0.359197 | -0.174850 |
| PQC | 0.503926 | -0.497216 | -0.220453 | -0.670996 |

---

# 14. PCA-Derived Weights

```text
AI_INDEX          0.26837950
LEGAL_WGI_SCORE   0.26942446
RES_INDEX         0.20902441
PQC               0.25317163
```

---

# 15. CRITIC Weights

| Variable | CRITIC Weight |
|------------|------------|
| AI_INDEX | 0.241936 |
| LEGAL_WGI_SCORE | 0.210281 |
| RES_INDEX | 0.227146 |
| PQC | 0.320637 |

---

# 16. Entropy Weights

| Variable | Entropy Weight |
|------------|------------|
| AI_INDEX | 0.290727 |
| LEGAL_WGI_SCORE | 0.234477 |
| RES_INDEX | 0.155500 |
| PQC | 0.319295 |

---

# 17. Weight Robustness Assessment

```text
Equal vs PCA

Spearman rho = 0.9992427048606825
p-value      = 7.153803172038685e-126

PCA vs Entropy

Spearman rho = 0.9972671523233321
p-value      = 2.290322902718063e-101

CRITIC vs PCA

Spearman rho = 0.998304317405441
p-value      = 1.776061187692281e-110
```

The ranking structure remains highly stable across alternative weighting methodologies.

---

# 18. QSSI 2026 Top 20 Countries

```text
Rank  Country                    QSSI

1     Denmark                  0.883898
2     Norway                   0.854815
3     Singapore                0.846803
4     United States            0.826602
5     Australia                0.822180
6     Germany                  0.819843
7     Finland                  0.814612
8     Ireland                  0.805977
9     Canada                   0.804139
10    Luxembourg               0.798930
11    France                   0.779162
12    Sweden                   0.775481
13    Japan                    0.769431
14    Belgium                  0.762393
15    Switzerland              0.761517
16    Austria                  0.755492
17    United Kingdom           0.749018
18    United Arab Emirates     0.747201
19    Spain                    0.745928
20    Iceland                  0.728642
```

---

# 19. QSSI 2026 Bottom 20 Countries

```text
Rank  Country                    QSSI

71    Antigua and Barbuda      0.351695
72    Bosnia and Herzegovina   0.342012
73    Maldives                 0.339315
74    Uganda                   0.332203
75    Burkina Faso             0.315858
76    Cambodia                 0.303576
77    Angola                   0.278110
78    Guatemala                0.255819
79    Myanmar                  0.247054
80    Chad                     0.239890
81    Honduras                 0.230823
82    Nicaragua                0.220457
83    Iraq                     0.220278
84    Guinea                   0.219293
85    Libya                    0.213475
86    Zimbabwe                 0.213106
87    Mali                     0.192921
88    Burundi                  0.150303
89    Liberia                  0.141950
90    Haiti                    0.098629
```

---

# 20. Reproducibility Audit

```text
Timestamp

2026-06-05T16:11:24.057391

Python Version

3.12.13

Platform

Linux-6.6.122+-x86_64-with-glibc2.35

Countries = 90

Final N = 90
```

---

# 21. SHA-256 Reproducibility Registry

| File | SHA256 |
|------------|------------|
| AI_INDEX_2026_v1_MC_Canon.csv | 16656947ff8486b896640a00d05deccee086e52358f6614472ad38929af0b776 |
| LEGAL_WGI_2026_v1_MC_Canon.csv | 13e5310373fc4104b70b0eb410ccb1628099336f21fe705545b472290cc7b4e7 |
| RES_INDEX_2026_MC_Canon.csv | 4e936fa81a2fa2d491b897313ac136d38af431cb72f55b3adb85006bded88c9d |
| PQC_NCSI_2026_MC_Canon.csv | a421685fedadd3fb3b0b9ffbdb3822401ea4ab98098853b104f54397631cda8d |
| QSSI_MASTER_DATASET.csv | 6ac531236999faa3680978cbe09eb8c93e9ebc85e1881f937d257f873b727931 |
| QSSI_RANKINGS_2026.csv | 56681c6fcc4c89a89982b9e117beedde76f02ef4c1c473bd86079e66542d8215 |

---

# 22. Repository Source Archive

```text
AI_INDEX_2026_v1_MC_Canon.csv
LEGAL_WGI_2026_v1_MC_Canon.csv
RES_INDEX_2026_MC_Canon.csv
PQC_NCSI_2026_MC_Canon.csv
QSSI_MASTER_DATASET.csv
QSSI_RANKINGS_2026.csv

Source Archive

2025-Government-AI-Readiness-Index-Report_01_26.pdf

2025_wjp_rule_of_law_index_HISTORICAL_DATA_FILE.xlsx

dataset_2026-04-29T12_08_28.599500883Z_DEFAULT_INTEGRATION_IMF.STA_NDGAIN_1.0.1.csv

qssi_raw_sources_v2026.1.csv

wgicalculator-2025.xlsx
```

---

# 23. Methodological Conclusion

The QSSI 2026 framework produced a fully harmonized cross-national dataset comprising 90 countries and four canonical dimensions. Complete-case harmonization eliminated all missing observations, PCA diagnostics confirmed factorability, and robustness analyses demonstrated near-perfect rank-order stability across Equal Weighting, PCA, Entropy, and CRITIC weighting schemes. The resulting rankings constitute a reproducible, auditable, and statistically validated global assessment generated under the FAIR+D Canon™ methodological framework.

---

### Citation

Current Edition DOI

10.5281/zenodo.20385492

All Versions DOI

10.5281/zenodo.17302169

ORCID

https://orcid.org/0009-0007-5615-3558
