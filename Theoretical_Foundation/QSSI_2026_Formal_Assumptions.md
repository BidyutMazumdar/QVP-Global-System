# QSSI 2026 Formal Assumptions
## Quantum-Veil Sovereignty Security Index (QSSI)
### FAIR+D Canon™ Global Framework

---

## Current Definitive Edition DOI
10.5281/zenodo.20385492

## Canonical DOI (All Versions)
10.5281/zenodo.17302169

## Author
Dr. B. Mazumdar

## ORCID
https://orcid.org/0009-0007-5615-3558

## Framework Classification
Formal Theoretical, Statistical, Computational, Methodological, and Epistemological Assumptions

## Framework Status
QSSI 2026 Definitive World Edition

---

# Abstract

This document presents the formal theoretical, statistical, computational, methodological, and epistemological assumptions underlying the Quantum-Veil Sovereignty Security Index (QSSI) 2026 Definitive World Edition.

QSSI is a multidimensional sovereign capability assessment framework designed to evaluate national preparedness across four strategic dimensions:

1. Artificial Intelligence Capability
2. Governance and Legal Quality
3. National Resilience Capacity
4. Post-Quantum Cybersecurity Readiness

The framework integrates heterogeneous international datasets through deterministic harmonization, complete-case selection, Min-Max normalization, dimensionality assessment, robustness validation, reproducible aggregation, audit-traceable computation, and integrity-preserving archival procedures.

These assumptions establish the foundational conditions necessary for rigorous interpretation, reproducibility, longitudinal comparability, transparency, and policy-grade analytical application under the FAIR+D Canon™ Global Framework.

---

# 1. Sovereign Entity Assumption

QSSI assumes that sovereign nation-states constitute the appropriate analytical unit for comparative capability assessment.

Each country is treated as an independent sovereign observation.

The framework excludes:

- Subnational jurisdictions
- Municipal entities
- Regional administrations
- Corporate organizations
- International alliances
- Non-state actors
- Private institutions
- Multinational enterprises

The sovereign state remains the sole unit of analysis.

---

# 2. Dataset Validity Assumption

QSSI assumes that all incorporated datasets provide empirically valid representations of their intended strategic capability domains.

## Source Dataset Coverage

| Dimension | Dataset | Coverage |
|------------|------------|-----------:|
| Artificial Intelligence Capability | AI_INDEX_2026 | 195 |
| Governance & Legal Quality | LEGAL_WGI_2026 | 213 |
| National Resilience Capacity | RES_INDEX_2026 | 181 |
| Post-Quantum Cybersecurity Readiness | PQC_NCSI_2026 | 124 |

Each dataset is assumed to possess sufficient informational validity, methodological credibility, measurement consistency, and international comparability for sovereign capability assessment.

---

# 3. Cross-Domain Harmonization Assumption

Country identifiers originating from heterogeneous international sources may differ in naming conventions, territorial labels, or administrative representations.

QSSI assumes that harmonization procedures correctly identify equivalent sovereign entities across all incorporated datasets.

### Examples

- United States of America → United States
- United Kingdom of Great Britain and Northern Ireland → United Kingdom
- Republic of Korea → South Korea
- Czechia → Czech Republic

The harmonization process is assumed to preserve analytical validity, cross-source consistency, and sovereign comparability.

---

# 4. Coverage Intersection Assumption

Only sovereign entities possessing valid observations across all four strategic dimensions are retained.

Countries with incomplete observations are excluded from composite index construction.

## Dataset Matrix

| Dataset | Coverage |
|----------|----------:|
| AI | 195 |
| LEGAL | 213 |
| RES | 181 |
| PQC | 124 |

## Cross-Domain Overlap Matrix

| | AI | LEGAL | RES | PQC |
|---|---:|---:|---:|---:|
| AI | 195 | 172 | 128 | 118 |
| LEGAL | 172 | 213 | 136 | 117 |
| RES | 128 | 136 | 181 | 94 |
| PQC | 118 | 117 | 94 | 124 |

### Final Analytical Sample

