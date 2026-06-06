## Quantum Sovereignty & Strategic Intelligence Index (QSSI™) 2026

**Author:** Dr. B. Mazumdar, D.Sc. (Hon.), D.Litt. (Hon.)  
**ORCID:** https://orcid.org/0009-0007-5615-3558  
**All Versions DOI:** 10.5281/zenodo.17302169  
**Current Edition DOI:** 10.5281/zenodo.20385492  

---

## Dataset Harmonization and Coverage Assessment

| Variable | Source Coverage |
|----------|----------------|
| AI_INDEX | 195 |
| LEGAL_WGI_SCORE | 213 |
| RES_INDEX | 181 |
| PQC | 124 |

### Cross-Dataset Coverage Matrix

| | AI | LEGAL | RES | PQC |
|---|---:|---:|---:|---:|
| AI | 195 | 172 | 128 | 118 |
| LEGAL | 172 | 213 | 136 | 117 |
| RES | 128 | 136 | 181 | 94 |
| PQC | 118 | 117 | 94 | 124 |

---

## Canonical Harmonization Results

| Metric | Value |
|----------|------:|
| Definitive Final Sample (N) | 90 |
| Countries Included | 90 |
| Countries Excluded Due to PQC Coverage Constraints | 36 |
| Missing Observations Remaining | 0 |

### Final Harmonized Variables

| Variable | Coverage |
|----------|----------|
| AI_INDEX | 90 |
| LEGAL_WGI_SCORE | 90 |
| RES_INDEX | 90 |
| PQC | 90 |

### Data Integrity Verification

```text
Shape: (90, 5)

country              0
AI_INDEX             0
LEGAL_WGI_SCORE      0
RES_INDEX            0
PQC                  0
dtype: int64
```

No missing observations remain after harmonization and canonical filtering.

---

## Included Countries (N = 90)

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

## Statistical Adequacy Assessment

### Eigenvalue Structure

```text
0.74561879
0.17028181
0.04806765
0.03603175
```

Sum of Explained Variance:

```text
0.9999999999999999
```

### Kaiser–Meyer–Olkin Measure

| Statistic | Value |
|------------|-------:|
| KMO | 0.7355868518654463 |

### Bartlett’s Test of Sphericity

| Statistic | Value |
|------------|-------:|
| Chi-Square | 249.83379389196242 |
| p-value | 4.450885068086372 × 10⁻⁵¹ |

The KMO statistic exceeds conventional adequacy thresholds and Bartlett’s test strongly rejects the null hypothesis of an identity correlation matrix, supporting dimensional reduction and latent structure estimation.

---

## Descriptive Statistics

| Variable | Mean | Std | Min | 25% | Median | 75% | Max |
|-----------|------:|------:|------:|------:|------:|------:|------:|
| AI_INDEX | 0.566620 | 0.250973 | 0.050407 | 0.393117 | 0.633618 | 0.766077 | 1.000000 |
| LEGAL_WGI_SCORE | 0.540517 | 0.228008 | 0.108866 | 0.359012 | 0.504046 | 0.697156 | 0.966323 |
| RES_INDEX | 0.394125 | 0.140781 | 0.150195 | 0.298129 | 0.371685 | 0.459482 | 0.808925 |
| PQC | 0.595676 | 0.272357 | 0.000000 | 0.376115 | 0.641621 | 0.827448 | 0.982370 |

---

## Correlation Structure

| Variable | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|-----------|---------:|---------:|---------:|---------:|
| AI_INDEX | 1.000000 | 0.783568 | 0.517254 | 0.840634 |
| LEGAL_WGI_SCORE | 0.783568 | 1.000000 | 0.664976 | 0.730088 |
| RES_INDEX | 0.517254 | 0.664976 | 1.000000 | 0.380787 |
| PQC | 0.840634 | 0.730088 | 0.380787 | 1.000000 |

---

## Distribution Diagnostics

| Variable | Skewness | Kurtosis |
|-----------|---------:|---------:|
| AI_INDEX | -0.395939 | -0.913245 |
| LEGAL_WGI_SCORE | 0.183835 | -0.892587 |
| RES_INDEX | 0.780795 | 0.498641 |
| PQC | -0.443125 | -1.006802 |

---

## Reliability Assessment

### Cronbach's Alpha

| Statistic | Estimate | 95% Confidence Interval |
|-----------|----------:|------------------------|
| Alpha | 0.878569 | [0.832, 0.915] |

The internal consistency estimate indicates strong reliability across the four-dimensional index architecture.

---

## Principal Component Structure

