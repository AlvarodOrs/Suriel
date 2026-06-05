<!-- [START]
## Overview

Research project focused on building a modular, event-driven backtesting system for evaluating trading strategies on historical financial data (Yahoo Finance and similar sources).

The emphasis is on reproducible simulation, correct accounting of returns, and consistent evaluation methodology rather than strategy optimization.

## Scope

- **Market data pipeline** — ingestion, cleaning, alignment, and normalization of time-series data
- **Execution model** — simplified event-driven simulation of orders, positions, and portfolio state
- **Strategy layer** — implementation of baseline strategies (momentum, moving average crossover) with modular interface
- **Performance evaluation** — PnL computation, returns distribution, volatility, drawdown, and risk-adjusted metrics

## Constraints

- No live trading or brokerage integration
- Assumes frictionless or simplified execution model (configurable)
- Designed for research and experimentation, not production trading

## Status

In progress. Core framework design and initial strategy implementations underway.
[END] -->
# Suriel

Uncertainty-aware financial forecasting using Bayesian Neural Networks for probabilistic time-series modeling and risk-sensitive decision analysis.

---

## Overview

Suriel is a modular research framework for evaluating probabilistic deep learning methods in financial time-series forecasting. The core focus is not point prediction accuracy, but the quality, calibration, and decision relevance of predictive uncertainty under non-stationary market conditions.

Traditional forecasting systems assume deterministic outputs. Suriel instead models full predictive distributions, enabling explicit representation of epistemic uncertainty and its relationship to financial risk, regime shifts, and model degradation.

The central research question:

> Do Bayesian Neural Networks produce better-calibrated uncertainty estimates than deterministic and ensemble deep learning models, and does this translate into improved risk-aware decision making under realistic market conditions?

The system is designed as an experimental pipeline for benchmarking uncertainty-aware machine learning in financial environments.

---

## Objectives

- Develop a reproducible framework for probabilistic financial forecasting
- Benchmark Bayesian Neural Networks against deterministic and ensemble baselines
- Evaluate uncertainty calibration under different market regimes
- Analyze the relationship between predictive uncertainty and forecasting error
- Study whether uncertainty improves simulated risk-aware decision making
- Provide a reproducible experimental setup for research and benchmarking

---

## Scope

### Data Layer
- Historical financial time-series data (configurable asset classes)
- Time-consistent preprocessing and feature engineering
- Strict temporal splits (train / validation / test) to prevent leakage

### Modeling Layer

**Deterministic baselines:**
- Linear and nonlinear MLP models
- LSTM / GRU architectures
- Transformer-based time-series models (optional extension)
- Classical statistical baselines (ARIMA, GARCH where applicable)

**Probabilistic models:**
- Bayesian Neural Networks (variational inference)
- Monte Carlo Dropout approximations
- Deep ensemble methods as probabilistic baselines

---

### Uncertainty Modeling

- Predictive distribution estimation instead of point forecasts
- Separation of uncertainty components:
  - Epistemic uncertainty (model uncertainty)
  - Aleatoric uncertainty (data noise)
- Calibration analysis of predictive probabilities

---

### Evaluation Framework

**Predictive performance:**
- MAE / RMSE

**Probabilistic performance:**
- Negative Log-Likelihood (NLL)
- Continuous Ranked Probability Score (CRPS)

**Calibration metrics:**
- Expected Calibration Error (ECE)
- Reliability diagrams

**Financial simulation metrics:**
- Sharpe ratio (simulated strategies)
- Maximum drawdown
- Turnover and transaction cost sensitivity
- Risk-adjusted return stability across regimes

---

## System Architecture

Suriel is structured as a modular research pipeline:

1. **Data pipeline**
   - ingestion, cleaning, normalization, feature generation

2. **Model training layer**
   - deterministic and probabilistic model training workflows

3. **Inference layer**
   - generation of predictive distributions and uncertainty estimates

4. **Evaluation engine**
   - statistical and financial performance benchmarking

5. **Backtesting simulator**
   - event-driven portfolio simulation using historical data

