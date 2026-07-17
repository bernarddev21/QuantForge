from loguru import logger
import os

# Ensure log directory exists
os.makedirs("storage/logs", exist_ok=True)

# Remove default console logger
logger.remove()

# Console output
logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
    colorize=True,
    format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | {message}"
)

# Log file
logger.add(
    "storage/logs/quantforge.log",
    rotation="5 MB",
    retention="30 days",
    level="DEBUG",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

def get_logger():
    return logger