| Variable | PC1 | PC2 | PC3 | PC4 |
|-----------|---------:|---------:|---------:|---------:|
| AI_INDEX | 0.534197 | -0.272778 | -0.351497 | 0.718802 |
| LEGAL_WGI_SCORE | 0.536276 | 0.105185 | 0.835959 | 0.050156 |
| RES_INDEX | 0.416053 | 0.816887 | -0.359197 | -0.174850 |
| PQC | 0.503926 | -0.497216 | -0.220453 | -0.670996 |

---

## PCA-Derived Composite Weights

| Variable | Weight |
|-----------|--------:|
| AI_INDEX | 0.268380 |
| LEGAL_WGI_SCORE | 0.269424 |
| RES_INDEX | 0.209024 |
| PQC | 0.253172 |

---

## CRITIC Objective Weights

| Variable | CRITIC Weight |
|-----------|--------------:|
| AI_INDEX | 0.241936 |
| LEGAL_WGI_SCORE | 0.210281 |
| RES_INDEX | 0.227146 |
| PQC | 0.320637 |

---

## Entropy Objective Weights

| Variable | Entropy Weight |
|-----------|---------------:|
| AI_INDEX | 0.290727 |
| LEGAL_WGI_SCORE | 0.234477 |
| RES_INDEX | 0.155500 |
| PQC | 0.319295 |

---

## Weighting Robustness Validation

### Rank Correlation Analysis

| Comparison | Spearman ρ | p-value |
|------------|-----------:|---------:|
| Equal vs PCA | 0.999243 | 7.153803 × 10⁻¹²⁶ |
| PCA vs Entropy | 0.997267 | 2.290323 × 10⁻¹⁰¹ |
| Equal vs CRITIC | 0.998304 | 1.776061 × 10⁻¹¹⁰ |

The exceptionally high concordance across weighting methodologies demonstrates strong ranking robustness and methodological stability.

---

# Global Rankings

## Top 20 Countries

| Rank | Country | QSSI |
|------:|---------|------:|
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
|------:|---------|------:|
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

## Top 10 Summary

| Rank | Country | QSSI |
|------:|---------|------:|
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

## Bottom 10 Summary

| Rank | Country | QSSI |
|------:|---------|------:|
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

## Reproducibility and Audit Infrastructure

### Computational Environment

| Attribute | Value |
|------------|--------|
| Timestamp | 2026-06-05T16:11:24.057391 |
| Python Version | 3.12.13 |
| Platform | Linux-6.6.122+-x86_64-with-glibc2.35 |
| Countries | 90 |
| Final N | 90 |

### Generated Audit Artifacts

```text
QSSI_MASTER_DATASET.csv
QSSI_RANKINGS_2026.csv
QSSI_FINAL_AUDIT.json
QSSI_SHA256_AUDIT.csv
QSSI_CRITIC_WEIGHTS.csv
QSSI_ENTROPY_WEIGHTS.csv
```

### SHA-256 Integrity Register

| File | SHA256 |
|------|--------|
| AI_INDEX_2026_v1_MC_Canon.csv | 16656947ff8486b896640a00d05deccee086e52358f6614472ad38929af0b776 |
| LEGAL_WGI_2026_v1_MC_Canon.csv | 13e5310373fc4104b70b0eb410ccb1628099336f21fe705545b472290cc7b4e7 |
| RES_INDEX_2026_MC_Canon.csv | 4e936fa81a2fa2d491b897313ac136d38af431cb72f55b3adb85006bded88c9d |
| PQC_NCSI_2026_MC_Canon.csv | a421685fedadd3fb3b0b9ffbdb3822401ea4ab98098853b104f54397631cda8d |
| QSSI_MASTER_DATASET.csv | 6ac531236999faa3680978cbe09eb8c93e9ebc85e1881f937d257f873b727931 |
| QSSI_RANKINGS_2026.csv | 56681c6fcc4c89a89982b9e117beedde76f02ef4c1c473bd86079e66542d8215 |

---

## Definitive Audit Summary

| Metric | Value |
|----------|------:|
| Final Countries | 90 |
| Final Observations | 90 |
| Missing Values | 0 |
| Reliability (Cronbach's α) | 0.878569 |
| KMO | 0.735587 |
| Bartlett p-value | 4.450885 × 10⁻⁵¹ |
| PCA Variance Explained (PC1) | 74.56% |
| Rank Stability (Equal vs PCA) | 0.999243 |
| Rank Stability (PCA vs Entropy) | 0.997267 |
| Rank Stability (Equal vs CRITIC) | 0.998304 |

The final harmonized QSSI™ 2026 dataset consists of 90 countries with complete coverage across all four constituent dimensions. Statistical adequacy diagnostics, reliability testing, principal component analysis, objective weighting procedures, robustness validation, and cryptographic integrity verification collectively support a reproducible and fully auditable analytical framework suitable for comparative international assessment.
