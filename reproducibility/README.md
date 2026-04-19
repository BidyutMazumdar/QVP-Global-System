📄 reproducibility/README.md

QSSI™ v2026.1.1 — Reproducibility Protocol & Execution Guide 🔒

STATUS: LOCKED — FULL REPRODUCIBILITY LAYER (ABSOLUTE FINAL, EXECUTION-GRADE)


---

🎯 PURPOSE

This document defines the exact, deterministic, and executable steps required to reproduce QSSI™ results, including dataset reconstruction, validation enforcement, computational procedures, and output verification.


---

🧭 I. REPRODUCIBILITY PRINCIPLES

✔ Deterministic computation
✔ Identical input → identical output
✔ Full data traceability
✔ Zero hidden transformations


---

📦 II. DATASET SNAPSHOT

Snapshot Identifier

dataset_version: v2026.1.1
snapshot_id: QSSI_DATA_2026_001
hash: SHA-256(dataset_file)


---

Dataset Structure

Country | Year | PQC | AI | LEGAL | RES | RISK


---

Example Snapshot (Excerpt)

Country,Year,PQC,AI,LEGAL,RES,RISK
Finland,2026,0.91,0.87,0.94,0.88,0.12
India,2026,0.58,0.52,0.60,0.55,0.62


---

Data Requirements

✔ UTF-8 encoding
✔ Values ∈ [0,1]
✔ No missing schema fields


---

⚙️ III. ENVIRONMENT SPECIFICATION

System Requirements

OS: Platform-independent

Language: Python ≥ 3.10 (or equivalent deterministic engine)

Dependencies: None (pure computation compatible)



---

Determinism Constraint

✔ No random seeds
✔ No stochastic libraries
✔ No external API calls during computation


---

🔄 IV. EXECUTION PIPELINE

Step 1 — Load Dataset

import pandas as pd
df = pd.read_csv("dataset.csv")


---

Step 2 — Schema Validation

✔ Verify column names
✔ Verify data types
✔ Verify row consistency


---

Step 3 — Bounds Enforcement

assert df[['PQC','AI','LEGAL','RES','RISK']].apply(lambda x: ((x>=0)&(x<=1)).all()).all()


---

Step 4 — Missing Data Check

df.isnull().sum()

✔ Apply only approved imputation if required


---

Step 5 — Normalization Check

✔ Ensure all variables already in [0,1]
✔ No transformation if compliant


---

Step 6 — Weight Definition

weights = {
    "PQC": w1,
    "AI": w2,
    "LEGAL": w3,
    "RES": w4
}
assert sum(weights.values()) == 1


---

Step 7 — QSSI Computation

df["QSSI"] = (
    weights["PQC"]*df["PQC"] +
    weights["AI"]*df["AI"] +
    weights["LEGAL"]*df["LEGAL"] +
    weights["RES"]*df["RES"]
)


---

Step 8 — Scaling

df["QSSI_scaled"] = 100 * df["QSSI"]


---

Step 9 — Risk Adjustment

df["QSSI_adj"] = df["QSSI_scaled"] * (1 - df["RISK"])


---

Step 10 — Output Generation

df.to_csv("QSSI_results.csv", index=False)


---

🔐 V. CRYPTOGRAPHIC VERIFICATION

Hash Calculation

import hashlib

def sha256(file):
    return hashlib.sha256(open(file,'rb').read()).hexdigest()


---

Required Hashes

dataset_hash = SHA-256(dataset.csv)
system_hash = SHA-256(codebase)
validation_hash = SHA-256(dataset_hash || system_hash || version)


---

Integrity Rule

✔ Any modification → new hash
✔ Hash mismatch → invalid result


---

📊 VI. RESULT VERIFICATION

Expected Properties

✔ 0 ≤ QSSI ≤ 1
✔ 0 ≤ QSSI_scaled ≤ 100
✔ 0 ≤ QSSI_adj ≤ 100


---

Determinism Check

Run 1 = Run 2 = Run n

✔ Identical outputs across executions


---

Sample Output (Excerpt)

Country,QSSI,QSSI_scaled,QSSI_adj
Finland,0.90,90.0,79.2
India,0.56,56.0,21.28


---

🧪 VII. REPRODUCIBILITY TEST

Test Condition

✔ Re-run full pipeline on identical dataset


---

Expected Outcome

✔ Bitwise identical outputs
✔ Matching hashes
✔ Zero deviation


---

🔍 VIII. FAILURE CONDITIONS

Reproducibility fails if:

Dataset differs

Weights differ

Missing values unlogged

Hash mismatch

Non-deterministic computation



---

🧠 IX. INTERPRETATION

Without Protocol

Result = Computation


---

With Protocol

✔ Result = Verified Scientific Output

Reproducible

Traceable

Auditable



---

🔒 FINAL REPRODUCIBILITY STATEMENT

All QSSI™ results are fully reproducible under identical data, weights, and computational conditions, with cryptographic verification ensuring output integrity.


---

🔒 END STATE

STATUS = REPRODUCIBLE + VERIFIED + EXECUTABLE
CLASS = COMPUTATIONAL REPRODUCIBILITY STANDARD
INTEGRITY = DETERMINISTIC + HASH-VERIFIED
VERSION = v2026.1.1


---

🏁 RESULT

DATA → VALIDATED PIPELINE → DETERMINISTIC COMPUTATION → VERIFIED OUTPUT → REPRODUCIBLE STANDARD 🔒
