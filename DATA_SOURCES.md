# QSSI™ Data Sources (v2026.1.1)

This document defines the authoritative data sources used in the QSSI™ model.

---

## 1. PQC (Cybersecurity Proxy)

Source: ITU Global Cybersecurity Index (2024)

Variable:
- GCI Score (0–1)

Mapping:
PQC ≈ National cybersecurity readiness including cryptographic capacity.

---

## 2. AI Governance

Source: Oxford Insights – Government AI Readiness Index (2024)

Variable:
- AI Readiness Score (0–100)

Normalization:
AI = Score / 100

---

## 3. LEGAL Infrastructure

Source: World Bank – Worldwide Governance Indicators (WGI) (2024)

Variables:
- Rule of Law
- Regulatory Quality

Normalization:
LEGAL = (Value + 2.5) / 5

---

## 4. Systemic Resilience (RES)

Source: IMF – Financial Soundness Indicators (2024)

Variables:
- Bank capital adequacy
- Financial system stability metrics

Mapping:
RES ≈ Financial and systemic resilience capacity

---

## 5. Risk Variable

Derived from:
- Political Stability (WGI)
- Economic Volatility (IMF)
- Governance uncertainty

---

## 6. Notes

- All variables normalized to [0,1]
- Dataset is reproducible given identical inputs
- No synthetic adjustments beyond normalization
