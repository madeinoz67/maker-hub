from databases import Database
from fastapi import FastAPI
from loguru import logger

from app.core import config


async def connect_to_db(app: FastAPI) -> None:

    database = Database(config.get_settings().DATABASE_URL)

    try:
        logger.debug("--- DB CONNECTING ---")
        await database.connect()
        app.state._db = database
        logger.debug("--- DB CONNECTING COMPLETE ---")
    except Exception as e:
        logger.warn("--- DB CONNECTION ERROR ---")
        logger.warn(e)
        logger.warn("--- DB CONNECTION ERROR ---")


async def close_db_connection(app: FastAPI) -> None:
    try:
        logger.debug("--- DB DISCONNECTING ---")
        await app.state._db.disconnect()
        logger.debug("--- DB DISCONNECTION COMPLETE ---")
    except Exception as e:
        logger.warn("--- DB DISCONNECT ERROR ---")
        logger.warn(e)
        logger.warn("--- DB DISCONNECT ERROR ---")
