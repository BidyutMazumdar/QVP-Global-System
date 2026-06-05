# QSSI 2026 Frequently Asked Questions (FAQ)

## FAIR+D Canon™ Global Framework

### Current Edition DOI
10.5281/zenodo.20385492

### All Versions DOI
10.5281/zenodo.17302169

### Author
Dr. B. Mazumdar

ORCID:
https://orcid.org/0009-0007-5615-3558

---

## 1. What is QSSI 2026?

QSSI (Quantum-Safe Sovereignty Index) 2026 is a composite cross-national benchmarking framework designed to evaluate sovereign preparedness across Artificial Intelligence (AI), Legal-Governance Capacity, National Resilience, and Post-Quantum Cybersecurity (PQC) readiness.

The framework integrates internationally recognized datasets into a standardized, reproducible, and auditable measurement architecture.

---

## 2. What indicators are included in QSSI 2026?

QSSI 2026 consists of four core dimensions:

| Dimension | Records |
|------------|---------:|
| AI_INDEX | 195 |
| LEGAL_WGI_SCORE | 213 |
| RES_INDEX | 181 |
| PQC | 124 |

---

## 3. What was the final country coverage?

| Metric | Value |
|----------|------:|
| Countries Initially Considered | 90 |
| Countries Excluded Due to PQC Coverage Limitations | 36 |
| Definitive Final N | 90 |
| Final Countries Included | 90 |

Dataset Shape:

```text
(90, 5)
```

Variables:

```text
country
AI_INDEX
LEGAL_WGI_SCORE
RES_INDEX
PQC
```

---

## 4. Were there any missing values?

No.

```text
country              0
AI_INDEX             0
LEGAL_WGI_SCORE      0
RES_INDEX            0
PQC                  0
dtype: int64
```

Total Missing Values:

```text
0
```

---

## 5. Which countries were included?

First Countries:

```text
Albania
Algeria
Angola
Antigua and Barbuda
Argentina
```

Last Countries:

```text
United Arab Emirates
United Kingdom
United States
Uruguay
Zimbabwe
```

Total Countries:

```text
90
```

---

## 6. What overlap existed among the source datasets?

```csv
Variable,AI,LEGAL,RES,PQC
AI,195,172,128,118
LEGAL,172,213,136,117
RES,128,136,181,94
PQC,118,117,94,124
```

---

## 7. What were the PCA explained variance ratios?

```csv
PC,Explained_Variance
PC1,0.74561879
PC2,0.17028181
PC3,0.04806765
PC4,0.03603175
```

Total Variance Explained:

```text
0.9999999999999999
```

---

## 8. Was the dataset suitable for factor analysis?

Yes.

### Kaiser-Meyer-Olkin (KMO)

```text
0.7355868518654463
```

### Bartlett's Test of Sphericity

```text
Chi-square = 249.83379389196242
p-value = 4.450885068086372e-51
```

---

## 9. What are the descriptive statistics?

```csv
Variable,Count,Mean,Std,Min,25%,50%,75%,Max
AI_INDEX,90,0.566620,0.250973,0.050407,0.393117,0.633618,0.766077,1.000000
LEGAL_WGI_SCORE,90,0.540517,0.228008,0.108866,0.359012,0.504046,0.697156,0.966323
RES_INDEX,90,0.394125,0.140781,0.150195,0.298129,0.371685,0.459482,0.808925
PQC,90,0.595676,0.272357,0.000000,0.376115,0.641621,0.827448,0.982370
```

---

## 10. What were the correlations among variables?

```csv
Variable,AI_INDEX,LEGAL_WGI_SCORE,RES_INDEX,PQC
AI_INDEX,1.000000,0.783568,0.517254,0.840634
LEGAL_WGI_SCORE,0.783568,1.000000,0.664976,0.730088
RES_INDEX,0.517254,0.664976,1.000000,0.380787
PQC,0.840634,0.730088,0.380787,1.000000
```

---

## 11. What were the skewness and kurtosis values?

### AI_INDEX

```text
Skewness = -0.39593851843313316
Kurtosis = -0.9132445811266638
```

### LEGAL_WGI_SCORE

```text
Skewness = 0.18383490244953005
Kurtosis = -0.8925871305381747
```

### RES_INDEX

```text
Skewness = 0.7807954023495343
Kurtosis = 0.49864057599433886
```

### PQC

```text
Skewness = -0.4431250138665039
Kurtosis = -1.0068022159176826
```

---

## 12. What was the reliability score?

```text
Cronbach Alpha = 0.8785685555594794
95% CI = [0.832, 0.915]
```

---

## 13. What were the PCA loadings?

```csv
Variable,PC1,PC2,PC3,PC4
AI_INDEX,0.534197,-0.272778,-0.351497,0.718802
LEGAL_WGI_SCORE,0.536276,0.105185,0.835959,0.050156
RES_INDEX,0.416053,0.816887,-0.359197,-0.174850
PQC,0.503926,-0.497216,-0.220453,-0.670996
```

---

## 14. What were the PCA-derived weights?

```csv
Variable,PCA_Weight
AI_INDEX,0.26837950
LEGAL_WGI_SCORE,0.26942446
RES_INDEX,0.20902441
PQC,0.25317163
```

---

## 15. What were the CRITIC weights?

```csv
Variable,CRITIC_Weight
AI_INDEX,0.241936
LEGAL_WGI_SCORE,0.210281
RES_INDEX,0.227146
PQC,0.320637
```

---

## 16. What were the Entropy weights?

```csv
Variable,Entropy_Weight
AI_INDEX,0.290727
LEGAL_WGI_SCORE,0.234477
RES_INDEX,0.155500
PQC,0.319295
```

