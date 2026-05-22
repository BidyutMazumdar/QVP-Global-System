#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
QVP GLOBAL SYSTEM™ v9.0
Canonical International Sovereign Analytics Edition

International Framework for Sovereign Analytics,
Computational Governance,
and Reproducible Policy Intelligence

Canonical DOI (All Versions):
10.5281/zenodo.17302169

Authoritative Release DOI:
10.5281/zenodo.20257025

ORCID:
https://orcid.org/0009-0007-5615-3558

Author:
Dr. B. Mazumdar

Founder:
FAIR+D Canon™ — India (2025)
"""

import os
import json
import hashlib
import warnings
import random
import platform

import numpy as np
import pandas as pd

from datetime import datetime

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance

from scipy.stats import entropy
from scipy.stats import spearmanr
from scipy.spatial.distance import cdist

from statsmodels.stats.outliers_influence import variance_inflation_factor


warnings.filterwarnings("ignore")


SEED = 42

np.random.seed(SEED)
random.seed(SEED)


FRAMEWORK_NAME = "QVP GLOBAL SYSTEM™ v9.0"

FRAMEWORK_DESCRIPTION = (
    "International Framework for Sovereign Analytics, "
    "Computational Governance, and Reproducible Policy Intelligence"
)

AUTHOR = "Dr. B. Mazumdar"

ORCID = "https://orcid.org/0009-0007-5615-3558"

DOI_ALL = "10.5281/zenodo.17302169"

DOI_V9 = "10.5281/zenodo.20257025"


SUPPORTED_DATASETS = [

    "AI_INDEX_2026_v1_MC_Canon.csv",
    "LEGAL_WGI_2026_v1_MC_Canon.csv",
    "PQC_NCSI_2026_MC_Canon.csv",
    "RES_INDEX_2026_MC_Canon.csv",
    "SCI_2026_v1_MC_Canon.csv",
    "SCI_PLUS_2026_v1_MC_Canon.csv",
    "SCI_ULTRA_2026_v1_Fair+DCanon.csv"
]


def ensure_directory(path):

    os.makedirs(
        path,
        exist_ok=True
    )


def sha256_file(filepath):

    digest = hashlib.sha256()

    with open(filepath, "rb") as file:

        while True:

            chunk = file.read(8192)

            if not chunk:
                break

            digest.update(chunk)

    return digest.hexdigest()


def detect_country_column(df):

    possible_columns = [

        "Country",
        "country",
        "COUNTRY",
        "Nation",
        "STATE",
        "State"
    ]

    for column in possible_columns:

        if column in df.columns:
            return column

    return None


def load_dataset(path):

    dataframe = pd.read_csv(path)

    return dataframe


def preprocess(df):

    country_column = detect_country_column(df)

    if country_column:

        countries = df[country_column]

        X = df.drop(
            columns=[country_column]
        )

    else:

        countries = pd.Series(
            range(len(df))
        )

        X = df.copy()

    numeric_columns = X.select_dtypes(
        include=np.number
    ).columns.tolist()

    X = X[numeric_columns]

    if X.shape[1] == 0:

        raise Exception(
            "No numeric columns found in dataset"
        )

    X = X.replace(
        [np.inf, -np.inf],
        np.nan
    )

    imputer = SimpleImputer(
        strategy="median"
    )

    X_imputed = imputer.fit_transform(X)

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(
        X_imputed
    )

    processed = pd.DataFrame(
        X_scaled,
        columns=numeric_columns
    )

    processed = processed.replace(
        [np.inf, -np.inf],
        np.nan
    ).fillna(0)

    return countries, processed


def entropy_weights(df):

    scaler = MinMaxScaler()

    normalized = scaler.fit_transform(df)

    normalized = np.where(
        normalized == 0,
        1e-12,
        normalized
    )

    probability_matrix = (
        normalized /
        normalized.sum(axis=0)
    )

    entropy_values = entropy(
        probability_matrix,
        axis=0
    )

    divergence = 1 - entropy_values

    weights = divergence / divergence.sum()

    return weights


def pca_weights(df):

    if df.shape[1] == 1:

        return np.array([1.0])

    pca = PCA()

    pca.fit(df)

    explained_variance = (
        pca.explained_variance_ratio_
    )

    components = np.abs(
        pca.components_
    )

    weighted_components = np.dot(
        explained_variance,
        components
    )

    weighted_components = (
        weighted_components /
        weighted_components.sum()
    )

    return weighted_components


def hybrid_weights(df):

    entropy_weight = entropy_weights(df)

    pca_weight = pca_weights(df)

    combined_weights = (
        entropy_weight +
        pca_weight
    ) / 2

    combined_weights = (
        combined_weights /
        combined_weights.sum()
    )

    return combined_weights


def topsis(df, weights):

    matrix = df.values

    weighted_matrix = matrix * weights

    ideal_best = weighted_matrix.max(
        axis=0
    )

    ideal_worst = weighted_matrix.min(
        axis=0
    )

    distance_best = cdist(
        weighted_matrix,
        [ideal_best]
    ).flatten()

    distance_worst = cdist(
        weighted_matrix,
        [ideal_worst]
    ).flatten()

    denominator = (
        distance_best +
        distance_worst
    )

    denominator = np.where(
        denominator == 0,
        1e-12,
        denominator
    )

    score = (
        distance_worst /
        denominator
    )

    return score


def monte_carlo(
    df,
    weights,
    iterations=1000,
    noise_scale=0.01
):

    simulations = []

    for _ in range(iterations):

        noise = np.random.normal(
            0,
            noise_scale,
            df.shape
        )

        perturbed = df.values + noise

        result = topsis(
            pd.DataFrame(perturbed),
            weights
        )

        simulations.append(result)

    simulations = np.array(simulations)

    mean_scores = simulations.mean(
        axis=0
    )

    std_scores = simulations.std(
        axis=0
    )

    return mean_scores, std_scores


def bayesian_analysis(scores):

    mean_value = np.mean(scores)

    std_value = np.std(scores)

    ci_lower = (
        mean_value -
        1.96 * std_value
    )

    ci_upper = (
        mean_value +
        1.96 * std_value
    )

    return {

        "mean":
            float(mean_value),

        "std":
            float(std_value),

        "95_ci_lower":
            float(ci_lower),

        "95_ci_upper":
            float(ci_upper)
    }


def vif_analysis(df):

    if df.shape[1] < 2:

        return pd.DataFrame({

            "feature":
                df.columns,

            "VIF":
                [0.0] * len(df.columns)
        })

    cleaned_df = df.copy()

    cleaned_df = cleaned_df.loc[
        :,
        cleaned_df.std() > 0
    ]

    if cleaned_df.shape[1] < 2:

        return pd.DataFrame({

            "feature":
                cleaned_df.columns,

            "VIF":
                [0.0] * len(cleaned_df.columns)
        })

    cleaned_df = cleaned_df.replace(
        [np.inf, -np.inf],
        np.nan
    ).dropna(axis=1)

    if cleaned_df.shape[1] < 2:

        return pd.DataFrame({

            "feature":
                cleaned_df.columns,

            "VIF":
                [0.0] * len(cleaned_df.columns)
        })

    vif_values = []

    for i in range(cleaned_df.shape[1]):

        try:

            vif_score = variance_inflation_factor(
                cleaned_df.values,
                i
            )

            if np.isinf(vif_score):

                vif_score = 999999.0

            vif_values.append(
                float(vif_score)
            )

        except Exception:

            vif_values.append(0.0)

    vif_table = pd.DataFrame({

        "feature":
            cleaned_df.columns,

        "VIF":
            vif_values
    })

    return vif_table


def explainability_analysis(df, target):

    model = RandomForestRegressor(

        n_estimators=500,

        random_state=SEED
    )

    model.fit(
        df,
        target
    )

    importance = permutation_importance(

        model,

        df,

        target,

        n_repeats=10,

        random_state=SEED
    )

    result = pd.DataFrame({

        "feature":
            df.columns,

        "importance":
            importance.importances_mean
    })

    result = result.sort_values(

        by="importance",

        ascending=False
    )

    return result


def spearman_validation(rank_a, rank_b):

    correlation, p_value = spearmanr(

        rank_a,

        rank_b
    )

    return {

        "spearman_correlation":
            float(correlation),

        "p_value":
            float(p_value)
    }


def export_json(obj, path):

    with open(

        path,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            obj,

            file,

            indent=4
        )


def generate_provenance(

    output_dir,

    dataset_name
):

    provenance = {

        "framework":
            FRAMEWORK_NAME,

        "description":
            FRAMEWORK_DESCRIPTION,

        "author":
            AUTHOR,

        "orcid":
            ORCID,

        "doi_all_versions":
            DOI_ALL,

        "doi_v9_release":
            DOI_V9,

        "dataset":
            dataset_name,

        "seed":
            SEED,

        "timestamp_utc":
            datetime.utcnow().isoformat(),

        "python_version":
            platform.python_version(),

        "platform":
            platform.platform(),

        "processor":
            platform.processor()
    }

    export_json(

        provenance,

        os.path.join(

            output_dir,

            "provenance.json"
        )
    )


def generate_integrity_manifest(output_dir):

    manifest = {}

    for file in os.listdir(output_dir):

        path = os.path.join(

            output_dir,

            file
        )

        if os.path.isfile(path):

            manifest[file] = sha256_file(path)

    export_json(

        manifest,

        os.path.join(

            output_dir,

            "sha256_manifest.json"
        )
    )


def process_dataset(

    dataset_path,

    output_root
):

    dataset_name = (

        os.path.basename(dataset_path)

        .replace(".csv", "")
    )

    output_dir = os.path.join(

        output_root,

        dataset_name
    )

    ensure_directory(output_dir)

    print("=" * 100)

    print(
        f"PROCESSING DATASET: {dataset_name}"
    )

    print("=" * 100)

    dataframe = load_dataset(dataset_path)

    countries, processed = preprocess(
        dataframe
    )

    weights = hybrid_weights(
        processed
    )

    scores = topsis(
        processed,
        weights
    )

    mc_mean, mc_std = monte_carlo(
        processed,
        weights
    )

    bayesian = bayesian_analysis(
        scores
    )

    vif = vif_analysis(
        processed
    )

    explainability = explainability_analysis(
        processed,
        scores
    )

    rankings = pd.DataFrame({

        "Country":
            countries,

        "QVP_SCORE":
            scores,

        "MC_MEAN":
            mc_mean,

        "MC_STD":
            mc_std
    })

    rankings["RANK"] = rankings[
        "QVP_SCORE"
    ].rank(

        ascending=False,

        method="dense"
    )

    rankings = rankings.sort_values(

        by="QVP_SCORE",

        ascending=False
    )

    validation = spearman_validation(

        rankings["QVP_SCORE"],

        rankings["MC_MEAN"]
    )

    rankings.to_csv(

        os.path.join(

            output_dir,

            "rankings.csv"
        ),

        index=False
    )

    pd.DataFrame({

        "feature":
            processed.columns,

        "weight":
            weights

    }).to_csv(

        os.path.join(

            output_dir,

            "weights.csv"
        ),

        index=False
    )

    vif.to_csv(

        os.path.join(

            output_dir,

            "vif.csv"
        ),

        index=False
    )

    explainability.to_csv(

        os.path.join(

            output_dir,

            "shap_importance.csv"
        ),

        index=False
    )

    export_json(

        bayesian,

        os.path.join(

            output_dir,

            "bayesian_summary.json"
        )
    )

    export_json(

        validation,

        os.path.join(

            output_dir,

            "validation.json"
        )
    )

    generate_provenance(

        output_dir,

        dataset_name
    )

    generate_integrity_manifest(
        output_dir
    )

    print(
        f"COMPLETED: {dataset_name}"
    )

    print()


def execute_pipeline():

    INPUT_DIR = "."

    OUTPUT_DIR = "outputs"

    ensure_directory(
        OUTPUT_DIR
    )

    dataset_files = [

        file

        for file in os.listdir(INPUT_DIR)

        if file.endswith(".csv")
    ]

    if not dataset_files:

        raise Exception(
            "No CSV datasets found"
        )

    for file in dataset_files:

        process_dataset(

            os.path.join(

                INPUT_DIR,

                file
            ),

            OUTPUT_DIR
        )

    final_manifest = {

        "framework":
            FRAMEWORK_NAME,

        "description":
            FRAMEWORK_DESCRIPTION,

        "author":
            AUTHOR,

        "orcid":
            ORCID,

        "canonical_doi":
            DOI_ALL,

        "release_doi":
            DOI_V9,

        "processed_datasets":
            dataset_files,

        "timestamp_utc":
            datetime.utcnow().isoformat()
    }

    export_json(

        final_manifest,

        os.path.join(

            OUTPUT_DIR,

            "QVP_GLOBAL_MANIFEST.json"
        )
    )

    print("=" * 100)

    print(
        "QVP GLOBAL SYSTEM™ v9.0 EXECUTION COMPLETE"
    )

    print("=" * 100)

    print(
        "Deterministic Sovereign Analytics Engine"
    )

    print(
        "International Reproducible Governance Intelligence Framework"
    )

    print("=" * 100)

    print(
        f"Canonical DOI: {DOI_ALL}"
    )

    print(
        f"Release DOI: {DOI_V9}"
    )

    print(
        f"ORCID: {ORCID}"
    )

    print("=" * 100)


if __name__ == "__main__":

    execute_pipeline()
