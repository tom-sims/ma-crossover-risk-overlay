#Moving Average Crossover with ML Risk Control & Volatility Targeting
Overview
This project explores a classic moving average crossover strategy on SPY and progressively extends it with machine learning–based risk control and volatility targeting.
The goal was not to build a high-return or production-ready trading system, but to understand:
Where simple trend-following strategies fail


How machine learning can (and cannot) add value


How professional risk management techniques improve robustness


The final result is a risk-controlled trend-following strategy with significantly reduced drawdowns and improved risk-adjusted performance.

1. Baseline Strategy: Moving Average Crossover
The project began with a simple, well-known strategy:
Compute a fast and slow moving average of price


Go long when the fast MA is above the slow MA


Stay out of the market otherwise


Signals are shifted forward by one day to avoid lookahead bias


This type of strategy is widely studied and serves as a baseline trend-following signal, not an alpha-generating model.
Key Observations
The strategy captures long-term trends reasonably well


It suffers from large drawdowns during market crashes


Performance is highly dependent on market regime (trending vs choppy)


This confirmed a common result in quantitative finance:
trend-following works, but risk management dominates outcomes.

2. First ML Attempt: Regime Classification (What Didn’t Work)
The next step was to explore whether machine learning could identify favorable market regimes.
Approach
Engineered market state features (MA slopes, MA distance, volatility)


Trained a Random Forest classifier to label periods as:


“Good for trend-following”


“Bad for trend-following”


Used ML as a binary gate:


Only trade when ML predicted a favorable regime


Result
This approach consistently reduced exposure too aggressively, leading to:
Missed upside


Flat equity curves


Lower overall performance


Key Insight
Using ML as a hard decision-maker (“trade / don’t trade”) is often counterproductive in financial markets.
This mirrors findings in academic and professional research:
ML is rarely effective as a strict timing tool, especially for short-horizon predictions.

3. Reframing ML: From Prediction to Risk Control
Rather than abandoning ML, the role of ML was redefined.
New Perspective
Instead of asking:
“Should I trade?”
The ML model was used to ask:
“How risky does the current environment appear?”
Implementation
The Random Forest outputs probabilities, not binary predictions


These probabilities are interpreted as regime confidence


ML does not decide direction


ML only reduces exposure during high-risk regimes


This transformed ML into a risk overlay, not a signal generator.

4. Volatility Targeting
To further stabilize the strategy, volatility targeting was introduced.
Motivation
Even with better regime handling, fixed position sizing leads to:
Excessive risk during volatile periods


Underutilization of capital during calm periods


Method
Estimate rolling realized volatility


Scale exposure so that portfolio volatility targets a fixed annual level


Cap leverage to avoid unrealistic position sizes


This step normalizes risk over time and is widely used in:
Trend-following funds


Risk parity portfolios


CTA strategies



5. Final Strategy Architecture
The final pipeline is:
Price Data
   ↓
Moving Average Signal (Direction)
   ↓
ML-Based Risk Overlay (Exposure Reduction)
   ↓
Volatility Targeting (Position Scaling)
   ↓
Backtest with Transaction Costs

Each component has a clear, limited role:
Moving averages provide directional bias


ML controls downside risk


Volatility targeting stabilizes returns



6. Results & Takeaways
Key Outcomes
Raw returns were lower than buy-and-hold


Volatility and drawdowns were dramatically reduced


Risk-adjusted performance (Sharpe ratio) improved significantly


Maximum drawdowns were reduced to single-digit percentages


Main Lessons
Simple strategies fail primarily due to poor risk management


ML is more effective as a risk control tool than a predictor


Robustness and interpretability matter more than optimization


Accepting lower returns in exchange for stability is often rational



7. Limitations & Future Work
This project intentionally avoids overfitting and complexity. Known limitations include:
Single asset (SPY)


Daily data only


No macroeconomic features


No walk-forward retraining


Possible extensions:
Apply to multiple assets


Walk-forward ML retraining


Portfolio-level risk allocation


Comparative analysis across MA parameter ranges



