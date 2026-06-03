# QSSI 2026 Formal Assumptions

## Quantum-Veil Sovereignty Security Index (QSSI)

### FAIR+D Canon™ Global Framework

#### Current Definitive Edition DOI

10.5281/zenodo.20385492

#### All Versions DOI

10.5281/zenodo.17302169

#### Author

Dr. B. Mazumdar, D.Sc. (Hon.), D.Litt. (Hon.)

#### ORCID

https://orcid.org/0009-0007-5615-3558

#### Founder

FAIR+D Canon™ (India, 2025)

#### Document Classification

Formal Theoretical and Methodological Assumptions

#### Framework Status

Definitive World Edition (2026)

---

# Abstract

This document presents the formal theoretical, statistical, computational, methodological, and epistemological assumptions underlying the Quantum-Veil Sovereignty Security Index (QSSI) 2026 Definitive World Edition.

The assumptions establish the foundational conditions required for the rigorous measurement of sovereign capability across Artificial Intelligence Capacity, Governance and Legal Quality, National Resilience Capacity, and Post-Quantum Cybersecurity Readiness.

Together, these assumptions support methodological transparency, analytical defensibility, reproducibility, longitudinal comparability, and policy-grade interpretation under the FAIR+D Canon™ Global Framework.

---

# 1. Sovereign Entity Assumption

QSSI assumes that sovereign nation-states constitute the appropriate analytical unit for comparative capability assessment.

Each country is treated as an independent sovereign observation.

The framework excludes:

- Subnational jurisdictions
- Municipal entities
- Corporate organizations
- International alliances
- Non-state actors
- Private institutions

The sovereign state remains the sole unit of analysis.

---

# 2. Dataset Validity Assumption

QSSI assumes that all incorporated datasets provide valid empirical representations of their intended strategic capability domains.

### Source Datasets

| Dimension | Dataset | Coverage |
|------------|------------|------------|
| Artificial Intelligence Capability | AI_INDEX_2026 | 195 Countries |
| Governance & Legal Quality | LEGAL_WGI_2026 | 213 Countries |
| National Resilience Capacity | RES_INDEX_2026 | 181 Countries |
| Post-Quantum Cybersecurity Readiness | PQC_NCSI_2026 | 124 Countries |

Each dataset is assumed to possess sufficient informational validity, institutional credibility, and measurement consistency for sovereign capability assessment.

---

# 3. Country Harmonization Assumption

Country identifiers originating from heterogeneous international sources may differ in naming conventions.

QSSI assumes that harmonization procedures correctly identify equivalent sovereign entities across all datasets.

### Examples

- United States of America → United States
- United Kingdom of Great Britain and Northern Ireland → United Kingdom
- Republic of Korea → South Korea
- Czechia → Czech Republic

Following harmonization:

- Initial Common Countries = 87
- Final Common Countries = 91

The framework assumes that harmonization preserves analytical validity and cross-source consistency.

---

# 4. Completeness Assumption

Only sovereign entities possessing valid observations across all four strategic dimensions are retained.

Countries with incomplete observations are excluded from composite index construction.

### Dataset Coverage

- AI = 195 Countries
- LEGAL = 213 Countries
- RES = 181 Countries
- PQC = 124 Countries

### Final Analytical Sample

**N = 91 Sovereign Entities**

The retained sample is assumed to remain sufficiently representative for comparative sovereign assessment.

---

# 5. Indicator Independence Assumption

QSSI assumes that individual dimensions measure related yet non-identical aspects of sovereign capability.

Indicators may exhibit moderate correlation while maintaining distinct informational contributions.

The framework therefore assumes:

- Partial dependence is acceptable.
- Complete redundancy is absent.
- Each dimension contributes unique analytical value.

---

# 6. Normalization Assumption

Because indicators originate from heterogeneous scales, units, and measurement systems, QSSI applies Min-Max normalization.

### Transformation

X_norm = (X − X_min) / (X_max − X_min)

### Constraint

0 ≤ X ≤ 1

The framework assumes that Min-Max normalization preserves ordinal relationships and relative positioning among sovereign entities.

---

# 7. Monotonicity Assumption

QSSI assumes that increasing indicator values correspond to increasing sovereign capability.

Accordingly:

- Higher AI_INDEX values indicate stronger AI capability.
- Higher LEGAL_WGI_SCORE values indicate stronger governance quality.
- Higher RES_INDEX values indicate stronger resilience capacity.
- Higher PQC values indicate stronger post-quantum readiness.

No incorporated indicator is interpreted inversely.

---

# 8. Composite Aggregation Assumption

QSSI assumes that sovereign capability may be represented through multidimensional aggregation.

The composite structure is defined as:

QSSI = Σ(wᵢXᵢ)

Subject to:

Σwᵢ = 1

wᵢ ≥ 0

where:

- Xᵢ represents normalized indicators.
- wᵢ represents indicator weights.

The framework assumes additive contribution across dimensions.

---

# 9. Weight Validation Assumption

QSSI assumes that weighting structures should be empirically evaluated rather than arbitrarily assigned.

Four weighting frameworks were examined:

1. Equal Weight
2. PCA Weight
3. Entropy Weight
4. CRITIC Weight

### PCA Weights

- AI_INDEX = 0.277213
- LEGAL_WGI_SCORE = 0.281636
- RES_INDEX = 0.160179
- PQC = 0.280972

### Entropy Weights

- AI_INDEX = 0.244018
- LEGAL_WGI_SCORE = 0.261042
- RES_INDEX = 0.281391
- PQC = 0.213550

### CRITIC Weights

- AI_INDEX = 0.218814
- LEGAL_WGI_SCORE = 0.201191
- RES_INDEX = 0.289561
- PQC = 0.290434

Cross-method comparison is assumed to improve robustness and methodological defensibility.

---

# 10. Latent Structure Assumption

Principal Component Analysis (PCA) identified a dominant common capability structure.

### Explained Variance

- PC1 = 0.779325
- PC2 = 0.142224
- PC3 = 0.041180
- PC4 = 0.037271

The framework assumes that sovereign capability possesses an underlying latent multidimensional structure.

---

# 11. Ranking Assumption

Countries are ranked according to descending QSSI scores.

The framework assumes that ordinal ranking provides meaningful comparative interpretation of sovereign capability.

Rank differences should be interpreted as relative rather than absolute measures of superiority.

---

# 12. Temporal Comparability Assumption

QSSI is designed for future longitudinal comparison.

To minimize methodological drift, the framework assumes stability in:

- Indicator definitions
- Harmonization procedures
- Normalization procedures
- Aggregation mechanisms
- Canonical methodological architecture

This assumption supports cross-edition comparability.

---

# 13. Reproducibility Assumption

All reported outputs are assumed computationally reproducible.

Accordingly:

- Source datasets are archived.
- Metadata are preserved.
- Manifests are documented.
- Methodological artifacts are version-controlled.
- Publication records are permanently referenced.

Independent replication should yield equivalent results.

---

# 14. FAIR+D Canon Assumption

QSSI assumes that sovereign capability assessment should satisfy FAIR+D Canon™ principles.

### FAIR+D Principles

- Findable
- Accessible
- Interoperable
- Reusable
- Defensible

All methodological decisions are evaluated against these principles.

---

# 15. Scope Limitation Assumption

QSSI measures sovereign capability readiness.

The framework does not directly measure:

- Military power
- Economic output
- Gross Domestic Product (GDP)
- National wealth
- Geopolitical influence
- Ideological orientation
- Political legitimacy
- Cultural influence

Interpretations outside the defined capability scope should be avoided.

---

# 16. Uncertainty Assumption

QSSI assumes that all empirical measurements contain uncertainty.

Observed values represent estimates derived from available information rather than absolute truths.

Accordingly:

- Measurement uncertainty exists.
- Data limitations may exist.
- Temporal variation may occur.
- Rankings should be interpreted probabilistically.

---

# 17. Interpretation Assumption

QSSI scores represent comparative sovereign capability estimates.

They should be interpreted as structured analytical indicators designed to support evidence-informed decision making.

QSSI is not intended to provide deterministic judgments regarding national superiority.

---

# Relationship to the Definitive Methodology

The assumptions defined herein provide the theoretical and methodological foundations supporting the implementation procedures described in:

- QSSI_2026_Definitive_World_Edition.md

The methodology document specifies operational procedures, whereas the present document specifies the underlying assumptions required for interpretation and application.

# Conclusion

The assumptions presented herein establish the formal theoretical, methodological, statistical, and computational foundations of the Quantum-Veil Sovereignty Security Index (QSSI) 2026 Definitive World Edition.

Collectively, these assumptions support methodological rigor, analytical transparency, computational reproducibility, longitudinal consistency, and policy-grade sovereign capability assessment under the FAIR+D Canon™ Global Framework.

---

# Citation

Mazumdar, B. (2026).

*Quantum-Veil Sovereignty Security Index (QSSI) 2026 Definitive World Edition.*

Zenodo.

Current DOI: 10.5281/zenodo.20385492

All Versions DOI: 10.5281/zenodo.17302169

ORCID: 0009-0007-5615-3558

---

###### END OF FILE
