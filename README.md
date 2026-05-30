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

Bayesian Neural Networks for uncertainty-aware financial forecasting and probabilistic time-series modeling.

## Objectives

- Implement Bayesian Neural Networks in PyTorch
- Explore variational inference and Monte Carlo methods
- Evaluate predictive uncertainty and calibration
- Analyze financial time-series under noisy conditions

## Status

Early-stage research and implementation.

## Planned Components

- Data ingestion and preprocessing
- Baseline Bayesian MLP models
- Uncertainty estimation
- Calibration evaluation
- Financial forecasting experiments
