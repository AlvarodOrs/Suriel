"""
MAIN_CURRENCY  = the currency YOU want to trade with
CRYPTO_TICKERS = the coins    YOU want to trade with
MARKET_TICKERS = the stocks   YOU want to trade with
----------------------------------------------------
B = yfinance.Ticker(A).info.get('longName')
*_TICKERS = {
    A: B
}
"""

MAIN_CURRENCY: str  = 'USD'

CRYPTO_TICKERS: dict[str, str] = {
    # Exactly as yfinance  :  whatever here
    f'USDT-{MAIN_CURRENCY}': f'Tether USDt {MAIN_CURRENCY}',
    f'USDC-{MAIN_CURRENCY}': f'USD Coin {MAIN_CURRENCY}',
    f'BTC-{MAIN_CURRENCY}' : f'Bitcoin {MAIN_CURRENCY}',
    f'ETH-{MAIN_CURRENCY}' : f'Ethereum {MAIN_CURRENCY}',
    f'SOL-{MAIN_CURRENCY}' : f'Solana {MAIN_CURRENCY}',
    f'XRP-{MAIN_CURRENCY}' : f'XRP {MAIN_CURRENCY}',
    f'XMR-{MAIN_CURRENCY}' : f'Monero {MAIN_CURRENCY}',
}

MARKET_TICKERS: dict[str, str] = {
    'SGOV' : 'iShares 0-3 Month Treasury Bond ETF',
    'BIL'  : 'State Street SPDR Bloomberg 1-3 Month T-Bill ETF',
    'MSFT' : 'Microsoft Corporation',
    'BRK-B': 'Berkshire Hathaway Inc.',
    'NVDA' : 'NVIDIA Corporation',
    'META' : 'Meta Platforms, Inc.',
    'PLTR' : 'Palantir Technologies Inc.',
    'HOOD' : 'Robinhood Markets, Inc.',
    'MSTR' : 'Strategy Inc',
    'ASML' : 'ASML Holding N.V.'
}

MERGED = CRYPTO_TICKERS | MARKET_TICKERS