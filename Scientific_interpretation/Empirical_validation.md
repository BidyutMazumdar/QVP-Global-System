# QSSI 2026 Empirical Validation

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

# Empirical Validation Summary

| Metric | Value |
|----------|----------:|
| AI Indicators | 195 |
| Legal Indicators | 213 |
| Resilience Indicators | 181 |
| PQC Indicators | 124 |
| Initial Countries Considered | 126 |
| Excluded (Insufficient PQC Coverage) | 36 |
| Definitive Final Countries | 90 |
| Missing Values After Harmonization | 0 |

---

# Indicator Crosswalk Matrix

|        | AI | LEGAL | RES | PQC |
|--------|------:|------:|------:|------:|
| AI | 195 | 172 | 128 | 118 |
| LEGAL | 172 | 213 | 136 | 117 |
| RES | 128 | 136 | 181 | 94 |
| PQC | 118 | 117 | 94 | 124 |

---

# Final Sample

## Countries Included

| Index |
|---------|
| Albania |
| Algeria |
| Angola |
| Antigua and Barbuda |
| Argentina |
| ... |
| United Arab Emirates |
| United Kingdom |
| United States |
| Uruguay |
| Zimbabwe |

---

# Dataset Integrity Audit

| Variable | Missing Values |
|------------|-------------:|
| country | 0 |
| AI_INDEX | 0 |
| LEGAL_WGI_SCORE | 0 |
| RES_INDEX | 0 |
| PQC | 0 |

**Final Dataset Shape:** `(90,5)`

---

# Principal Component Analysis (PCA)

## Eigenvalue Proportions

| Component | Variance Explained |
|-----------|-------------------:|
| PC1 | 0.74561879 |
| PC2 | 0.17028181 |
| PC3 | 0.04806765 |
| PC4 | 0.03603175 |

**Total Variance Explained = 1.000000000000000**

---

# Sampling Adequacy and Factorability

| Test | Value |
|---------|---------:|
| Kaiser-Meyer-Olkin (KMO) | 0.7355868518654463 |
| Bartlett Chi-Square | 249.83379389196242 |
| Bartlett p-value | 4.450885068086372e-51 |

### Interpretation

- KMO > 0.70 indicates good sampling adequacy.
- Bartlett test highly significant.
- PCA application statistically justified.

---

# Descriptive Statistics

| Variable | Mean | Std | Min | 25% | Median | 75% | Max |
|------------|---------:|---------:|---------:|---------:|---------:|---------:|---------:|
| AI_INDEX | 0.566620 | 0.250973 | 0.050407 | 0.393117 | 0.633618 | 0.766077 | 1.000000 |
| LEGAL_WGI_SCORE | 0.540517 | 0.228008 | 0.108866 | 0.359012 | 0.504046 | 0.697156 | 0.966323 |
| RES_INDEX | 0.394125 | 0.140781 | 0.150195 | 0.298129 | 0.371685 | 0.459482 | 0.808925 |
| PQC | 0.595676 | 0.272357 | 0.000000 | 0.376115 | 0.641621 | 0.827448 | 0.982370 |

---

# Correlation Matrix

| Variable | AI | LEGAL | RES | PQC |
|------------|---------:|---------:|---------:|---------:|
| AI_INDEX | 1.000000 | 0.783568 | 0.517254 | 0.840634 |
| LEGAL_WGI_SCORE | 0.783568 | 1.000000 | 0.664976 | 0.730088 |
| RES_INDEX | 0.517254 | 0.664976 | 1.000000 | 0.380787 |
| PQC | 0.840634 | 0.730088 | 0.380787 | 1.000000 |

---

# Distribution Diagnostics

| Variable | Skewness | Kurtosis |
|------------|---------:|---------:|
| AI_INDEX | -0.395939 | -0.913245 |
| LEGAL_WGI_SCORE | 0.183835 | -0.892587 |
| RES_INDEX | 0.780795 | 0.498641 |
| PQC | -0.443125 | -1.006802 |

---

# Reliability Analysis

| Metric | Value |
|----------|---------:|
| Cronbach Alpha | 0.8785685555594794 |
| 95% Confidence Interval | [0.832, 0.915] |

### Interpretation

Excellent internal consistency and cross-dimensional reliability.

---

# PCA Loading Matrix

| Variable | PC1 | PC2 | PC3 | PC4 |
|------------|---------:|---------:|---------:|---------:|
| AI_INDEX | 0.534197 | -0.272778 | -0.351497 | 0.718802 |
| LEGAL_WGI_SCORE | 0.536276 | 0.105185 | 0.835959 | 0.050156 |
| RES_INDEX | 0.416053 | 0.816887 | -0.359197 | -0.174850 |
| PQC | 0.503926 | -0.497216 | -0.220453 | -0.670996 |

