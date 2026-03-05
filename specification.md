## Next Research Upgrades (Short Spec)

### 1) Feature Importance (What it should have)
- **Global importance**: rank top features (gain / permutation / SHAP if available).
- **Stability check**: top features consistent across time windows (not just one period).
- **Redundancy pruning**: drop highly correlated features; keep a smaller strong set.
- **Diagnostics**: feature vs. future return monotonicity (bin/quantile plots), missing/clip rates.
- **Actionable output**: `top_20_features.json` + a short table in the report.

---

### 2) Walk-Forward Validation (What it should have)
- **Rolling splits**: `train -> validate -> test`, then roll forward (no leakage).
- **Retraining schedule**: retrain every `N` days/weeks (configurable).
- **Per-window metrics**: IC mean/std, IC_IR, long-short return, Sharpe, max drawdown.
- **Aggregation**: weighted average + distribution (median, worst decile window).
- **Model selection**: pick hyperparams on validation only; lock for test windows.

---

### 3) Strategy Optimization (What it should have)
- **Portfolio construction**: long/short quantiles or top-k with weights (equal, z-score, risk-parity).
- **Turnover control**: `topk_drop`, holding period, rebalance frequency, min-change threshold.
- **Risk controls**: leverage cap, position cap, sector/industry neutrality (optional), volatility targeting.
- **Costs + slippage**: include realistic transaction costs; evaluate net performance.
- **Parameter sweep**: grid over `topk`, `hold`, `drop`, `rebalance`, `cost` and select by net Sharpe/IR.