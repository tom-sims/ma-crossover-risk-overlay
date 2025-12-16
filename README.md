# Moving Average Crossover with ML Risk Control & Volatility Targeting

## Overview

This project explores a simple moving average crossover strategy on SPY and gradually extends it to study how machine learning and risk management techniques affect performance.

The goal of the project was not to build a profitable trading system, but to better understand:

   - Where basic trend-following strategies break down

   - How machine learning can be applied in a realistic way

   - Why risk management often matters more than signal quality

The final strategy focuses on reducing risk and drawdowns rather than maximizing returns.

## How to run:

- Create a virtual environment:
  
      python3 -m venv venv
  
      source venv/bin/activate
  
- Install dependencies:
  
      pip install -r requirements.txt
  
- Provide your own SPY.parquet data in the data folder
  
- Run
  
      python main.py


## First Strategy: Moving Average Crossover

The project started with a standard moving average crossover strategy:

   - A fast and a slow moving average are calculated on price

   - The strategy goes long when the fast MA is above the slow MA

   - It stays out of the market otherwise

   - Signals are shifted forward by one day to avoid lookahead bias

This type of strategy is commonly used as a basic trend-following example.

Observations:

   - The strategy captures long-term market trends reasonably well

   - It experiences large drawdowns during market crashes

   - Performance varies significantly depending on market conditions

This reinforced a common idea in quantitative finance: Trend-following can work, but risk management is critical.

## Initial ML Approach: Regime Classification

The next step was to test whether machine learning could help identify market regimes where trend-following performs better.

Approach:

   - Created features such as moving average slopes, MA distance, and rolling volatility

   - Trained a Random Forest classifier to label periods as favorable or unfavorable

   - Used the model as a binary filter to allow or block trades

Outcome:

This approach did not work well in practice. The model tended to block trading too often, which resulted in:

   - Missed profitable trends

   - Long periods of flat performance

   - Worse overall results

This showed that using ML as a strict “trade or don’t trade” decision tool can be ineffective.

## Using ML for Risk Control Instead of Prediction

Instead of discarding ML entirely, I changed what it was doing.

Rather than asking whether the strategy should trade, the model was used to estimate how risky the current market environment appears.

   - The model outputs probabilities instead of hard decisions

   - These probabilities are treated as a confidence or risk measure

   - Exposure is reduced during higher-risk regimes rather than eliminated

This allowed ML to act as a risk overlay instead of a signal generator.

## Volatility Targeting

Volatility targeting was added to further stabilize the strategy.

   - Rolling volatility is estimated using recent returns

   - Position size is scaled to target a consistent level of risk

   - Leverage is capped to keep the strategy realistic

This approach is commonly used in systematic trading to maintain stable risk over time.

## Final Strategy Structure

The final process is:

Price Data
   ↓
Moving Average Signal
   ↓
ML-Based Risk Adjustment
   ↓
Volatility Targeting
   ↓
Backtest with Transaction Costs

Each component has a specific role:

   - Moving averages determine direction

   - ML adjusts risk exposure

   - Volatility targeting controls overall risk

## Results and Takeaways

   - The final strategy produces lower returns than buy-and-hold

   - Volatility and drawdowns are significantly reduced

   - Risk-adjusted performance improves compared to the baseline

   - Large losses during market stress are avoided

Key Lessons

   - Simple strategies often fail due to poor risk control

   - ML is more effective as a risk management tool than a predictor

   - Improving robustness can be more important than increasing returns

## Limitations and Future Work

This project has several limitations:

   - Only one asset (SPY) is tested

   - Daily data is used

   - No macroeconomic or cross-asset features are included
     
Possible next steps include:

   - Testing on additional assets

   - Walk-forward retraining of the ML model

   - Portfolio-level analysis