---

# PCA-Derived Composite Weights

| Variable | Weight |
|------------|---------:|
| AI_INDEX | 0.26837950 |
| LEGAL_WGI_SCORE | 0.26942446 |
| RES_INDEX | 0.20902441 |
| PQC | 0.25317163 |

---

# Alternative Weighting Robustness

## CRITIC Weights

| Variable | Weight |
|------------|---------:|
| AI_INDEX | 0.241936 |
| LEGAL_WGI_SCORE | 0.210281 |
| RES_INDEX | 0.227146 |
| PQC | 0.320637 |

## Entropy Weights

| Variable | Weight |
|------------|---------:|
| AI_INDEX | 0.290727 |
| LEGAL_WGI_SCORE | 0.234477 |
| RES_INDEX | 0.155500 |
| PQC | 0.319295 |

---

# Rank Stability Validation

| Comparison | Spearman Correlation | p-value |
|-------------|---------:|---------:|
| Equal vs PCA | 0.9992427048606825 | 7.153803172038685e-126 |
| PCA vs Entropy | 0.9972671523233321 | 2.290322902718063e-101 |
| PCA vs CRITIC | 0.9983043174054410 | 1.776061187692281e-110 |

### Interpretation

QSSI rankings remain exceptionally stable across independent weighting methodologies.

---

# Global QSSI 2026 Rankings

## Top 20 Countries

| Rank | Country | QSSI |
|------:|----------|---------:|
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

## Bottom 20 Countries

| Rank | Country | QSSI |
|------:|----------|---------:|
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

# Top 10 Countries

| Rank | Country | QSSI |
|------:|----------|---------:|
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

# Bottom 10 Countries

| Rank | Country | QSSI |
|------:|----------|---------:|
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

# Computational Audit Metadata

| Field | Value |
|---------|---------|
| Timestamp | 2026-06-05T16:11:24.057391 |
| Python Version | 3.12.13 |
| Platform | Linux-6.6.122+-x86_64-with-glibc2.35 |
| Countries | 90 |
| Final N | 90 |

---

# Cryptographic Reproducibility Audit (SHA-256)

| File | SHA256 |
|---------|---------|
| AI_INDEX_2026_v1_MC_Canon.csv | 16656947ff8486b896640a00d05deccee086e52358f6614472ad38929af0b776 |
| LEGAL_WGI_2026_v1_MC_Canon.csv | 13e5310373fc4104b70b0eb410ccb1628099336f21fe705545b472290cc7b4e7 |
| RES_INDEX_2026_MC_Canon.csv | 4e936fa81a2fa2d491b897313ac136d38af431cb72f55b3adb85006bded88c9d |
| PQC_NCSI_2026_MC_Canon.csv | a421685fedadd3fb3b0b9ffbdb3822401ea4ab98098853b104f54397631cda8d |
| QSSI_MASTER_DATASET.csv | 6ac531236999faa3680978cbe09eb8c93e9ebc85e1881f937d257f873b727931 |
| QSSI_RANKINGS_2026.csv | 56681c6fcc4c89a89982b9e117beedde76f02ef4c1c473bd86079e66542d8215 |

---

# Source Repository Structure

```text
QVP-Global-System/
│
├── data/
│   ├── raw/
│   │   ├── 2025-Government-AI-Readiness-Index-Report_01_26.pdf
│   │   ├── 2025_wjp_rule_of_law_index_HISTORICAL_DATA_FILE.xlsx
│   │   ├── dataset_2026-04-29T12_08_28.599500883Z_DEFAULT_INTEGRATION_IMF.STA_NDGAIN_1.0.1.csv
│   │   ├── qssi_raw_sources_v2026.1.csv
│   │   └── wgicalculator-2025.xlsx
│   │
│   ├── Benchmark/
│   ├── canonical/
│   ├── final/
│   ├── processed/
│   ├── raw/
│   │
│   ├── AI_OECD_2026.csv
│   ├── AI_OXFORD_2026.csv
│   ├── RES_GLOBAL_RESILIENCE_INDEX_v1.0_STRICT.csv
│   ├── RES_IMF_2026.csv
│   ├── RES_NDGAIN_2026_FINAL.csv
│   ├── qssi_resilience_institutional_2026_FAIR+D_Canon.csv
│   └── wjp_clean.csv
```

---

# Citation

Current Edition DOI:
10.5281/zenodo.20385492

All Versions DOI:
10.5281/zenodo.17302169

ORCID:
https://orcid.org/0009-0007-5615-3558

---

## Version

**QSSI 2026 Empirical Validation — FAIR+D Canon™ Global Framework — International Institutional Edition**
