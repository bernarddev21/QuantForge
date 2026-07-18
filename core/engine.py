from config.settings import WATCHLIST

from data.service import DataService
from data.database import create_database
from data.database import add_asset
from data.database import add_candles

from research.statistics import StatisticsEngine
from research.signals import SignalEngine

from core.logger import get_logger

logger = get_logger()


class QuantForgeEngine:

    def __init__(self):
        self.data_service = DataService()
        self.statistics = StatisticsEngine()
        self.signal_engine = SignalEngine()

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

            df = self.statistics.calculate_returns(candles)
            df = self.statistics.add_features(df)
            signal = self.signal_engine.moving_average_signal(df)

            logger.info(
             f"{symbol}\n"
             f"Signal: {signal}\n"
             f"Average Return: {df['return'].mean():.6f}\n"
             f"MA20: {df['ma20'].iloc[-1]:.2f}\n"
             f"MA50: {df['ma50'].iloc[-1]:.2f}\n"
             f"Volatility20: {df['volatility20'].iloc[-1]:.6f}"
)
              
        logger.success("Engine complete.")    

            

             

            

            

            
        
