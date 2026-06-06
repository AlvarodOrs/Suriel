from src.training import TradingPipeline

pipeline = TradingPipeline(
    "./data/raw/EURUSD_Candlestick_1_Hour_BID_01.07.2020-15.07.2023.csv"
)
pipeline.run()