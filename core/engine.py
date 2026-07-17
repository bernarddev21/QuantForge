from data.binance import BinanceClient
from data.database import create_database
from data.database import add_asset
from data.database import add_candles

from core.logger import get_logger

logger = get_logger()


class QuantForgeEngine:

    def __init__(self):
        self.client = BinanceClient()

    def run(self):

        logger.info("Starting QuantForge...")

        create_database()

        add_asset(
            symbol="BTC/USDT",
            exchange="Binance"
        )

        candles = self.client.get_candles()

        logger.info(f"Downloaded {len(candles)} candles")

        add_candles(
            asset_symbol="BTC/USDT",
            candles=candles,
            timeframe="1h"
        )

        logger.success("Engine complete.")