#
# Copyright 2021 Stephen Eaton
#
# This file is part of Maker-Hub.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights,
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
    """Application .env default settings."""

    API_V1_STR: str = "/api/v1"
    DEV_MODE: bool = False
    DEBUG: bool = False
    DATABASE_URL: str = "sqlite+aiosqlite:///./app/dbdata/maker-hub.db"
    LOGFILE: str = "maker-hub.log"
    ENABLE_SQL_LOGGING: bool = False
    VERSION: str = "2021.0.0-Dev3"

    NANOID_ALPHABET: str = "0123456789abcdefghijklmnopqrstuvwxyz"
    NANOID_SIZE: int = 26

    HOST: str = "http://127.0.0.1"
    PORT: int = 8000

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()

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
