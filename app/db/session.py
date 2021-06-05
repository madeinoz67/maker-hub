from contextvars import ContextVar
from pathlib import Path
from typing import Callable, Optional

from loguru import logger
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from app.core.config import settings
from app.models.modelbase import SqlAlchemyBase  # noqa:

__async_engine: Optional[Callable[[], AsyncEngine]] = None


def global_init(db_file: str):
    global __async_engine

    if __async_engine:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file.")

    folder = Path(db_file).parent
    folder.mkdir(parents=True, exist_ok=True)

    conn_str = "sqlite+aiosqlite:///" + db_file.strip()

    logger.info(f"DB URL: {conn_str}")

    enable_sql_logging = settings.ENABLE_SQL_LOGGING

    __async_engine = create_async_engine(
        conn_str, echo=enable_sql_logging, connect_args={"check_same_thread": False}
    )


def create_session() -> AsyncSession:
    global __async_engine

    if not __async_engine:
        raise Exception("You must call global_init() before using this method.")

    session: AsyncSession = AsyncSession(__async_engine)
    session.sync_session.expire_on_commit = False

    return session


async def get_db_session() -> AsyncSession:
    async with create_session() as session:
        yield session


db_session_context: ContextVar[AsyncSession] = ContextVar("db_session_context")
