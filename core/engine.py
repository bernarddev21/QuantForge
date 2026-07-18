from config.settings import WATCHLIST

from data.service import DataService
from data.database import create_database
from data.database import add_asset
from data.database import add_candles

from core.logger import get_logger

logger = get_logger()


class QuantForgeEngine:

    def __init__(self):
        self.data_service = DataService()

    def run(self):

        logger.info("Starting QuantForge...")

        create_database()

        market_data = self.data_service.get_multiple_assets(WATCHLIST)

        for symbol, candles in market_data.items():

            add_asset(
                symbol=symbol,
                exchange="Binance"
            )

            logger.info(f"Downloaded {len(candles)} candles for {symbol}")

            add_candles(
                asset_symbol=symbol,
                candles=candles,
                timeframe="1h"
            )

        logger.success("Engine complete.")