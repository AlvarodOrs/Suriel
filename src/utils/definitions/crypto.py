from typing import Any, Optional
from dataclasses import dataclass
from datetime import date

@dataclass(slots=True)
class Coin:
    id: str
    symbol: str
    name: str
    raw: dict[str, Any]

# Market data
@dataclass
class CryptoMarketData:
    coin_id: str
    date: date

    price: float

    market_cap: float

    volume_24h: float

    fully_diluted_valuation: Optional[float]

    circulating_supply: Optional[float]

    total_supply: Optional[float]

    max_supply: Optional[float]

# Dominance
@dataclass
class CryptoDominanceFeatures:
    date: date

    btc_dominance: Optional[float]

    eth_dominance: Optional[float]

# Volatility
@dataclass
class CryptoVolatilityFeatures:
    coin_id: str
    date: date

    rolling_vol_7: Optional[float]

    rolling_vol_30: Optional[float]

    rolling_vol_90: Optional[float]