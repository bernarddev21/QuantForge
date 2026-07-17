import ccxt


class BinanceClient:

    def __init__(self):
        self.exchange = ccxt.binance({
            "enableRateLimit": True
        })

    def get_candles(self, symbol="BTC/USDT", timeframe="1h", limit=100):

        candles = self.exchange.fetch_ohlcv(
            symbol,
            timeframe=timeframe,
            limit=limit
        )

        return candles