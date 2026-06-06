# QSSI™ — QUANTUM SOVEREIGN STRENGTH INDEX 2026
## Provenance Statement, Data Lineage, Coverage Audit, Statistical Validation & Reproducibility Record

**Current Canonical Edition DOI:** 10.5281/zenodo.20385492  
**Version Archive DOI (All Editions):** 10.5281/zenodo.17302169  
**ORCID:** https://orcid.org/0009-0007-5615-3558

---

# 1. DATA PROVENANCE SUMMARY

| Dataset | Initial Coverage |
|----------|----------:|
| AI_INDEX | 195 |
| LEGAL_WGI_SCORE | 213 |
| RES_INDEX | 181 |
| PQC | 124 |

---

# 2. CROSS-DATASET INTERSECTION MATRIX

| Variable | AI | LEGAL | RES | PQC |
|----------|----------:|----------:|----------:|----------:|
| AI | 195 | 172 | 128 | 118 |
| LEGAL | 172 | 213 | 136 | 117 |
| RES | 128 | 136 | 181 | 94 |
| PQC | 118 | 117 | 94 | 124 |

---

# 3. HARMONIZATION RESULTS

| Metric | Value |
|----------|----------:|
| Countries Included | 90 |
| Countries Excluded Due to PQC Coverage Constraints | 36 |
| Definitive Final N | 90 |

---

# 4. FINAL HARMONIZED VARIABLES

| Variable | Coverage |
|----------|----------:|
| AI_INDEX | 90 |
| LEGAL_WGI_SCORE | 90 |
| RES_INDEX | 90 |
| PQC | 90 |

---

# 5. COUNTRY COVERAGE

## Included Countries (N = 90)

### First Five Countries

| Index | Country |
|----------|----------|
| 0 | Albania |
| 1 | Algeria |
| 2 | Angola |
| 3 | Antigua and Barbuda |
| 4 | Argentina |

### Last Five Countries

| Index | Country |
|----------|----------|
| 85 | United Arab Emirates |
| 86 | United Kingdom |
| 87 | United States |
| 88 | Uruguay |
| 89 | Zimbabwe |

---

# 6. DATA INTEGRITY VERIFICATION

Dataset Shape:

```text
(90, 5)
```

Missing Values Audit:

| Variable | Missing Values |
|----------|----------:|
| country | 0 |
| AI_INDEX | 0 |
| LEGAL_WGI_SCORE | 0 |
| RES_INDEX | 0 |
| PQC | 0 |

### Integrity Result

```text
No missing observations remain after harmonization and canonical filtering.
```

---

# 7. NORMALIZATION VERIFICATION

Sample Records

| Country | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|----------|----------:|----------:|----------:|----------:|
| Albania | 0.446322 | 0.487651 | 0.270189 | 0.955820 |
| Algeria | 0.449950 | 0.358597 | 0.275554 | 0.345157 |
| Angola | 0.227441 | 0.297740 | 0.300972 | 0.292056 |
| Antigua and Barbuda | 0.204852 | 0.607289 | 0.454614 | 0.150382 |
| Argentina | 0.700634 | 0.455790 | 0.348677 | 0.575191 |

---

# 8. DESCRIPTIVE STATISTICS

| Statistic | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|----------|----------:|----------:|----------:|----------:|
| Count | 90.0 | 90.0 | 90.0 | 90.0 |
| Mean | 0.566620 | 0.540517 | 0.394125 | 0.595676 |
| Std | 0.250973 | 0.228008 | 0.140781 | 0.272357 |
| Min | 0.050407 | 0.108866 | 0.150195 | 0.000000 |
| 25% | 0.393117 | 0.359012 | 0.298129 | 0.376115 |
| 50% | 0.633618 | 0.504046 | 0.371685 | 0.641621 |
| 75% | 0.766077 | 0.697156 | 0.459482 | 0.827448 |
| Max | 1.000000 | 0.966323 | 0.808925 | 0.982370 |

---

# 9. CORRELATION MATRIX

| Variable | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|----------|----------:|----------:|----------:|----------:|
| AI_INDEX | 1.000000 | 0.783568 | 0.517254 | 0.840634 |
| LEGAL_WGI_SCORE | 0.783568 | 1.000000 | 0.664976 | 0.730088 |
| RES_INDEX | 0.517254 | 0.664976 | 1.000000 | 0.380787 |
| PQC | 0.840634 | 0.730088 | 0.380787 | 1.000000 |

---

# 10. DISTRIBUTIONAL DIAGNOSTICS

| Variable | Skewness | Kurtosis |
|----------|----------:|----------:|
| AI_INDEX | -0.395939 | -0.913245 |
| LEGAL_WGI_SCORE | 0.183835 | -0.892587 |
| RES_INDEX | 0.780795 | 0.498641 |
| PQC | -0.443125 | -1.006802 |

---

# 11. PCA VALIDATION

## Explained Variance Ratio

```text
[0.74561879, 0.17028181, 0.04806765, 0.03603175]
```

Variance Sum:

```text
0.9999999999999999
```

---

# 12. FACTOR ADEQUACY TESTS

## Kaiser–Meyer–Olkin (KMO)

```text
KMO = 0.7355868518654463
```

## Bartlett's Test of Sphericity

```text
Chi-square = 249.83379389196242
p-value = 4.450885068086372e-51
```

---

# 13. INTERNAL CONSISTENCY

