from __future__ import annotations

import json
import hashlib
from pathlib import Path

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error,
)

DOI = "10.5281/zenodo.20007621"
ORCID = "https://orcid.org/0009-0007-5615-3558"

AUTHOR = (
    "Dr. B. Mazumdar, D.Sc. (Hon.), D.Litt. (Hon.)\n"
    "Architect of Modern Statehood\n"
    "Founder & Principal Architect, FAIR+D Canon™\n"
    "Proprietary Sovereign Systems Architecture & Governance Framework"
)

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "final" / "QVP_GLOBAL_MASTER_2026.csv"

OUTPUT_DIR = BASE_DIR / "simulation"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

FEATURES = [
    "PQC_SCORE",
    "AI_INDEX",
    "LEGAL_WGI_SCORE",
    "RES_INDEX",
]

TARGET = "QVP_GLOBAL_SCORE"

SEED = 42

df = pd.read_csv(DATA_PATH)

df.columns = [c.strip() for c in df.columns]

df = df.dropna(subset=FEATURES + [TARGET])

df = df[
    (df[FEATURES + [TARGET]] >= 0).all(axis=1)
]

df = df[
    (df[FEATURES + [TARGET]] <= 1).all(axis=1)
]

X = df[FEATURES].astype(float)

y = df[TARGET].astype(float)

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=SEED,
)

models = {
    "linear_regression": LinearRegression(),
    "ridge_regression": Ridge(alpha=1.0, random_state=SEED),
    "random_forest": RandomForestRegressor(
        n_estimators=500,
        max_depth=8,
        min_samples_split=4,
        min_samples_leaf=2,
        random_state=SEED,
    ),
}

metrics_output = {}

prediction_tables = []

feature_tables = []

best_model_name = None
best_r2 = -np.inf

for model_name, model in models.items():

    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    r2 = r2_score(y_test, preds)

    mae = mean_absolute_error(y_test, preds)

    rmse = np.sqrt(mean_squared_error(y_test, preds))

    metrics_output[model_name] = {
        "r2": float(r2),
        "mae": float(mae),
        "rmse": float(rmse),
    }

    if r2 > best_r2:
        best_r2 = r2
        best_model_name = model_name

    prediction_df = pd.DataFrame({
        "country": df.iloc[y_test.index]["country"].values,
        "actual": y_test.values,
        "predicted": preds,
        "residual": y_test.values - preds,
        "model": model_name,
    })

    prediction_tables.append(prediction_df)

    if hasattr(model, "coef_"):

        feature_df = pd.DataFrame({
            "feature": FEATURES,
            "importance": model.coef_,
            "model": model_name,
        })

    else:

        feature_df = pd.DataFrame({
            "feature": FEATURES,
            "importance": model.feature_importances_,
            "model": model_name,
        })

    feature_tables.append(feature_df)

predictions = pd.concat(prediction_tables, ignore_index=True)

feature_importance = pd.concat(feature_tables, ignore_index=True)

best_model = models[best_model_name]

full_predictions = best_model.predict(X_scaled)

final_output = df.copy()

final_output["PREDICTED_QVP_SCORE"] = full_predictions

final_output["PREDICTION_RESIDUAL"] = (
    final_output[TARGET] - final_output["PREDICTED_QVP_SCORE"]
)

final_output["SYSTEM_VERSION"] = "QSSI_PREDICT_v1.0"

final_output["DOI"] = DOI

final_output["ORCID"] = ORCID

dataset_hash = hashlib.sha256(
    pd.util.hash_pandas_object(df, index=True).values
).hexdigest()

system_hash = hashlib.sha256(
    json.dumps(metrics_output, sort_keys=True).encode()
).hexdigest()

validation_hash = hashlib.sha256(
    (dataset_hash + system_hash + "QSSI_PREDICT_v1.0").encode()
).hexdigest()

