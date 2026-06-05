# QSSI 2026: A Composite Framework for Quantifying Sovereign Strategic Intelligence

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

## Abstract

This study presents the Quantified Sovereign Strategic Intelligence Index (QSSI) 2026, a multidimensional composite framework designed to evaluate sovereign strategic capacity through the integration of artificial intelligence readiness, institutional quality, resilience capability, and public-sector digital maturity. The framework applies a transparent FAIR+D Canon™ methodology combining canonical harmonization, complete-case filtering, normalization, principal component analysis, and composite score aggregation.

The analytical dataset integrates four globally recognized dimensions covering 195 AI observations, 213 governance observations, 181 resilience observations, and 124 public-sector digital capability observations. After harmonization and complete-case filtering, a final balanced sample of 90 countries was obtained.

Statistical validation demonstrates strong construct coherence, satisfactory factorability, high internal consistency, and robustness across alternative weighting schemes. The resulting QSSI scores provide a reproducible empirical basis for comparative assessment of sovereign strategic intelligence capacity across countries.

---

## 1. Introduction

Governments increasingly operate within environments characterized by technological acceleration, geopolitical uncertainty, climate-related risks, cybersecurity challenges, and institutional complexity. Strategic state capacity therefore depends not only upon governance quality but also upon the ability to integrate technological readiness, resilience capability, and public-sector digital transformation.

QSSI 2026 was developed to provide a unified quantitative framework capable of capturing these complementary dimensions within a single composite indicator.

The framework integrates four domains:

| Dimension | Description |
|------------|-------------|
| AI_INDEX | National artificial intelligence readiness |
| LEGAL_WGI_SCORE | Institutional and governance quality |
| RES_INDEX | Sovereign resilience capacity |
| PQC | Public-sector digital capability |

---

## 2. Data Sources

### AI Readiness

| Source |
|----------|
| AI_OECD_2026.csv |
| AI_OXFORD_2026.csv |
| AI_INDEX_2026_v1_MC_Canon.csv |

### Governance and Legal Capacity

| Source |
|----------|
| wjp_clean.csv |
| wgicalculator-2025.xlsx |
| LEGAL_WGI_2026_v1_MC_Canon.csv |

### Resilience Capacity

| Source |
|----------|
| RES_IMF_2026.csv |
| RES_NDGAIN_2026_FINAL.csv |
| RES_GLOBAL_RESILIENCE_INDEX_v1.0_STRICT.csv |
| RES_INDEX_2026_MC_Canon.csv |

### Public Capability and Digital Readiness

| Source |
|----------|
| PQC_NCSI_2026_MC_Canon.csv |

---

## 3. Coverage Analysis

### Raw Coverage

| Variable | Coverage |
|-----------|---------:|
| AI_INDEX | 195 |
| LEGAL_WGI_SCORE | 213 |
| RES_INDEX | 181 |
| PQC | 124 |

### Pairwise Coverage Matrix

| Variable | AI | LEGAL | RES | PQC |
|-----------|----:|------:|----:|----:|
| AI | 195 | 172 | 128 | 118 |
| LEGAL | 172 | 213 | 136 | 117 |
| RES | 128 | 136 | 181 | 94 |
| PQC | 118 | 117 | 94 | 124 |

---

## 4. Canonical Harmonization

All source datasets were harmonized using standardized sovereign identifiers and canonical country matching procedures.

### Harmonization Outcome

| Metric | Value |
|----------|------:|
| AI Coverage | 195 |
| LEGAL Coverage | 213 |
| RES Coverage | 181 |
| PQC Coverage | 124 |
| Excluded due to PQC coverage | 36 |
| Final Analytical Sample | 90 |

### Final Harmonized Variables

| Variable | Coverage |
|-----------|---------:|
| AI_INDEX | 90 |
| LEGAL_WGI_SCORE | 90 |
| RES_INDEX | 90 |
| PQC | 90 |

---

## 5. Data Integrity Verification

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

## 6. Final Sample

### Included Countries (N = 90)

```text
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
```

---

## 7. Normalization

All indicators were transformed to a common [0,1] interval using monotonic min-max normalization.

### Sample Normalized Data

| Country | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|----------|----------:|----------------:|----------:|----:|
| Albania | 0.446322 | 0.487651 | 0.270189 | 0.955820 |
| Algeria | 0.449950 | 0.358597 | 0.275554 | 0.345157 |
| Angola | 0.227441 | 0.297740 | 0.300972 | 0.292056 |
| Antigua and Barbuda | 0.204852 | 0.607289 | 0.454614 | 0.150382 |
| Argentina | 0.700634 | 0.455790 | 0.348677 | 0.575191 |

---

## 8. Descriptive Statistics

| Variable | Mean | Std | Min | Median | Max |
|-----------|------:|------:|------:|------:|------:|
| AI_INDEX | 0.566620 | 0.250973 | 0.050407 | 0.633618 | 1.000000 |
| LEGAL_WGI_SCORE | 0.540517 | 0.228008 | 0.108866 | 0.504046 | 0.966323 |
| RES_INDEX | 0.394125 | 0.140781 | 0.150195 | 0.371685 | 0.808925 |
| PQC | 0.595676 | 0.272357 | 0.000000 | 0.641621 | 0.982370 |

