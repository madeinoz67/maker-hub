from pydoc import doc
from typing import Optional

from beanie import init_beanie
from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import AnyUrl, BaseSettings, validator

from app.core.config import settings
from app.models.part import PartDB


class DatabaseConnector(BaseSettings):
    """Load database settings and build valid URI"""

    MONGO_DB_URI: Optional[AnyUrl] = None

    @validator("MONGO_DB_URI", pre=True, check_fields=False)
    def uri_is_valid(cls, v):
        if isinstance(v, AnyUrl):
            return v

        if settings.MONGO_HOST in ("localhost", "127.0.0.1"):
            try:
                return AnyUrl.build(
                    scheme=settings.MONGO_SCHEME,
                    host=settings.MONGO_HOST,
                    port=settings.MONGO_PORT,
                    user=settings.MONGO_USER,
                    password=settings.MONGO_PASSWORD,
                    path=f"/{settings.MONGO_DB}",
                    query="retryWrites=true&w=majority",
                )
            except Exception as e:
                raise AttributeError(v) from e
        try:
            return AnyUrl.build(
                scheme=settings.MONGO_SCHEME,
                host=settings.MONGO_HOST,
                user=settings.MONGO_USER,
                password=settings.MONGO_PASSWORD,
                path=f"/{settings.MONGO_DB}",
                query="retryWrites=true&w=majority",
            )
        except Exception as exc:
            logger.error(exc)
            raise AttributeError(v) from exc

    async def initialize_db(self) -> None:
        """start db client with Beanie and load models"""

        client = AsyncIOMotorClient(self.MONGO_DB_URI)
        logger.info(f"MONGO_DB_URI: {self.MONGO_DB_URI}")

        models = [PartDB]
        logger.info(f"DB Models: {models}")
        try:
            await init_beanie(
                database=client[settings.MONGO_DB], document_models=models
            )
            logger.info(f"Connected to {settings.MONGO_DB}")
        except Exception as e:
            logger.error(e)
            raise ConnectionError from e


db = DatabaseConnector()