| Metric | Value |
|----------|----------:|
| Countries Included | 90 |
| Countries Excluded Due To PQC Coverage Constraints | 36 |
| Missing Values | 0 |
| Final Observations | 90 |

### Final Dataset Shape

```text
(90, 5)
```

### Missing Value Audit

```text
country              0
AI_INDEX             0
LEGAL_WGI_SCORE      0
RES_INDEX            0
PQC                  0
dtype: int64
```

The retained sample is assumed to provide a sufficiently representative basis for comparative sovereign capability assessment.

---

# 5. Indicator Independence Assumption

QSSI assumes that each dimension measures a related yet non-identical component of sovereign capability.

Moderate correlation among indicators is permissible provided complete redundancy is absent.

The framework therefore assumes:

- Partial dependence is acceptable.
- Complete redundancy is absent.
- Distinct informational contributions exist.
- Each dimension contributes unique analytical value.

---

# 6. Normalization Assumption

Indicators originate from heterogeneous scales, units, and measurement systems.

To ensure comparability, QSSI applies Min-Max normalization.

## Transformation

\[
X_{norm}=\frac{X-X_{min}}{X_{max}-X_{min}}
\]

## Constraint

\[
0 \leq X_{norm} \leq 1
\]

The framework assumes that Min-Max normalization preserves ordinal relationships and relative positioning among sovereign entities.

---

# 7. Monotonicity Assumption

QSSI assumes that increasing indicator values correspond to increasing sovereign capability.

Accordingly:

- Higher AI_INDEX values indicate stronger AI capability.
- Higher LEGAL_WGI_SCORE values indicate stronger governance quality.
- Higher RES_INDEX values indicate stronger resilience capacity.
- Higher PQC values indicate stronger post-quantum cybersecurity readiness.

No incorporated indicator is interpreted inversely.

---

# 8. Statistical Adequacy Assumption

The framework assumes that the observed correlation structure is sufficient for multivariate dimensionality assessment.

## Eigenvalue Structure

```text
[0.74561879 0.17028181 0.04806765 0.03603175]
```

### Eigenvalue Sum

```text
0.9999999999999999
```

## Kaiser-Meyer-Olkin (KMO)

| Statistic | Value |
|------------|------------:|
| KMO | 0.7355868518654463 |

Interpretation:

Good sampling adequacy for multivariate dimensionality reduction.

## Bartlett's Test of Sphericity

| Statistic | Value |
|------------|------------:|
| Chi-Square | 249.83379389196242 |
| P-Value | 4.450885068086372e-51 |

Interpretation:

Highly significant correlation structure suitable for principal component analysis.

---

# 9. Distributional Assumption

The framework assumes that descriptive distributional properties provide meaningful characterization of sovereign capability variation.

## Descriptive Statistics

| Variable | Count | Mean | Std | Min | 25% | Median | 75% | Max |
|------------|------------:|------------:|------------:|------------:|------------:|------------:|------------:|------------:|
| AI_INDEX | 90 | 0.566620 | 0.250973 | 0.050407 | 0.393117 | 0.633618 | 0.766077 | 1.000000 |
| LEGAL_WGI_SCORE | 90 | 0.540517 | 0.228008 | 0.108866 | 0.359012 | 0.504046 | 0.697156 | 0.966323 |
| RES_INDEX | 90 | 0.394125 | 0.140781 | 0.150195 | 0.298129 | 0.371685 | 0.459482 | 0.808925 |
| PQC | 90 | 0.595676 | 0.272357 | 0.000000 | 0.376115 | 0.641621 | 0.827448 | 0.982370 |

---

# 10. Correlation Structure Assumption

The framework assumes that sovereign capability dimensions are meaningfully related while retaining distinct analytical contributions.

## Correlation Matrix

| Variable | AI_INDEX | LEGAL_WGI_SCORE | RES_INDEX | PQC |
|------------|------------:|------------:|------------:|------------:|
| AI_INDEX | 1.000000 | 0.783568 | 0.517254 | 0.840634 |
| LEGAL_WGI_SCORE | 0.783568 | 1.000000 | 0.664976 | 0.730088 |
| RES_INDEX | 0.517254 | 0.664976 | 1.000000 | 0.380787 |
| PQC | 0.840634 | 0.730088 | 0.380787 | 1.000000 |

