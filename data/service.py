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

    def get_multiple_assets(
        self,
        symbols,
        timeframe="1h",
        limit=100
    ):
        market_data = {}

        for symbol in symbols:
            market_data[symbol] = self.get_market_data(
                symbol=symbol,
                timeframe=timeframe,
                limit=limit
            )

        return market_data