# QSSI™ — Quantum Sovereignty & Security Index 2026
## Framework Definition, Harmonization Protocol, Statistical Validation, and Final Audit Record

---

### Citation Information

**Current Edition DOI:** 10.5281/zenodo.20385492

**Canonical DOI (All Versions):** 10.5281/zenodo.17302169

**ORCID:** https://orcid.org/0009-0007-5615-3558

---

# 1. Framework Overview

The Quantum Sovereignty & Security Index (QSSI™) is a composite sovereign-capability assessment framework integrating four harmonized dimensions:

| Dimension | Variable |
|------------|------------|
| Artificial Intelligence Capability | AI_INDEX |
| Legal & Governance Readiness | LEGAL_WGI_SCORE |
| Research & Scientific Capacity | RES_INDEX |
| Post-Quantum Cybersecurity Readiness | PQC |

The framework measures national preparedness for the emerging quantum-era strategic environment through a statistically validated multi-domain architecture.

---

# 2. Source Coverage

| Variable | Raw Coverage |
|-----------|------------:|
| AI_INDEX | 195 |
| LEGAL_WGI_SCORE | 213 |
| RES_INDEX | 181 |
| PQC | 124 |

---

# 3. Pairwise Coverage Matrix

| | AI | LEGAL | RES | PQC |
|---|---:|---:|---:|---:|
| AI | 195 | 172 | 128 | 118 |
| LEGAL | 172 | 213 | 136 | 117 |
| RES | 128 | 136 | 181 | 94 |
| PQC | 118 | 117 | 94 | 124 |

---

# 4. Harmonization & Canonical Filtering

Countries lacking complete PQC coverage were excluded from the final canonical sample.

| Metric | Value |
|----------|------:|
| Countries after harmonization | 90 |
| Excluded due to PQC coverage | 36 |
| Definitive Final N | 90 |

---

# 5. Final Harmonized Variables

| Variable | Coverage |
|-----------|---------:|
| AI_INDEX | 90 |
| LEGAL_WGI_SCORE | 90 |
| RES_INDEX | 90 |
| PQC | 90 |

---

# 6. Data Integrity Verification

```text
Shape
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

Countries = 90

---

# 8. Principal Component Analysis

## Explained Variance Ratio

```text
[0.74561879 0.17028181 0.04806765 0.03603175]
```

Variance Sum

```text
0.9999999999999999
```

---

# 9. Sampling Adequacy & Factorability

## Kaiser-Meyer-Olkin (KMO)

```text
KMO = 0.7355868518654463
```

## Bartlett Test of Sphericity

```text
Chi-square = 249.83379389196242