---

# 11. Distribution Diagnostics Assumption

Observed indicators are assumed to exhibit acceptable distributional properties for comparative analysis.

## AI_INDEX

- Skewness = -0.39593851843313316
- Kurtosis = -0.9132445811266638

## LEGAL_WGI_SCORE

- Skewness = 0.18383490244953005
- Kurtosis = -0.8925871305381747

## RES_INDEX

- Skewness = 0.7807954023495343
- Kurtosis = 0.49864057599433886

## PQC

- Skewness = -0.4431250138665039
- Kurtosis = -1.0068022159176826

---

# 12. Reliability Assumption

QSSI assumes that the incorporated dimensions jointly measure a coherent latent sovereign capability construct.

## Cronbach's Alpha

| Metric | Value |
|----------|------------:|
| Alpha | 0.8785685555594794 |

### 95% Confidence Interval

```text
[0.832, 0.915]
```

Interpretation:

Excellent internal consistency across sovereign capability dimensions.

---

# 13. Latent Structure Assumption

QSSI assumes that sovereign capability possesses an underlying multidimensional latent structure.

## PCA Loadings

| Variable | PC1 | PC2 | PC3 | PC4 |
|------------|------------:|------------:|------------:|------------:|
| AI_INDEX | 0.534197 | -0.272778 | -0.351497 | 0.718802 |
| LEGAL_WGI_SCORE | 0.536276 | 0.105185 | 0.835959 | 0.050156 |
| RES_INDEX | 0.416053 | 0.816887 | -0.359197 | -0.174850 |
| PQC | 0.503926 | -0.497216 | -0.220453 | -0.670996 |

---

# 14. Composite Aggregation Assumption

QSSI assumes that sovereign capability may be represented through multidimensional additive aggregation.

\[
QSSI=\sum_{i=1}^{n}(w_iX_i)
\]

Subject to:

\[
\sum w_i = 1
\]

\[
w_i \geq 0
\]

Where:

- \(X_i\) represents normalized indicators.
- \(w_i\) represents indicator weights.

---

# 15. Weight Validation Assumption

QSSI assumes that weighting structures should be empirically evaluated rather than arbitrarily assigned.

## PCA-Derived Canonical Weights

| Variable | Weight |
|------------|------------:|
| AI_INDEX | 0.26837950 |
| LEGAL_WGI_SCORE | 0.26942446 |
| RES_INDEX | 0.20902441 |
| PQC | 0.25317163 |

## CRITIC Weights

| Variable | Weight |
|------------|------------:|
| AI_INDEX | 0.241936 |
| LEGAL_WGI_SCORE | 0.210281 |
| RES_INDEX | 0.227146 |
| PQC | 0.320637 |

## Entropy Weights

| Variable | Weight |
|------------|------------:|
| AI_INDEX | 0.290727 |
| LEGAL_WGI_SCORE | 0.234477 |
| RES_INDEX | 0.155500 |
| PQC | 0.319295 |

---

# 16. Robustness Assumption

The framework assumes that methodological robustness is supported when alternative weighting systems generate highly consistent rankings.

## Rank Correlation Comparison

### Equal Weight vs PCA

```text
Spearman ρ = 0.9992427048606825
p-value = 7.153803172038685e-126
```

### PCA vs Entropy

```text
Spearman ρ = 0.9972671523233321
p-value = 2.290322902718063e-101
```

### PCA vs CRITIC

```text
Spearman ρ = 0.998304317405441
p-value = 1.776061187692281e-110
```

Interpretation:

Extremely high ranking stability across independent weighting methodologies, indicating strong methodological robustness and ranking persistence.

---

# 17. Ranking Assumption

Countries are ranked according to descending QSSI scores.

Rankings represent comparative positioning rather than absolute measures of superiority.

Differences in rank should be interpreted as relative capability differences within the observed analytical universe.

---

# 18. Temporal Comparability Assumption

QSSI is designed to support future longitudinal comparison.

Methodological consistency is maintained through:

