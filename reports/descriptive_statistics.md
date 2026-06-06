# QSSI™ 2026 Descriptive Statistics, Harmonization, Coverage, Validation and Composite Index Audit

## Sovereign Intelligence, Security and Stability Index (QSSI™) 2026

### FAIR+D Canon Research Series

**Author:** Dr. B. Mazumdar  
**ORCID:** 0009-0007-5615-3558  
**All Versions DOI:** 10.5281/zenodo.17302169  
**Current Edition DOI:** 10.5281/zenodo.20385492  

---

# 1. Source Dataset Coverage

| Dataset | Countries |
|----------|-----------:|
| AI_INDEX_2026_v1 | 195 |
| LEGAL_WGI_2026_v1 | 213 |
| RES_INDEX_2026 | 181 |
| PQC_NCSI_2026 | 124 |

---

# 2. Pairwise Dataset Intersection Matrix

| Variable | AI | LEGAL | RES | PQC |
|-----------|----:|------:|----:|----:|
| AI | 195 | 172 | 128 | 118 |
| LEGAL | 172 | 213 | 136 | 117 |
| RES | 128 | 136 | 181 | 94 |
| PQC | 118 | 117 | 94 | 124 |

---

# 3. Canonical Harmonization Outcome

| Metric | Value |
|----------|------:|
| Definitive Final N | 90 |
| Included Countries | 90 |
| Excluded Due To PQC Coverage | 36 |
| Missing Observations | 0 |

---

# 4. Included Countries (N = 90)

## First Five Countries

| Index | Country |
|-------:|----------|
| 0 | Albania |
| 1 | Algeria |
| 2 | Angola |
| 3 | Antigua and Barbuda |
| 4 | Argentina |

## Last Five Countries

| Index | Country |
|-------:|----------|
| 85 | United Arab Emirates |
| 86 | United Kingdom |
| 87 | United States |
| 88 | Uruguay |
| 89 | Zimbabwe |

---

# 5. Final Harmonized Dataset Structure

| Property | Value |
|-----------|--------|
| Shape | (90, 5) |
| Variables | country, AI_INDEX, LEGAL_WGI_SCORE, RES_INDEX, PQC |

---

# 6. Missing Value Audit

| Variable | Missing Values |
|------------|---------------:|
| country | 0 |
| AI_INDEX | 0 |
| LEGAL_WGI_SCORE | 0 |
| RES_INDEX | 0 |
| PQC | 0 |

### Result

No missing observations remain after harmonization and canonical filtering.

---

# 7. PCA Eigenvalue Variance Structure

| Principal Component | Explained Variance |
|---------------------|-------------------:|
| PC1 | 0.745619 |
| PC2 | 0.170282 |
| PC3 | 0.048068 |
| PC4 | 0.036032 |

### Total Explained Variance

| Metric | Value |
|---------|------:|
| Sum | 1.000000 |

---

# 8. Sampling Adequacy and Factorability Tests

| Test | Statistic |
|--------|----------:|
| Kaiser-Meyer-Olkin (KMO) | 0.735587 |
| Bartlett Chi-Square | 249.833794 |
| Bartlett p-value | 4.450885068086372e-51 |

### Interpretation

The KMO statistic indicates acceptable multivariate sampling adequacy. Bartlett's Test rejects the null hypothesis of an identity correlation matrix, confirming suitability for dimensionality reduction and composite index construction.

---

# 9. Descriptive Statistics

| Statistic | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|------------|---------:|----------------:|----------:|----:|
| Count | 90.000000 | 90.000000 | 90.000000 | 90.000000 |
| Mean | 0.566620 | 0.540517 | 0.394125 | 0.595676 |
| Std. Dev. | 0.250973 | 0.228008 | 0.140781 | 0.272357 |
| Minimum | 0.050407 | 0.108866 | 0.150195 | 0.000000 |
| 25% | 0.393117 | 0.359012 | 0.298129 | 0.376115 |
| Median | 0.633618 | 0.504046 | 0.371685 | 0.641621 |
| 75% | 0.766077 | 0.697156 | 0.459482 | 0.827448 |
| Maximum | 1.000000 | 0.966323 | 0.808925 | 0.982370 |

---

# 10. Correlation Matrix

| Variable | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|-----------|---------:|----------------:|----------:|----:|
| AI_INDEX | 1.000000 | 0.783568 | 0.517254 | 0.840634 |
| LEGAL_WGI_SCORE | 0.783568 | 1.000000 | 0.664976 | 0.730088 |
| RES_INDEX | 0.517254 | 0.664976 | 1.000000 | 0.380787 |
| PQC | 0.840634 | 0.730088 | 0.380787 | 1.000000 |

---

# 11. Distribution Diagnostics

