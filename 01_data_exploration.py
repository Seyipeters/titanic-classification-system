"""Stage 1: exploratory data analysis and data-quality checks."""
from pathlib import Path

import pandas as pd


def main() -> None:
    data_path = Path(__file__).resolve().parent.parent / "data" / "titanic.csv"
    if not data_path.exists():
        data_path = Path("data\\titanic.csv")
    df = pd.read_csv(data_path)
    print("shape:", df.shape)
    print("target:", "survived")
    print("missing_pct:
", (df.isna().mean() * 100).round(2))
    print("dtypes:
", df.dtypes)
    print("sample:
", df.head())


if __name__ == "__main__":
    main()