- Stable indicator definitions
- Stable harmonization procedures
- Stable normalization procedures
- Stable aggregation mechanisms
- Stable audit architecture
- Stable reproducibility framework

---

# 19. Reproducibility Assumption

All reported outputs are assumed computationally reproducible.

Accordingly:

- Source datasets are archived.
- Metadata are preserved.
- Computational artifacts are version-controlled.
- Statistical outputs are reproducible.
- Publication records are permanently referenced.
- Audit files are retained.
- Integrity verification records are maintained.

Independent replication should yield equivalent results.

---

# 20. Dataset Integrity Assumption

The framework assumes that archived datasets remain unchanged when verified against recorded SHA256 hashes.

## SHA256 Audit Registry

| File | SHA256 |
|----------|----------|
| AI_INDEX_2026_v1_MC_Canon.csv | 16656947ff8486b896640a00d05deccee086e52358f6614472ad38929af0b776 |
| LEGAL_WGI_2026_v1_MC_Canon.csv | 13e5310373fc4104b70b0eb410ccb1628099336f21fe705545b472290cc7b4e7 |
| RES_INDEX_2026_MC_Canon.csv | 4e936fa81a2fa2d491b897313ac136d38af431cb72f55b3adb85006bded88c9d |
| PQC_NCSI_2026_MC_Canon.csv | a421685fedadd3fb3b0b9ffbdb3822401ea4ab98098853b104f54397631cda8d |
| QSSI_MASTER_DATASET.csv | 6ac531236999faa3680978cbe09eb8c93e9ebc85e1881f937d257f873b727931 |
| QSSI_RANKINGS_2026.csv | 56681c6fcc4c89a89982b9e117beedde76f02ef4c1c473bd86079e66542d8215 |

---

# 21. FAIR+D Canon Assumption

QSSI assumes that sovereign capability assessment should satisfy FAIR+D Canon™ principles.

## FAIR+D Principles

- Findable
- Accessible
- Interoperable
- Reusable
- Defensible

---

# 22. Scope Limitation Assumption

QSSI measures sovereign capability readiness.

The framework does not directly measure:

- Military power
- Economic output
- GDP
- National wealth
- Geopolitical influence
- Ideological orientation
- Political legitimacy
- Cultural influence
- Diplomatic prestige

Interpretations outside the defined scope should be avoided.

---

# 23. Uncertainty Assumption

All empirical measurements contain uncertainty.

Accordingly:

- Measurement uncertainty exists.
- Data limitations may exist.
- Temporal variation may occur.
- Rankings should be interpreted probabilistically.
- Composite scores represent analytical estimates rather than absolute truths.

---

# 24. Interpretation Assumption

QSSI scores represent comparative sovereign capability estimates.

They are intended to support evidence-informed policy analysis, strategic assessment, sovereign benchmarking, and reproducible comparative research.

QSSI is not intended to provide deterministic judgments regarding national superiority.

---

# 25. Relationship to the Definitive Methodology

The assumptions defined herein provide the theoretical, statistical, computational, and methodological foundations supporting:

- QSSI_2026_Definitive_World_Edition.md

The methodology document specifies operational procedures, whereas the present document specifies foundational assumptions required for interpretation, implementation, replication, and application.

---

# Conclusion

The assumptions presented herein establish the formal theoretical, methodological, statistical, computational, and epistemological foundations of the Quantum-Veil Sovereignty Security Index (QSSI) 2026 Definitive World Edition.

Collectively, these assumptions support analytical transparency, methodological rigor, auditability, computational reproducibility, longitudinal consistency, robustness validation, integrity verification, and policy-grade sovereign capability assessment under the FAIR+D Canon™ Global Framework.

---

# Citation

Mazumdar, B. (2026).

*Quantum-Veil Sovereignty Security Index (QSSI) 2026 Definitive World Edition.*

Zenodo.

**Current Definitive Edition DOI:** 10.5281/zenodo.20385492

**Canonical DOI (All Versions):** 10.5281/zenodo.17302169

**ORCID:** https://orcid.org/0009-0007-5615-3558

---

###### END OF FILE