p-value = 4.450885068086372e-51
```

Interpretation:

- KMO exceeds accepted adequacy threshold.
- Bartlett test strongly rejects the null hypothesis.
- Dataset is suitable for dimensional reduction and latent-factor extraction.

---

# 10. Descriptive Statistics

| Statistic | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|------------|---------:|---------:|---------:|---------:|
| Count | 90.0 | 90.0 | 90.0 | 90.0 |
| Mean | 0.566620 | 0.540517 | 0.394125 | 0.595676 |
| Std | 0.250973 | 0.228008 | 0.140781 | 0.272357 |
| Min | 0.050407 | 0.108866 | 0.150195 | 0.000000 |
| 25% | 0.393117 | 0.359012 | 0.298129 | 0.376115 |
| 50% | 0.633618 | 0.504046 | 0.371685 | 0.641621 |
| 75% | 0.766077 | 0.697156 | 0.459482 | 0.827448 |
| Max | 1.000000 | 0.966323 | 0.808925 | 0.982370 |

---

# 11. Correlation Matrix

| | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|---|---:|---:|---:|---:|
| AI_INDEX | 1.000000 | 0.783568 | 0.517254 | 0.840634 |
| LEGAL_WGI_SCORE | 0.783568 | 1.000000 | 0.664976 | 0.730088 |
| RES_INDEX | 0.517254 | 0.664976 | 1.000000 | 0.380787 |
| PQC | 0.840634 | 0.730088 | 0.380787 | 1.000000 |

---

# 12. Distribution Diagnostics

## AI_INDEX

```text
Skewness = -0.39593851843313316
Kurtosis = -0.9132445811266638
```

## LEGAL_WGI_SCORE

```text
Skewness = 0.18383490244953005
Kurtosis = -0.8925871305381747
```

## RES_INDEX

```text
Skewness = 0.7807954023495343
Kurtosis = 0.49864057599433886
```

## PQC

```text
Skewness = -0.4431250138665039
Kurtosis = -1.0068022159176826
```

---

# 13. Bootstrap Stability Assessment

```text
(np.float64(0.8785685555594794), array([0.832, 0.915]))
(np.float64(0.8785685555594794), array([0.832, 0.915]))
```

Result indicates strong ranking stability and robust reproducibility.

---

# 14. PCA Loadings

| Variable | PC1 | PC2 | PC3 | PC4 |
|-----------|---------:|---------:|---------:|---------:|
| AI_INDEX | 0.534197 | -0.272778 | -0.351497 | 0.718802 |
| LEGAL_WGI_SCORE | 0.536276 | 0.105185 | 0.835959 | 0.050156 |
| RES_INDEX | 0.416053 | 0.816887 | -0.359197 | -0.174850 |
| PQC | 0.503926 | -0.497216 | -0.220453 | -0.670996 |

---

# 15. Variable Retention

```text
AI_INDEX           1.0
LEGAL_WGI_SCORE    1.0
RES_INDEX          1.0
PQC                1.0
dtype: float64
```

All variables retained.

---

# 16. PCA-Derived Weights

| Variable | PCA Weight |
|-----------|----------:|
| AI_INDEX | 0.26837950 |
| LEGAL_WGI_SCORE | 0.26942446 |
| RES_INDEX | 0.20902441 |
| PQC | 0.25317163 |

---

# 17. CRITIC Weights

| Variable | CRITIC Weight |
|-----------|-------------:|
| AI_INDEX | 0.241936 |
| LEGAL_WGI_SCORE | 0.210281 |
| RES_INDEX | 0.227146 |
| PQC | 0.320637 |

Saved:

```text
QSSI_CRITIC_WEIGHTS.csv
```

---

# 18. Entropy Weights

| Variable | Entropy Weight |
|-----------|--------------:|
| AI_INDEX | 0.290727 |
| LEGAL_WGI_SCORE | 0.234477 |
| RES_INDEX | 0.155500 |
| PQC | 0.319295 |

Saved:

```text
QSSI_ENTROPY_WEIGHTS.csv
```

---

# 19. Ranking Robustness

## Equal Weight vs PCA

```text
SignificanceResult(
statistic = 0.9992427048606825,
pvalue = 7.153803172038685e-126
)
```

## PCA vs Entropy

```text
SignificanceResult(
statistic = 0.9972671523233321,
pvalue = 2.290322902718063e-101
)
```

## Additional Robustness Check

```text
SignificanceResult(
statistic = 0.998304317405441,
pvalue = 1.776061187692281e-110
)
```

Result demonstrates near-perfect rank-order stability across weighting methodologies.

---

# 20. Top 20 Countries

| Rank | Country | QSSI |
|------:|-----------|---------:|
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

# 21. Bottom 20 Countries

| Rank | Country | QSSI |
|------:|-----------|---------:|
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

# 22. Top 10

| Rank | Country | QSSI |
|------:|-----------|---------:|
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

# 23. Bottom 10

| Rank | Country | QSSI |
|------:|-----------|---------:|
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

# 24. Reproducibility Metadata

```text
timestamp:
2026-06-05T16:11:24.057391

python_version:
3.12.13 (main, Mar 4 2026, 09:23:07) [GCC 11.4.0]

platform:
Linux-6.6.122+-x86_64-with-glibc2.35

countries:
90

final_N:
90
```

Saved:

```text
QSSI_FINAL_AUDIT.json
```

---

# 25. Cryptographic Audit Trail

| File | SHA256 |
|--------|--------|
| AI_INDEX_2026_v1_MC_Canon.csv | 16656947ff8486b896640a00d05deccee086e52358f6614472ad38929af0b776 |
| LEGAL_WGI_2026_v1_MC_Canon.csv | 13e5310373fc4104b70b0eb410ccb1628099336f21fe705545b472290cc7b4e7 |
| RES_INDEX_2026_MC_Canon.csv | 4e936fa81a2fa2d491b897313ac136d38af431cb72f55b3adb85006bded88c9d |
| PQC_NCSI_2026_MC_Canon.csv | a421685fedadd3fb3b0b9ffbdb3822401ea4ab98098853b104f54397631cda8d |
| QSSI_MASTER_DATASET.csv | 6ac531236999faa3680978cbe09eb8c93e9ebc85e1881f937d257f873b727931 |
| QSSI_RANKINGS_2026.csv | 56681c6fcc4c89a89982b9e117beedde76f02ef4c1c473bd86079e66542d8215 |

Saved:

```text
QSSI_SHA256_AUDIT.csv
```

---

# 26. Final Audit Summary

| Metric | Value |
|----------|------:|
| AI Coverage | 195 |
| LEGAL Coverage | 213 |
| RES Coverage | 181 |
| PQC Coverage | 124 |
| Countries Excluded | 36 |
| Final Countries | 90 |
| Missing Values | 0 |
| KMO | 0.7355868518654463 |
| Bartlett Chi-Square | 249.83379389196242 |
| Bartlett p-value | 4.450885068086372e-51 |
| Rank Stability (Equal vs PCA) | 0.9992427048606825 |
| Rank Stability (PCA vs Entropy) | 0.9972671523233321 |

---

# Definitive Canonical Result

```text
FINAL N = 90
COUNTRIES = 90
MISSING = 0
```

The QSSI™ 2026 canonical dataset contains 90 fully harmonized sovereign observations with complete coverage across AI capability, legal-governance readiness, research capacity, and post-quantum cybersecurity preparedness. Statistical diagnostics, robustness testing, weighting sensitivity analyses, and cryptographic audit verification confirm full reproducibility of the published results.
