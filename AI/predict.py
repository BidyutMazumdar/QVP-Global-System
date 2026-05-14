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

DOI = "10.5281/zenodo.20127955"
ORCID = "https://orcid.org/0009-0007-5615-3558"

AUTHOR = """Dr. B. Mazumdar, D.Sc. (Hon.), D.Litt. (Hon.)
Architect of Modern Statehood
Founder & Principal Architect, FAIR+D Canon™
Proprietary Sovereign Systems Architecture & Governance Framework"""

SYSTEM_NAME = "QSSI Predictive Sovereign Intelligence Engine"
SYSTEM_VERSION = "QSSI_PREDICT_v1.0"

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

np.random.seed(SEED)

df = pd.read_csv(DATA_PATH)
df.columns = [c.strip() for c in df.columns]

required_cols = FEATURES + [TARGET]

df = df.dropna(subset=required_cols).copy()

df = df[
    (df[required_cols] >= 0).all(axis=1)
]

df = df[
    (df[required_cols] <= 1).all(axis=1)
]

if "country" not in df.columns:
    df["country"] = ""

df["country"] = (
    df["country"]
    .fillna("")
    .astype(str)
    .str.strip()
)

X = df[FEATURES].astype(float)
y = df[TARGET].astype(float)

X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=SEED,
    shuffle=True,
)

scaler = MinMaxScaler()

X_train = pd.DataFrame(
    scaler.fit_transform(X_train_raw),
    columns=FEATURES,
    index=X_train_raw.index,
)

X_test = pd.DataFrame(
    scaler.transform(X_test_raw),
    columns=FEATURES,
    index=X_test_raw.index,
)

X_scaled = pd.DataFrame(
    scaler.transform(X),
    columns=FEATURES,
    index=df.index,
)

scaler_metadata = {
    "min": scaler.data_min_.tolist(),
    "max": scaler.data_max_.tolist(),
}

models = {
    "linear_regression": LinearRegression(),
    "ridge_regression": Ridge(
        alpha=1.0
    ),
    "random_forest": RandomForestRegressor(
        n_estimators=500,
        max_depth=8,
        min_samples_split=4,
        min_samples_leaf=2,
        random_state=SEED,
        n_jobs=-1,
        bootstrap=True,
        oob_score=True,
    ),
}

metrics_output = {}
prediction_tables = []
feature_tables = []

best_model_name = None
best_r2 = -np.inf

for model_name, model in models.items():

    model.fit(
        X_train,
        y_train,
    )

    preds = model.predict(
        X_test
    )

    r2 = float(
        r2_score(
            y_test,
            preds,
        )
    )

    mae = float(
        mean_absolute_error(
            y_test,
            preds,
        )
    )

    rmse = float(
        np.sqrt(
            mean_squared_error(
                y_test,
                preds,
            )
        )
    )

    metrics_output[model_name] = {
        "r2": r2,
        "mae": mae,
        "rmse": rmse,
    }

    if model_name == "random_forest":
        metrics_output[
            model_name
        ]["oob_score"] = float(
            model.oob_score_
        )

    if r2 > best_r2:
        best_r2 = r2
        best_model_name = model_name

    prediction_df = pd.DataFrame(
        {
            "iso3": (
                df.loc[
                    y_test.index,
                    "iso3",
                ].values
                if "iso3" in df.columns
                else ""
            ),
            "country": df.loc[
                y_test.index,
                "country",
            ].values,
            "actual": y_test.values,
            "predicted": preds,
            "residual": (
                y_test.values
                - preds
            ),
            "model": model_name,
        },
        index=y_test.index,
    )

    prediction_tables.append(
        prediction_df
    )

    if hasattr(
        model,
        "coef_",
    ):
        importance = np.asarray(
            model.coef_,
            dtype=float,
        )
    else:
        importance = np.asarray(
            model.feature_importances_,
            dtype=float,
        )

    feature_tables.append(
        pd.DataFrame(
            {
                "feature": FEATURES,
                "importance": importance,
                "model": model_name,
            }
        )
    )

assert best_model_name is not None

best_model = models[
    best_model_name
]

full_predictions = best_model.predict(
    X_scaled
)

final_output = df.copy()

final_output[
    "PREDICTED_QVP_SCORE"
] = full_predictions

final_output[
    "PREDICTED_QVP_SCORE"
] = final_output[
    "PREDICTED_QVP_SCORE"
].clip(
    0.0,
    1.0,
)

final_output[
    "PREDICTION_RESIDUAL"
] = (
    final_output[TARGET]
    - final_output[
        "PREDICTED_QVP_SCORE"
    ]
)

final_output[
    "SYSTEM_VERSION"
] = SYSTEM_VERSION

final_output[
    "DOI"
] = DOI

final_output[
    "ORCID"
] = ORCID

assert final_output[
    "PREDICTED_QVP_SCORE"
].between(
    0.0,
    1.0,
).all()