metadata = {
    "system": "QSSI Predictive Sovereign Intelligence Engine",
    "version": "v1.0",
    "doi": DOI,
    "orcid": ORCID,
    "author": AUTHOR,
    "dataset_hash": dataset_hash,
    "system_hash": system_hash,
    "validation_hash": validation_hash,
    "best_model": best_model_name,
    "metrics": metrics_output,
    "countries": int(len(df)),
    "features": FEATURES,
    "target": TARGET,
}

final_output.to_csv(
    OUTPUT_DIR / "prediction_output.csv",
    index=False,
)

predictions.to_csv(
    OUTPUT_DIR / "model_predictions.csv",
    index=False,
)

feature_importance.to_csv(
    OUTPUT_DIR / "feature_importance.csv",
    index=False,
)

with open(
    OUTPUT_DIR / "model_metrics.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(metrics_output, f, indent=4)

with open(
    OUTPUT_DIR / "system_metadata.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(metadata, f, indent=4)

latex_report = rf"""
\documentclass[11pt]{{article}}

\usepackage{{amsmath}}
\usepackage{{amssymb}}
\usepackage{{booktabs}}
\usepackage{{geometry}}
\usepackage{{longtable}}

\geometry{{margin=1in}}

\title{{QSSI Predictive Sovereign Intelligence Engine}}
\author{{{AUTHOR}}}
\date{{2026}}

\begin{document}

\maketitle

\section*{{DOI}}
{DOI}

\section*{{ORCID}}
{ORCID}

\section*{{System Definition}}

The predictive engine formalizes deterministic sovereign intelligence estimation using a multi-domain computational structure integrating:

\[
QVP = f(PQC, AI, LEGAL, RES)
\]

\section*{{Predictive Model}}

\[
\hat{{Y}} = \beta_0 + \sum_{{i=1}}^n \beta_i X_i + \varepsilon
\]

\section*{{Feature Space}}

\[
X = \{{PQC, AI, LEGAL, RES\}}
\]

\section*{{Optimization Objective}}

\[
\min \sum (Y - \hat{{Y}})^2
\]

\section*{{Evaluation Metrics}}

\[
R^2 = 1 - \frac{{\sum (y_i - \hat{{y}}_i)^2}}{{\sum (y_i - \bar{{y}})^2}}
\]

\[
MAE = \frac{{1}}{{n}} \sum |y_i - \hat{{y}}_i|
\]

\[
RMSE = \sqrt{{\frac{{1}}{{n}} \sum (y_i - \hat{{y}}_i)^2}}
\]

\section*{{Risk Constraint}}

\[
0 \leq QVP \leq 1
\]

\[
0 \leq R \leq 1
\]

\section*{{Validation Integrity}}

\[
H_d = SHA256(D)
\]

\[
H_s = SHA256(S)
\]

\[
H_v = SHA256(H_d \parallel H_s \parallel V)
\]

\section*{{Deterministic Structure}}

\[
QVP_{{adj}} = QVP_{{scaled}} \cdot (1 - R)
\]

\section*{{Empirical Objective}}

The system evaluates structural alignment between sovereign computational indicators and observable systemic resilience behavior through deterministic predictive estimation.

\section*{{Architecture Layer}}

\begin{{center}}
DATA $\rightarrow$ VALIDATION $\rightarrow$ MODEL $\rightarrow$ PREDICTION $\rightarrow$ AUDITABILITY $\rightarrow$ TRACEABILITY
\end{{center}}

\section*{{Computational Status}}

\begin{{itemize}}
\item Deterministic computation active
\item Validation layer active
\item Predictive estimation active
\item Audit traceability active
\item Sovereign scoring operational
\end{{itemize}}

\end{{document}}
"""

with open(
    OUTPUT_DIR / "predictive_engine.tex",
    "w",
    encoding="utf-8",
) as f:
    f.write(latex_report)

print(json.dumps(metadata, indent=4))
