import numpy as np

def performance_metrics(df, annualization):
    strat_ret = df['Strategy_Returns']
    cagr = df['Strategy_Equity'].iloc[-1] ** (annualization / len(strat_ret)) - 1
    vol = strat_ret.std() * np.sqrt(annualization)
    sharpe = cagr / vol if vol != 0 else np.nan
    drawdown = df['Strategy_Equity'] / df['Strategy_Equity'].cummax() - 1

    return {
        'CAGR': cagr,
        'Volatility': vol,
        'Sharpe': sharpe,
        'Max_Drawdown': drawdown.min(),
        'Trades': df['Trades'].sum()
    }