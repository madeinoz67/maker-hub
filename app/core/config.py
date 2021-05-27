import logging
import sys
from functools import lru_cache

from loguru import logger
from pydantic import BaseSettings

from app.core.logging import InterceptHandler


@lru_cache()
def get_settings():
    return Settings()


class Settings(BaseSettings):

    DEV_MODE: bool = False
    DEBUG: bool = False
    # DB_CONNECTION: str =
    LOGFILE: str = "maker-hub.log"
    ENABLE_SQL_LOGGING: bool = False

    nanoid_alphabet: str = "0123456789abcdefghijklmnopqrstuvwxyz"
    nanoid_size: int = 26

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Logging Configuration
LOGGING_LEVEL = logging.DEBUG if get_settings().DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
if get_settings().DEBUG:
    logger.add(get_settings().LOGFILE, enqueue=True)