---

## 9. Correlation Structure

| Variable | AI | LEGAL | RES | PQC |
|-----------|------:|------:|------:|------:|
| AI_INDEX | 1.000000 | 0.783568 | 0.517254 | 0.840634 |
| LEGAL_WGI_SCORE | 0.783568 | 1.000000 | 0.664976 | 0.730088 |
| RES_INDEX | 0.517254 | 0.664976 | 1.000000 | 0.380787 |
| PQC | 0.840634 | 0.730088 | 0.380787 | 1.000000 |

---

## 10. Distribution Diagnostics

| Variable | Skewness | Kurtosis |
|-----------|---------:|---------:|
| AI_INDEX | -0.395939 | -0.913245 |
| LEGAL_WGI_SCORE | 0.183835 | -0.892587 |
| RES_INDEX | 0.780795 | 0.498641 |
| PQC | -0.443125 | -1.006802 |

---

## 11. Factorability Assessment

### KMO Test

KMO = 0.7355868518654463

### Bartlett Test

Chi-square = 249.83379389196242

p-value = 4.450885068086372e-51

The results support the suitability of factor-analytic dimensional reduction.

---

## 12. Principal Component Analysis

### Eigenvalue Share

```text
[0.74561879, 0.17028181, 0.04806765, 0.03603175]
```

### Total Explained Variance

```text
0.9999999999999999
```

### PCA Loadings

| Variable | PC1 | PC2 | PC3 | PC4 |
|-----------|---------:|---------:|---------:|---------:|
| AI_INDEX | 0.534197 | -0.272778 | -0.351497 | 0.718802 |
| LEGAL_WGI_SCORE | 0.536276 | 0.105185 | 0.835959 | 0.050156 |
| RES_INDEX | 0.416053 | 0.816887 | -0.359197 | -0.174850 |
| PQC | 0.503926 | -0.497216 | -0.220453 | -0.670996 |

---

## 13. PCA-Derived Weights

| Variable | Weight |
|-----------|-------:|
| AI_INDEX | 0.26837950 |
| LEGAL_WGI_SCORE | 0.26942446 |
| RES_INDEX | 0.20902441 |
| PQC | 0.25317163 |

---

## 14. Reliability Assessment

Cronbach's Alpha

```text
0.8785685555594794
```

95% Confidence Interval

```text
[0.832, 0.915]
```

The index demonstrates strong internal consistency.

---

## 15. Alternative Weighting Validation

### CRITIC Weights

| Variable | Weight |
|-----------|-------:|
| AI_INDEX | 0.241936 |
| LEGAL_WGI_SCORE | 0.210281 |
| RES_INDEX | 0.227146 |
| PQC | 0.320637 |

### Entropy Weights

| Variable | Weight |
|-----------|-------:|
| AI_INDEX | 0.290727 |
| LEGAL_WGI_SCORE | 0.234477 |
| RES_INDEX | 0.155500 |
| PQC | 0.319295 |

---

## 16. Robustness Assessment

### Equal Weight vs PCA

```text
ρ = 0.9992427048606825
p = 7.153803172038685e-126
```

### PCA vs Entropy

```text
ρ = 0.9972671523233321
p = 2.290322902718063e-101
```

### PCA vs CRITIC

```text
ρ = 0.998304317405441
p = 1.776061187692281e-110
```

The ranking structure remains highly stable across alternative weighting schemes.

---

## 17. Results

### Top 20 Countries

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

## 18. Lowest-Ranked Countries

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

## 19. Reproducibility Audit

### Runtime Metadata

```json
{
  "timestamp": "2026-06-05T16:11:24.057391",
  "python_version": "3.12.13",
  "platform": "Linux-6.6.122+-x86_64-with-glibc2.35",
  "countries": 90,
  "final_N": 90
}
```

---

## 20. File Integrity Verification

| File | SHA256 |
|--------|--------|
| AI_INDEX_2026_v1_MC_Canon.csv | 16656947ff8486b896640a00d05deccee086e52358f6614472ad38929af0b776 |
| LEGAL_WGI_2026_v1_MC_Canon.csv | 13e5310373fc4104b70b0eb410ccb1628099336f21fe705545b472290cc7b4e7 |
| RES_INDEX_2026_MC_Canon.csv | 4e936fa81a2fa2d491b897313ac136d38af431cb72f55b3adb85006bded88c9d |
| PQC_NCSI_2026_MC_Canon.csv | a421685fedadd3fb3b0b9ffbdb3822401ea4ab98098853b104f54397631cda8d |
| QSSI_MASTER_DATASET.csv | 6ac531236999faa3680978cbe09eb8c93e9ebc85e1881f937d257f873b727931 |
| QSSI_RANKINGS_2026.csv | 56681c6fcc4c89a89982b9e117beedde76f02ef4c1c473bd86079e66542d8215 |

---

## References

Mazumdar, B. (2026). QSSI 2026 FAIR+D Canon™ Global Framework. Current Edition DOI: 10.5281/zenodo.20385492.

All versions may be cited using DOI: 10.5281/zenodo.17302169.

ORCID: https://orcid.org/0009-0007-5615-3558
