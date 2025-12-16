import numpy as np

def backtest(df, cost, target_vol, vol_lb, max_leverage, annualization):
    df = df.dropna(subset=['Strategy', 'ML_Prob', 'Returns']).copy()

    df['Risk_Scaler'] = np.where(df['ML_Prob'] < 0.3, 0.25, 1.0)
    df['Base_Position'] = df['Strategy'] * df['Risk_Scaler']

    df['Realized_Vol'] = df['Returns'].rolling(vol_lb).std() * np.sqrt(annualization)
    df['Vol_Scaler'] = (target_vol / df['Realized_Vol']).clip(0, max_leverage)

    df['Final_Position'] = df['Base_Position'] * df['Vol_Scaler']
    df['Trades'] = df['Final_Position'].diff().abs()

    df['Strategy_Returns'] = df['Returns'] * df['Final_Position'] - df['Trades'] * cost
    df['Strategy_Equity'] = (1 + df['Strategy_Returns']).cumprod()

    return df