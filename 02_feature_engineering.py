"""Stage 2: preprocessing and feature engineering."""
from pathlib import Path

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def build_features() -> tuple[pd.DataFrame, pd.Series]:
    data_path = Path(__file__).resolve().parent.parent / "data" / "titanic.csv"
    if not data_path.exists():
        data_path = Path("data\\titanic.csv")
    df = pd.read_csv(data_path)
    target = "survived"
    if target not in df.columns:
        target = df.columns[-1]

    X_raw = df.drop(columns=[target]).loc[:, df.drop(columns=[target]).isnull().mean() < 0.5]
    y = df[target]

    X = pd.DataFrame(index=X_raw.index)
    for col in X_raw.select_dtypes(include="number").columns:
        series = pd.to_numeric(X_raw[col], errors="coerce")
        X[col] = series.fillna(series.median() if not series.isna().all() else 0.0)

    for col in X_raw.select_dtypes(include=["object", "category", "bool"]).columns:
        if X_raw[col].nunique(dropna=False) > 50:
            continue
        encoder = LabelEncoder()
        X[col] = encoder.fit_transform(X_raw[col].astype(str).fillna("missing"))

    return X, y


if __name__ == "__main__":
    features, target = build_features()
    print("features:", features.shape)
    print("target:", target.shape)