## Cronbach's Alpha

```text
0.8785685555594794
```

95% Confidence Interval

```text
[0.832, 0.915]
```

---

# 14. PCA COMPONENT LOADINGS

| Variable | PC1 | PC2 | PC3 | PC4 |
|----------|----------:|----------:|----------:|----------:|
| AI_INDEX | 0.534197 | -0.272778 | -0.351497 | 0.718802 |
| LEGAL_WGI_SCORE | 0.536276 | 0.105185 | 0.835959 | 0.050156 |
| RES_INDEX | 0.416053 | 0.816887 | -0.359197 | -0.174850 |
| PQC | 0.503926 | -0.497216 | -0.220453 | -0.670996 |

---

# 15. PCA-DERIVED WEIGHTS

| Variable | Weight |
|----------|----------:|
| AI_INDEX | 0.26837950 |
| LEGAL_WGI_SCORE | 0.26942446 |
| RES_INDEX | 0.20902441 |
| PQC | 0.25317163 |

---

# 16. CRITIC WEIGHTS

| Variable | CRITIC Weight |
|----------|----------:|
| AI_INDEX | 0.241936 |
| LEGAL_WGI_SCORE | 0.210281 |
| RES_INDEX | 0.227146 |
| PQC | 0.320637 |

---

# 17. ENTROPY WEIGHTS

| Variable | Entropy Weight |
|----------|----------:|
| AI_INDEX | 0.290727 |
| LEGAL_WGI_SCORE | 0.234477 |
| RES_INDEX | 0.155500 |
| PQC | 0.319295 |

---

# 18. WEIGHTING ROBUSTNESS ANALYSIS

Equal Weight vs PCA

```text
Spearman ρ = 0.9992427048606825
p-value = 7.153803172038685e-126
```

PCA vs Entropy

```text
Spearman ρ = 0.9972671523233321
p-value = 2.290322902718063e-101
```

Additional Robustness Verification

```text
Spearman ρ = 0.998304317405441
p-value = 1.776061187692281e-110
```

---

# 19. TOP 20 COUNTRIES

| Rank | Country | QSSI |
|----------:|----------|----------:|
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

# 20. BOTTOM 20 COUNTRIES

| Rank | Country | QSSI |
|----------:|----------|----------:|
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

# 21. FINAL TOP 10

| Rank | Country | QSSI |
|----------:|----------|----------:|
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

# 22. FINAL BOTTOM 10

| Rank | Country | QSSI |
|----------:|----------|----------:|
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

# 23. REPRODUCIBILITY METADATA

| Field | Value |
|----------|----------|
| Timestamp | 2026-06-05T16:11:24.057391 |
| Python Version | 3.12.13 |
| Platform | Linux-6.6.122+-x86_64-with-glibc2.35 |
| Countries | 90 |
| Final N | 90 |

---

# 24. FILE HASH AUDIT (SHA-256)

| File | SHA256 |
|----------|----------|
| AI_INDEX_2026_v1_MC_Canon.csv | 16656947ff8486b896640a00d05deccee086e52358f6614472ad38929af0b776 |
| LEGAL_WGI_2026_v1_MC_Canon.csv | 13e5310373fc4104b70b0eb410ccb1628099336f21fe705545b472290cc7b4e7 |
| RES_INDEX_2026_MC_Canon.csv | 4e936fa81a2fa2d491b897313ac136d38af431cb72f55b3adb85006bded88c9d |
| PQC_NCSI_2026_MC_Canon.csv | a421685fedadd3fb3b0b9ffbdb3822401ea4ab98098853b104f54397631cda8d |
| QSSI_MASTER_DATASET.csv | 6ac531236999faa3680978cbe09eb8c93e9ebc85e1881f937d257f873b727931 |
| QSSI_RANKINGS_2026.csv | 56681c6fcc4c89a89982b9e117beedde76f02ef4c1c473bd86079e66542d8215 |

---

# 25. GENERATED OUTPUTS

```text
QSSI_MASTER_DATASET.csv
QSSI_RANKINGS_2026.csv
QSSI_CRITIC_WEIGHTS.csv
QSSI_ENTROPY_WEIGHTS.csv
QSSI_SHA256_AUDIT.csv
QSSI_FINAL_AUDIT.json
reports/provenance_statement.md
```

---

# 26. CANONICAL AUDIT CONCLUSION

```text
FINAL N = 90
COUNTRIES = 90
MISSING = 0

AI Coverage = 195
LEGAL Coverage = 213
RES Coverage = 181
PQC Coverage = 124

Countries Excluded Due To PQC Coverage = 36

KMO = 0.7355868518654463
Bartlett p-value = 4.450885068086372e-51

Cronbach Alpha = 0.8785685555594794

PCA Variance Explained = 74.561879%

Equal vs PCA Spearman = 0.9992427048606825
PCA vs Entropy Spearman = 0.9972671523233321

Data Integrity Status = VERIFIED
Normalization Status = VERIFIED
Weight Robustness Status = VERIFIED
Statistical Adequacy Status = VERIFIED
Reproducibility Status = VERIFIED
Hash Audit Status = VERIFIED

QSSI 2026 FINAL CANONICAL DATASET:
90 COUNTRIES
0 MISSING OBSERVATIONS
FULLY HARMONIZED
FULLY REPRODUCIBLE
SHA-256 AUDITED
```
