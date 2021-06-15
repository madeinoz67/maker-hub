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

from contextvars import ContextVar
from pathlib import Path
from typing import Callable, Optional

from loguru import logger
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from app.core.config import settings
from app.models.modelbase import SqlAlchemyBase  # noqa:

__async_engine: Optional[Callable[[], AsyncEngine]] = None


def global_init(db_file: str):
    """Initialize the database .

    Args:
        db_file (str): filename and path of sqlite db file

    Raises:
        Exception: no db file specified
    """
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
    """Create a DB session object for use with the Async engine .

    Raises:
        Exception: if global init is not called first

    Returns:
        AsyncSession: sqlalchemy Async Object
    """
    global __async_engine

    if not __async_engine:
        raise Exception("You must call global_init() before using this method.")

    session: AsyncSession = AsyncSession(__async_engine)
    session.sync_session.expire_on_commit = False

    return session


async def get_db_session() -> AsyncSession:
    """Get a DB session for use.

    Returns:
        AsyncSession:

    Yields:
        Iterator[AsyncSession]:
    """
    async with create_session() as session:
        yield session


db_session_context: ContextVar[AsyncSession] = ContextVar("db_session_context")
