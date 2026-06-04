CODEBOOK

FAIR+D Canon™ Strategic Capability Framework

Data Dictionary and Variable Definitions

2026 Edition

Author: Dr. B. Mazumdar
ORCID: 0009-0007-5615-3558

Current Edition DOI: 10.5281/zenodo.20385492
All-Version DOI: 10.5281/zenodo.17302169

---

1. Purpose

This Codebook provides definitions, metadata, interpretation guidance, and variable descriptions for all datasets included in the FAIR+D Canon™ Strategic Capability Framework (2026 Edition).

The framework integrates artificial intelligence capability, governance quality, resilience capacity, confidence assessment, and strategic capability measurement into a unified comparative analytical system.

---

2. Dataset Inventory

Dataset| Description
SCI_2026_v1_MC_Canon| Strategic Capability Index (SCI)
SCI_PLUS_2026_v1_MC_Canon| Extended SCI including Preparedness and Quality Capacity (PQC)
AI_INDEX_2026_v1_MC_Canon| Artificial Intelligence Capability Index
LEGAL_WGI_2026_v1_MC_Canon| Governance and Institutional Quality Index
PQC_NCSI_2026_MC_Canon| Preparedness and Quality Capacity Dataset
RES_INDEX_2026_MC_Canon| National Resilience Capacity Index
SCI_ULTRA_2026_v1_Fair+DCanon| Confidence-Adjusted Strategic Capability Framework

---

3. Variable Definitions

SCI_2026_v1_MC_Canon

country

Country or territory name.

Type: String

---

oecd_ai

Normalized OECD Artificial Intelligence indicator.

Range: 0–1

Higher values indicate stronger AI readiness.

---

oxford_ai

Normalized Oxford AI Governance indicator.

Range: 0–1

Higher values indicate stronger AI governance capacity.

---

AI_INDEX

Composite Artificial Intelligence Capability Index.

Range: 0–1

Interpretation:

Higher values indicate greater national AI capability.

---

rule_of_law

Normalized Rule of Law indicator.

Source:

Worldwide Governance Indicators (WGI)

Range: 0–1

---

regulatory_quality

Normalized Regulatory Quality indicator.

Source:

Worldwide Governance Indicators (WGI)

Range: 0–1

---

government_effectiveness

Normalized Government Effectiveness indicator.

Source:

Worldwide Governance Indicators (WGI)

Range: 0–1

---

control_of_corruption

Normalized Control of Corruption indicator.

Source:

Worldwide Governance Indicators (WGI)

Range: 0–1

---

LEGAL_WGI_SCORE

Composite Governance Quality Index.

Constructed from:

- Rule of Law
- Regulatory Quality
- Government Effectiveness
- Control of Corruption

Range: 0–1

Higher values indicate stronger institutional quality.

---

SCI_SCORE

Strategic Capability Index.

Constructed from:

- AI_INDEX
- LEGAL_WGI_SCORE

Range: 0–1

Higher values indicate stronger combined technological and governance capability.

---

rank

Country ranking based on SCI_SCORE.

Lower rank number indicates stronger performance.

---

4. SCI_PLUS Variables

All SCI variables plus:

PQC

Preparedness and Quality Capacity indicator.

Range: 0–1

Measures preparedness, institutional readiness, and quality capacity.

---

SCI_PLUS_SCORE

Extended Strategic Capability Score.

Combines:

- AI capability
- Governance quality
- Preparedness capacity

Range: 0–1

---

5. AI_INDEX Dataset Variables

oecd_ai

OECD AI indicator.

oxford_ai

Oxford AI indicator.

AI_INDEX

Composite AI capability score.

rank

AI capability ranking.

---

6. LEGAL_WGI Dataset Variables

rule_of_law

Rule of Law indicator.

regulatory_quality

Regulatory Quality indicator.

government_effectiveness

Government Effectiveness indicator.

control_of_corruption

Control of Corruption indicator.

LEGAL_WGI_SCORE

Composite governance quality measure.

rank

Governance ranking.

---

7. RES_INDEX Dataset Variables

imf_res

IMF resilience indicator.

Range: 0–1

---

ndgain_res

ND-GAIN resilience indicator.

Range: 0–1

---

global_resilience

Global resilience indicator.

Range: 0–1

---

RES_INDEX

Composite resilience score.

Range: 0–1

Higher values indicate stronger resilience and adaptive capacity.

---

8. PQC Dataset Variables

Country

Country name.

PQC

Preparedness and Quality Capacity score.

Range: 0–1

---

9. SCI_ULTRA Dataset Variables

SCI_ULTRA_SCORE

Integrated strategic capability score.

Components include:

- AI capability
- Governance quality
- Resilience
- Preparedness

Range: 0–1

---

confidence_score

Evidence-confidence adjustment factor.

Range observed:

0.30–1.00

Interpretation:

Higher values indicate greater data completeness, coverage, and reliability.

---

SCI_ADJUSTED_SCORE

Confidence-adjusted capability score.

Range: 0–1

Used for adjusted ranking calculations.

---

rank_raw

Original ranking based on SCI_ULTRA_SCORE.

---

rank_adjusted

Ranking after confidence adjustment.

---

rank_gap

Difference between adjusted and raw rankings.

Formula:

rank_adjusted − rank_raw

Interpretation:

Negative values indicate ranking improvement.

Positive values indicate ranking decline after adjustment.

---

capability_tier

Categorical capability classification.

Categories:

- High Capability
- Upper-Mid
- Mid
- Emerging / Fragile

---

confidence_level

Confidence classification.

Categories:

- High Confidence
- Moderate Confidence
- Low Confidence

---

risk_flag

Binary risk indicator.

Values:

- FALSE = No risk threshold exceeded
- TRUE = Risk threshold exceeded

---

10. Score Interpretation Guide

Score Range| Interpretation
0.80–1.00| Very High Capability
0.60–0.79| High Capability
0.40–0.59| Moderate Capability
0.20–0.39| Emerging Capability
Below 0.20| Fragile Capability

---

11. Statistical Validation Reference

The framework was validated using:

- Correlation Analysis
- Ordinary Least Squares Regression
- Multiple Regression
- Variance Inflation Factor (VIF)
- Bootstrap Confidence Intervals
- Sensitivity Analysis
- Spearman Rank Robustness Testing
- Shapiro–Wilk Distribution Testing
- Cook's Distance Outlier Diagnostics

Validation results are documented in:

"reports/validation_analysis.md"

---

12. Citation

Mazumdar, B. (2026).

FAIR+D Canon™ Strategic Capability Framework (SCI, SCI+, SCI ULTRA).

DOI: 10.5281/zenodo.20385492

ORCID: 0009-0007-5615-3558

---

Version: 2026 Edition (v1.0)

End of Codebook.
