from typing import Optional
from dataclasses import dataclass
from datetime import date

# Market data
@dataclass
class OHLCVRecord:
    symbol: str
    date: date

    open: float
    high: float
    low: float
    close: float
    adjusted_close: float

    volume: float

    dividend_amount: float = 0.0
    split_coefficient: float = 1.0

# Returns
@dataclass
class ReturnFeatures:
    symbol: str
    date: date

    daily_return: float
    log_return: float

    weekly_return: Optional[float]
    monthly_return: Optional[float]

# Indicators
## Trends
@dataclass
class TrendFeatures:
    symbol: str
    date: date

    sma_5: Optional[float]
    sma_10: Optional[float]
    sma_20: Optional[float]
    sma_50: Optional[float]
    sma_100: Optional[float]
    sma_200: Optional[float]

    ema_12: Optional[float]
    ema_26: Optional[float]

## Momentum
@dataclass
class MomentumFeatures:
    symbol: str
    date: date

    rsi_14: Optional[float]

    macd: Optional[float]
    macd_signal: Optional[float]
    macd_histogram: Optional[float]

    roc: Optional[float]
    momentum: Optional[float]

## Volatility
@dataclass
class VolatilityFeatures:
    symbol: str
    date: date

    atr_14: Optional[float]

    rolling_vol_10: Optional[float]
    rolling_vol_20: Optional[float]
    rolling_vol_60: Optional[float]

## Volume
@dataclass
class VolumeFeatures:
    symbol: str
    date: date

    obv: Optional[float]
    volume_ma: Optional[float]
    volume_change: Optional[float]
    vwap: Optional[float]

## Macroeconomics
@dataclass
class MacroFeatures:
    date: date

    federal_funds_rate: Optional[float]

    inflation: Optional[float]

    cpi: Optional[float]

    real_gdp: Optional[float]

    unemployment: Optional[float]

    treasury_yield_2y: Optional[float]
    treasury_yield_10y: Optional[float]
    treasury_yield_30y: Optional[float]

# Fundamentals
@dataclass
class FundamentalFeatures:
    symbol: str
    date: date

    market_cap: Optional[float]

    pe_ratio: Optional[float]
    peg_ratio: Optional[float]

    eps: Optional[float]

    book_value: Optional[float]

    price_to_book: Optional[float]
    price_to_sales: Optional[float]

    dividend_yield: Optional[float]

    beta: Optional[float]

    shares_outstanding: Optional[float]

# Statments
## Income
@dataclass
class IncomeStatementFeatures:
    symbol: str
    fiscal_date: date

    revenue: Optional[float]
    gross_profit: Optional[float]

    operating_income: Optional[float]

    net_income: Optional[float]

    ebitda: Optional[float]

## Balances
@dataclass
class BalanceSheetFeatures:
    symbol: str
    fiscal_date: date

    cash: Optional[float]

    total_assets: Optional[float]

    total_liabilities: Optional[float]

    shareholder_equity: Optional[float]

    long_term_debt: Optional[float]

# Cash
@dataclass
class CashFlowFeatures:
    symbol: str
    fiscal_date: date

    operating_cash_flow: Optional[float]

    capital_expenditures: Optional[float]

    free_cash_flow: Optional[float]

# Regime
@dataclass
class MarketRegimeFeatures:
    date: date

    spy_return: Optional[float]
    qqq_return: Optional[float]
    dia_return: Optional[float]

    vix_close: Optional[float]

    market_volatility: Optional[float]

    market_drawdown: Optional[float]

# News Sentiment
@dataclass
class NewsSentimentFeatures:
    symbol: str
    date: date

    sentiment_score_mean: Optional[float]

    sentiment_score_std: Optional[float]

    positive_articles: int

    negative_articles: int

    neutral_articles: int

    article_count: int