---

## 17. Who ranked in the Top 20?

```csv
Rank,Country,QSSI
1,Denmark,0.883898
2,Norway,0.854815
3,Singapore,0.846803
4,United States,0.826602
5,Australia,0.822180
6,Germany,0.819843
7,Finland,0.814612
8,Ireland,0.805977
9,Canada,0.804139
10,Luxembourg,0.798930
11,France,0.779162
12,Sweden,0.775481
13,Japan,0.769431
14,Belgium,0.762393
15,Switzerland,0.761517
16,Austria,0.755492
17,United Kingdom,0.749018
18,United Arab Emirates,0.747201
19,Spain,0.745928
20,Iceland,0.728642
```

---

## 18. Who ranked in the Bottom 20?

```csv
Rank,Country,QSSI
71,Antigua and Barbuda,0.351695
72,Bosnia and Herzegovina,0.342012
73,Maldives,0.339315
74,Uganda,0.332203
75,Burkina Faso,0.315858
76,Cambodia,0.303576
77,Angola,0.278110
78,Guatemala,0.255819
79,Myanmar,0.247054
80,Chad,0.239890
81,Honduras,0.230823
82,Nicaragua,0.220457
83,Iraq,0.220278
84,Guinea,0.219293
85,Libya,0.213475
86,Zimbabwe,0.213106
87,Mali,0.192921
88,Burundi,0.150303
89,Liberia,0.141950
90,Haiti,0.098629
```

---

## 19. What were the Top 10 countries?

```csv
Rank,Country,QSSI
1,Denmark,0.883898
2,Norway,0.854815
3,Singapore,0.846803
4,United States,0.826602
5,Australia,0.822180
6,Germany,0.819843
7,Finland,0.814612
8,Ireland,0.805977
9,Canada,0.804139
10,Luxembourg,0.798930
```

---

## 20. What were the Bottom 10 countries?

```csv
Rank,Country,QSSI
81,Honduras,0.230823
82,Nicaragua,0.220457
83,Iraq,0.220278
84,Guinea,0.219293
85,Libya,0.213475
86,Zimbabwe,0.213106
87,Mali,0.192921
88,Burundi,0.150303
89,Liberia,0.141950
90,Haiti,0.098629
```

---

## 21. How robust were alternative weighting methods?

### Equal vs PCA

```text
Spearman Correlation = 0.9992427048606825
p-value = 7.153803172038685e-126
```

### PCA vs Entropy

```text
Spearman Correlation = 0.9972671523233321
p-value = 2.290322902718063e-101
```

### Additional Robustness Validation

```text
Spearman Correlation = 0.998304317405441
p-value = 1.776061187692281e-110
```

---

## 22. What audit metadata were recorded?

```csv
Field,Value
timestamp,2026-06-05T16:11:24.057391
python_version,"3.12.13 (main, Mar 4 2026, 09:23:07) [GCC 11.4.0]"
platform,Linux-6.6.122+-x86_64-with-glibc2.35
countries,90
final_N,90
```

---

## 23. What files were generated?

```csv
File
AI_INDEX_2026_v1_MC_Canon.csv
LEGAL_WGI_2026_v1_MC_Canon.csv
RES_INDEX_2026_MC_Canon.csv
PQC_NCSI_2026_MC_Canon.csv
QSSI_MASTER_DATASET.csv
QSSI_RANKINGS_2026.csv
QSSI_FINAL_AUDIT.json
QSSI_SHA256_AUDIT.csv
QSSI_CRITIC_WEIGHTS.csv
QSSI_ENTROPY_WEIGHTS.csv
```

---

## 24. What are the SHA256 verification hashes?

```csv
File,SHA256
AI_INDEX_2026_v1_MC_Canon.csv,16656947ff8486b896640a00d05deccee086e52358f6614472ad38929af0b776
LEGAL_WGI_2026_v1_MC_Canon.csv,13e5310373fc4104b70b0eb410ccb1628099336f21fe705545b472290cc7b4e7
RES_INDEX_2026_MC_Canon.csv,4e936fa81a2fa2d491b897313ac136d38af431cb72f55b3adb85006bded88c9d
PQC_NCSI_2026_MC_Canon.csv,a421685fedadd3fb3b0b9ffbdb3822401ea4ab98098853b104f54397631cda8d
QSSI_MASTER_DATASET.csv,6ac531236999faa3680978cbe09eb8c93e9ebc85e1881f937d257f873b727931
QSSI_RANKINGS_2026.csv,56681c6fcc4c89a89982b9e117beedde76f02ef4c1c473bd86079e66542d8215
```

---

## 25. How should QSSI 2026 be cited?

### Current Edition DOI

```text
10.5281/zenodo.20385492
```

### Concept DOI (All Versions)

```text
10.5281/zenodo.17302169
```

Recommended Citation:

```text
Mazumdar, B. (2026).
QSSI 2026: Quantum-Safe Sovereignty Index.
FAIR+D Canon™ Global Framework.
Current Edition DOI: 10.5281/zenodo.20385492

All Versions DOI:
10.5281/zenodo.17302169

ORCID:
https://orcid.org/0009-0007-5615-3558
```

---

## Version Information

```text
Framework:
FAIR+D Canon™ Global Framework

Edition:
QSSI 2026

Current DOI:
10.5281/zenodo.20385492

All Versions DOI:
10.5281/zenodo.17302169

Author:
Dr. B. Mazumdar

ORCID:
https://orcid.org/0009-0007-5615-3558

Countries:
90

Final N:
90

Missing Values:
0

Status:
Audited Release
```
