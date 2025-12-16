import numpy as np

def add_moving_averages(df, fast, slow):
    df[f'{fast}_ma'] = df['Close'].rolling(fast).mean()
    df[f'{slow}_ma'] = df['Close'].rolling(slow).mean()
    return df

def add_features(df, fast, slow):
    df['Returns'] = df['Close'].pct_change()
    df['ma_diff'] = df[f'{fast}_ma'] - df[f'{slow}_ma']
    df['ma_diff_pct'] = df['ma_diff'] / df['Close']
    df['fast_slope'] = df[f'{fast}_ma'].diff()
    df['slow_slope'] = df[f'{slow}_ma'].diff()
    df['vol_20'] = df['Returns'].rolling(20).std()
    df['vol_60'] = df['Returns'].rolling(60).std()
    return df