assert final_output[
    "PREDICTION_RESIDUAL"
].notna().all()

predictions = pd.concat(
    prediction_tables,
    ignore_index=True,
)

feature_importance = pd.concat(
    feature_tables,
    ignore_index=True,
)

dataset_hash = hashlib.sha256(
    DATA_PATH.read_bytes()
).hexdigest()

system_hash = hashlib.sha256(
    json.dumps(
        metrics_output,
        sort_keys=True,
    ).encode(
        "utf-8"
    )
).hexdigest()

prediction_hash = hashlib.sha256(
    final_output.to_csv(
        index=False
    ).encode(
        "utf-8"
    )
).hexdigest()

validation_hash = hashlib.sha256(
    (
        dataset_hash
        + system_hash
        + prediction_hash
        + SYSTEM_VERSION
    ).encode(
        "utf-8"
    )
).hexdigest()

model_ranking = sorted(
    metrics_output.items(),
    key=lambda x: x[1]["r2"],
    reverse=True,
)

metadata = {
    "system": SYSTEM_NAME,
    "version": SYSTEM_VERSION,
    "doi": DOI,
    "orcid": ORCID,
    "author": AUTHOR,
    "dataset_hash": dataset_hash,
    "system_hash": system_hash,
    "prediction_hash": prediction_hash,
    "validation_hash": validation_hash,
    "best_model": best_model_name,
    "model_ranking": model_ranking,
    "metrics": metrics_output,
    "countries": int(
        len(df)
    ),
    "features": FEATURES,
    "target": TARGET,
    "scaler": scaler_metadata,
}

final_output.to_csv(
    OUTPUT_DIR
    / "prediction_output.csv",
    index=False,
)

predictions.to_csv(
    OUTPUT_DIR
    / "model_predictions.csv",
    index=False,
)

feature_importance.to_csv(
    OUTPUT_DIR
    / "feature_importance.csv",
    index=False,
)

with open(
    OUTPUT_DIR
    / "model_metrics.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(
        metrics_output,
        f,
        indent=4,
        ensure_ascii=False,
    )

with open(
    OUTPUT_DIR
    / "system_metadata.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(
        metadata,
        f,
        indent=4,
        ensure_ascii=False,
    )

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

\begin{{document}}

\maketitle

\section*{{DOI}}
{DOI}

\section*{{ORCID}}
{ORCID}

\section*{{System Definition}}

\[
QVP = f(PQC, AI, LEGAL, RES)
\]

\section*{{Predictive Model}}

\[
\hat{{Y}} =
\beta_0
+
\sum_{{i=1}}^n
\beta_i X_i
+
\varepsilon
\]

\section*{{Feature Space}}

\[
X =
\{{
PQC,
AI,
LEGAL,
RES
}}
\]

\section*{{Optimization Objective}}

\[
\min
\sum
(
Y
-
\hat{{Y}}
)^2
\]

\section*{{Evaluation Metrics}}

\[
R^2
=
1
-
\frac
{{
\sum
(
y_i
-
\hat{{y}}_i
)^2
}}
{{
\sum
(
y_i
-
\bar{{y}}
)^2
}}
\]

\[
MAE
=
\frac{{1}}{{n}}
\sum
|y_i
-
\hat{{y}}_i|
\]

\[
RMSE
=
\sqrt
{{
\frac{{1}}{{n}}
\sum
(
y_i
-
\hat{{y}}_i
)^2
}}
\]

\section*{{Constraint Space}}

\[
0
\leq
QVP
\leq
1
\]

\[
0
\leq
R
\leq
1
\]

\section*{{Integrity Validation}}

\[
H_d
=
SHA256(D)
\]

\[
H_s
=
SHA256(S)
\]

\[
H_p
=
SHA256(P)
\]

\[
H_v
=
SHA256
(
H_d
\parallel
H_s
\parallel
H_p
\parallel
V
)
\]

\section*{{Deterministic Adjustment}}

\[
QVP_{{adj}}
=
QVP_{{scaled}}
\cdot
(
1
-
R
)
\]

\section*{{Architecture}}

\[
DATA
\rightarrow
VALIDATION
\rightarrow
NORMALIZATION
\rightarrow
MODEL
\rightarrow
PREDICTION
\rightarrow
AUDITABILITY
\rightarrow
TRACEABILITY
\]

\section*{{Operational Status}}

\begin{{itemize}}
\item Deterministic computation active
\item Predictive estimation active
\item Feature normalization active
\item Validation integrity active
\item Output auditability active
\item Sovereign scoring operational
\end{{itemize}}

\end{{document}}
"""

with open(
    OUTPUT_DIR
    / "predictive_engine.tex",
    "w",
    encoding="utf-8",
) as f:
    f.write(
        latex_report
    )

print(
    json.dumps(
        metadata,
        indent=4,
        ensure_ascii=False,
    )
)