---

## Constraints

- No live trading or brokerage integration
- No assumption of stationarity in financial time series
- All evaluation uses time-consistent validation (no data leakage)
- Backtesting includes transaction cost and slippage modeling
- System is designed for research, not production trading

---

## Roadmap

Suriel follows a staged, evidence-driven validation pipeline. Progression between phases is conditional on statistical validation, not implementation completeness.

---

### Phase 0: Research Design and Experiment Specification

Define the experimental framework before implementation.

**Deliverables:**
- Formal problem definition (forecast target, horizon, assets)
- Dataset specification and sourcing strategy
- Train / validation / test split design (time-consistent)
- Baseline model definitions
- Probabilistic model definitions
- Evaluation metrics specification (predictive, probabilistic, financial)
- Backtesting assumptions (costs, slippage, constraints)

**Exit criteria:**
- Fully reproducible experimental protocol defined before training begins

---

### Phase 1: Model Implementation and Training

Implementation of deterministic and probabilistic forecasting models.

**Deliverables:**
- Modular ML pipeline
- Trained deterministic baselines
- Implemented Bayesian and ensemble models
- Feature engineering pipeline
- Initial offline evaluation

**Exit criteria:**
- Baselines stable and reproducible
- Probabilistic outputs coherent and interpretable

---

### Phase 2: Historical Backtesting and Statistical Validation

#### Phase 2.0: Offline Backtesting

Evaluation on unseen historical data.

**Deliverables:**
- Walk-forward validation framework
- Rolling-window backtesting engine
- Transaction cost simulation
- Regime-based evaluation (volatility, crisis, bull/bear periods)
- Calibration diagnostics per regime

**Exit criteria:**
- Evidence of calibration and stability across regimes
- No leakage or overfitting detected

---

#### Phase 2.1: Simulated Live Evaluation (Paper Trading)

Real-time inference without capital exposure.

**Deliverables:**
- Live market data ingestion pipeline
- Paper trading execution simulator
- Latency and drift monitoring
- Performance tracking under live conditions

**Exit criteria:**
- Stability over extended simulation period
- Consistency with offline backtesting results

---

### Phase 3: Controlled Live Evaluation (Personal Capital Only)

#### Phase 3.0: Minimal Capital Deployment

Strictly constrained real-world testing with personal capital only.

**Constraints:**
- Fixed risk limits and exposure caps
- No uncontrolled leverage
- Full audit logging of decisions

**Deliverables:**
- Execution tracking system
- Live vs simulated performance comparison
- Slippage and execution impact analysis

**Exit criteria:**
- Statistical consistency between paper and live performance

---

#### Phase 3.1: Extended Personal Capital Validation

Gradual scaling of personal exposure only after stability is proven.

**Deliverables:**
- Multi-asset evaluation (if applicable)
- Stress testing under volatility spikes
- Risk-adjusted allocation tuning

**Exit criteria:**
- Multi-period stability across different market regimes

---

### Phase 4: Research Publication and External Collaboration

External engagement only after reproducibility and stability are demonstrated.

**Requirements:**
- Audit-grade experimental reporting
- Full reproducibility of results
- External validation of methodology

**Deliverables:**
- Research paper or technical report
- Open-source framework release (optional)
- Collaboration proposals for institutions

---

### Phase 5: Productionization (Optional)

Only if empirical results justify deployment.

**Deliverables:**
- Production inference API
- Monitoring and drift detection system
- Model versioning and retraining pipeline
- Governance and reliability controls

---

## Non-Goals

- High-frequency trading system design
- Guaranteed profitability or alpha generation
- Retail investor participation mechanisms
- Uncontrolled scaling of capital exposure
- Non-reproducible experimental claims

---

## Status

Active research and implementation phase.

Current focus:
- baseline model implementation
- probabilistic forecasting pipeline development
- initial backtesting framework
- calibration and evaluation metrics implementation

---

## Key Principle

All system behavior is validated through statistical evidence under time-consistent evaluation. No assumption of performance is accepted without reproducible experimental support.