| Variable | Skewness | Kurtosis |
|-----------|---------:|---------:|
| AI_INDEX | -0.395939 | -0.913245 |
| LEGAL_WGI_SCORE | 0.183835 | -0.892587 |
| RES_INDEX | 0.780795 | 0.498641 |
| PQC | -0.443125 | -1.006802 |

---

# 12. Composite Reliability

| Metric | Estimate | 95% Confidence Interval |
|---------|---------:|------------------------|
| Reliability Coefficient | 0.878569 | [0.832, 0.915] |

---

# 13. PCA Component Loadings

| Variable | PC1 | PC2 | PC3 | PC4 |
|-----------|----------:|----------:|----------:|----------:|
| AI_INDEX | 0.534197 | -0.272778 | -0.351497 | 0.718802 |
| LEGAL_WGI_SCORE | 0.536276 | 0.105185 | 0.835959 | 0.050156 |
| RES_INDEX | 0.416053 | 0.816887 | -0.359197 | -0.174850 |
| PQC | 0.503926 | -0.497216 | -0.220453 | -0.670996 |

---

# 14. PCA-Derived Composite Weights

| Variable | Weight |
|-----------|-------:|
| AI_INDEX | 0.268380 |
| LEGAL_WGI_SCORE | 0.269424 |
| RES_INDEX | 0.209024 |
| PQC | 0.253172 |

---

# 15. CRITIC Objective Weights

| Variable | CRITIC Weight |
|-----------|--------------:|
| AI_INDEX | 0.241936 |
| LEGAL_WGI_SCORE | 0.210281 |
| RES_INDEX | 0.227146 |
| PQC | 0.320637 |

---

# 16. Entropy Objective Weights

| Variable | Entropy Weight |
|-----------|---------------:|
| AI_INDEX | 0.290727 |
| LEGAL_WGI_SCORE | 0.234477 |
| RES_INDEX | 0.155500 |
| PQC | 0.319295 |

---

# 17. Ranking Robustness Assessment

| Comparison | Spearman Correlation | p-value |
|------------|--------------------:|---------:|
| Equal Weight vs PCA | 0.999243 | 7.153803172038685e-126 |
| PCA vs Entropy | 0.997267 | 2.290322902718063e-101 |
| Additional Robustness Check | 0.998304 | 1.776061187692281e-110 |

### Interpretation

The exceptionally high rank-order correlations demonstrate strong methodological robustness and ranking stability across alternative weighting frameworks.

---

# 18. Top 20 Sovereign QSSI™ Rankings (2026)

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

# 19. Bottom 20 Sovereign QSSI™ Rankings (2026)

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

# 20. Final Top 10

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

# 21. Final Bottom 10

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

# 22. Reproducibility and Computational Environment

| Attribute | Value |
|------------|--------|
| Timestamp | 2026-06-05T16:11:24.057391 |
| Python Version | 3.12.13 |
| Platform | Linux-6.6.122+-x86_64-with-glibc2.35 |
| Final Countries | 90 |
| Final N | 90 |

---

# 23. SHA-256 Integrity Audit

| File | SHA-256 |
|--------|----------|
| AI_INDEX_2026_v1_MC_Canon.csv | 16656947ff8486b896640a00d05deccee086e52358f6614472ad38929af0b776 |
| LEGAL_WGI_2026_v1_MC_Canon.csv | 13e5310373fc4104b70b0eb410ccb1628099336f21fe705545b472290cc7b4e7 |
| RES_INDEX_2026_MC_Canon.csv | 4e936fa81a2fa2d491b897313ac136d38af431cb72f55b3adb85006bded88c9d |
| PQC_NCSI_2026_MC_Canon.csv | a421685fedadd3fb3b0b9ffbdb3822401ea4ab98098853b104f54397631cda8d |
| QSSI_MASTER_DATASET.csv | 6ac531236999faa3680978cbe09eb8c93e9ebc85e1881f937d257f873b727931 |
| QSSI_RANKINGS_2026.csv | 56681c6fcc4c89a89982b9e117beedde76f02ef4c1c473bd86079e66542d8215 |

---

# 24. Generated Outputs

| Output File |
|-------------|
| QSSI_RANKINGS_2026.csv |
| QSSI_FINAL_AUDIT.json |
| QSSI_SHA256_AUDIT.csv |
| QSSI_CRITIC_WEIGHTS.csv |
| QSSI_ENTROPY_WEIGHTS.csv |

---

# Citation

Mazumdar, B. (2026). *QSSI™ 2026: Sovereign Intelligence, Security and Stability Index (QSSI™) Framework, Datasets, Harmonization Protocols, Composite Index Construction, Validation and International Rankings*. FAIR+D Canon Research Series.

**ORCID:** 0009-0007-5615-3558  
**Current Edition DOI:** 10.5281/zenodo.20385492  
**All Versions DOI:** 10.5281/zenodo.17302169

---
End of Report
