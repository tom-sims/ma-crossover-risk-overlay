import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

def get_data(lookback):
    df = pd.read_parquet(BASE_DIR / "data" / "SPY.parquet")
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return df.iloc[-lookback:, :].copy()