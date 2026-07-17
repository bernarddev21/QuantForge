from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    Float,
    String,
    BigInteger,
    ForeignKey,
)

from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from core.logger import get_logger

logger = get_logger()

DATABASE_URL = "sqlite:///storage/database.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True)
    symbol = Column(String, unique=True, nullable=False)
    exchange = Column(String, nullable=False)

    candles = relationship("Candle", back_populates="asset")


class Candle(Base):
    __tablename__ = "candles"

    id = Column(Integer, primary_key=True)

    asset_id = Column(Integer, ForeignKey("assets.id"))

    timeframe = Column(String)
    timestamp = Column(BigInteger)

    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

    asset = relationship("Asset", back_populates="candles")


def create_database():
    Base.metadata.create_all(engine)


def add_asset(symbol, exchange):

    session = SessionLocal()

    existing = session.query(Asset).filter_by(symbol=symbol).first()

    if existing:
        logger.warning(f"Asset already exists: {symbol}")
        session.close()
        return

    asset = Asset(
        symbol=symbol,
        exchange=exchange
    )

    session.add(asset)
    session.commit()

    logger.info(f"Added asset: {symbol}")

    session.close()


def add_candles(asset_symbol, candles, timeframe):

    session = SessionLocal()

    asset = session.query(Asset).filter_by(symbol=asset_symbol).first()

    if asset is None:
        logger.error(f"Asset not found: {asset_symbol}")
        session.close()
        return

    inserted = 0

    for candle in candles:

        exists = session.query(Candle).filter_by(
            asset_id=asset.id,
            timeframe=timeframe,
            timestamp=candle[0]
        ).first()

        if exists:
            continue

        new_candle = Candle(
            asset_id=asset.id,
            timeframe=timeframe,
            timestamp=candle[0],
            open=candle[1],
            high=candle[2],
            low=candle[3],
            close=candle[4],
            volume=candle[5]
        )

        session.add(new_candle)
        inserted += 1

    session.commit()

    logger.info(f"Inserted {inserted} new candles.")

    session.close()