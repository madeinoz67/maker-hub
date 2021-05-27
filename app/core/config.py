import logging
import sys
from functools import lru_cache

from loguru import logger
from pydantic import BaseSettings, Field

from app.core.logging import InterceptHandler


@lru_cache()
def get_settings():
    return Settings()


class Settings(BaseSettings):
    DEV_MODE: bool = Field(..., env="DEV_MODE")
    DEBUG: bool = Field(..., env="DEBUG")
    # db_connection: str
    LOGFILE: str = Field(..., env="LOGFILE")
    ENABLE_SQL_LOGGING: bool = Field(..., env="ENABLE_SQL_LOGGING")
    # # enable_sql_logging: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        # fields = {
        #     "DEV_MODE": {"env": "DEV_MODE"},
        #     "DEBUG": {"env": "DEBUG"},
        #     "DB_CONNECTION": {"env": "DB_CONNECTION"},
        #     "LOGFILE": {"env": "LOGFILE"},
        #     "ENABLE_SQL_LOGGING": {"env": "ENABLE_SQL_LOGGING"},
        # }


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
