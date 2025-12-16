import matplotlib.pyplot as plt

from src.data_loader import get_data
from src.features import add_moving_averages, add_features
from src.strategy import add_strategy
from src.ml import add_regime_label, train_regime_model
from src.backtest import backtest
from src.metrics import performance_metrics

TICKER = 'SPY'
FAST = 20
SLOW = 200
LOOKBACK = 4000

COST_PER_TRADE = 0.0005
ANNUALIZATION = 252

REGIME_LOOKAHEAD = 20
NEG_RETURN_TOL = -0.01
TRAIN_SPLIT = 0.7

TARGET_VOL = 0.10
VOL_LOOKBACK = 20
MAX_LEVERAGE = 1.5

FEATURE_COLS = [
    'ma_diff_pct',
    'fast_slope',
    'slow_slope',
    'vol_20',
    'vol_60'
]

def main():
    df = get_data(LOOKBACK)

    df = add_moving_averages(df, FAST, SLOW)
    df = add_strategy(df, FAST, SLOW)

    df = add_features(df, FAST, SLOW)
    df = add_regime_label(df, REGIME_LOOKAHEAD, NEG_RETURN_TOL)

    df, model = train_regime_model(df, FEATURE_COLS, TRAIN_SPLIT)

    df = backtest(
        df,
        cost=COST_PER_TRADE,
        target_vol=TARGET_VOL,
        vol_lb=VOL_LOOKBACK,
        max_leverage=MAX_LEVERAGE,
        annualization=ANNUALIZATION
    )

    metrics = performance_metrics(df, ANNUALIZATION)

    print("\nPERFORMANCE METRICS")
    for k, v in metrics.items():
        print(f"{k:15}: {v:.4f}")

    df['BuyHold_Equity'] = (1 + df['Returns']).cumprod()

    plt.figure(figsize=(10, 5))
    plt.plot(df['BuyHold_Equity'] - 1, label=f'{TICKER} Buy & Hold')
    plt.plot(df['Strategy_Equity'] - 1, label='My Stratergy')
    plt.legend()
    plt.title('MA + ML Risk Control + Volatility Targeting')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()