
def data_filename(ticker: str, period: str, interval: tuple[str, str],
                  offer_side:str = "BID", metric: str = "Candlestick", extension: str = 'csv') -> str:
    
    """
    data_filename(ticker="EURUSD", period="1 Hour", start="1/7/2020", finish="15/7/2023",
                  offer_side="BID", metric="Candlestick", extension="csv")
    """
    start, finish = interval

    period_value, period_metric           = period.split(' ')
    start_day, start_month, start_year    = start.split('/')
    finish_day, finish_month, finish_year = finish.split('/')

    start_day    = f"{int(start_day):02d}"
    start_month  = f"{int(start_month):02d}"
    finish_day   = f"{int(finish_day):02d}"
    finish_month = f"{int(finish_month):02d}"
    
    return f'{ticker}_{metric}_{period_value}_{period_metric}_{offer_side}_{start_day}.{start_month}.{start_year}-{finish_day}.{finish_month}.{finish_year}.{extension}'
