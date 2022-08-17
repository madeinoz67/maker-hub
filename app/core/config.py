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


from functools import lru_cache
from pathlib import Path
from typing import Optional

from loguru import logger
from pydantic import BaseModel, BaseSettings, Field

APP_ROOT = Path(__file__).parent.parent
logger.info(f"Application root: {APP_ROOT}")


class AppSettings(BaseModel):
    """Application configuration using pydantic `BaseModel`.
    Will be accessed as `fastapi_settings` within the application.
    """

    title: str = "Maker Hub"
    description: str = "Open Source Personal Hub for Makers: Manage Parts, projects, ideas, documentation, parts and footprints etc"

    version: str = "0.0.1"
    docs_url: str = "/docs"
    debug: bool = True


class GlobalSettings(BaseSettings):
    """Global configuration using pydantic `BaseSettings`.
    Will be accessed as `settings` within the application.
    """

    fastapi_settings: AppSettings = AppSettings()

    APP_DIR: Path = APP_ROOT

    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    DEBUG: bool = False

    DISABLE_DOCS: bool = False

    SECRET_KEY: str = "overriden_by_dotenv_value"

    MONGO_SCHEME: Optional[str] = None
    MONGO_HOST: Optional[str] = None
    MONGO_PORT: Optional[str] = None
    MONGO_USER: Optional[str] = None
    MONGO_PASSWORD: Optional[str] = None
    MONGO_DB: Optional[str] = None

    API_V1_STR: str = "/api/1"

    LOGFILE: str = "maker-hub.log"

    NANOID_ALPHABET: str = "0123456789abcdefghijklmnopqrstuvwxyz"
    NANOID_SIZE: int = 26

    HOST: str = "http://127.0.0.1"
    PORT: int = 8000

    class Config:
        env_file = APP_ROOT.parent / ".env"
        env_file_encoding = "utf-8"


class DevSettings(GlobalSettings):
    """Configuration for development environment."""

    DEV_MODE: bool = True

    class Config:
        env_prefix = "DEV_"


class PrdSettings(GlobalSettings):
    """Configuration for production environment."""

    DEV_MODE: bool = False

    class Config:
        env_prefix = "PRD_"


class FactorySettings:
    """Callable class that loads Dev or Prod settings."""

    def __init__(self, env_state: Optional[str] = None):
        self.env_state = env_state

    def __call__(self):
        if self.env_state == "dev":
            return DevSettings()
        elif self.env_state == "prd":
            return PrdSettings()
        else:
            raise ValueError(f"Invalid env_state: {self.env_state}")


settings = FactorySettings(GlobalSettings().ENV_STATE)()
logger.info(f"Settings: {settings.__repr__()}")
