from data.binance import BinanceClient


class DataService:

    def __init__(self):
        self.binance = BinanceClient()

    def get_market_data(
        self,
        symbol="BTC/USDT",
        timeframe="1h",
        limit=100
    ):
        return self.binance.get_candles(
            symbol=symbol,
            timeframe=timeframe,
            limit=limit
        )