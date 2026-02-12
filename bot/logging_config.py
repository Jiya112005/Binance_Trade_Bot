import logging
from logging.handlers import RotatingFileHandler 
import os

def setup_loggers():
    os.makedirs("logs", exist_ok=True)
    
    logger = logging.getLogger("trading_bot")
    logger.setLevel(logging.INFO)
    
    
    if not logger.handlers:
        handler = RotatingFileHandler("logs/bot.log", maxBytes=1_000_000, backupCount=3)
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger