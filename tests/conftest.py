import os
import warnings
from contextvars import ContextVar
from typing import AsyncGenerator
from unittest import mock

import alembic
import pytest
from alembic.config import Config

# from example.routers.utils.db import get_db
from fastapi import FastAPI
from httpx import AsyncClient  # noqa:
from pytest_factoryboy import register
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from tests.factories import PartCreateSchemaFactory

# Default to using sqlite in memory for fast tests.
# Can be overridden by environment variable for testing in CI against other
# database engines

SQLALCHEMY_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL", "sqlite+aiosqlite:///./tests/files/test.db"
)

db_session_context: ContextVar[AsyncSession] = ContextVar("db_session_context")

# Register factories
register(PartCreateSchemaFactory)

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# see https://linw1995.com/en/blog/How-To-Write-Asynchronous-Code-With-Contextvars-Properly/
def apply_context(ctx):
    """
    Update the current context
    """
    for var in ctx:
        var.set(ctx[var])


# Apply migrations at beginning and end of testing session
@pytest.fixture(scope="session")
def apply_migrations():
    with mock.patch.dict(
        os.environ, {"DATABASE_URL": SQLALCHEMY_DATABASE_URL}, clear=True
    ):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        config = Config("alembic.ini")
        alembic.command.upgrade(config, "head")
        yield
        alembic.command.downgrade(config, "base")


@pytest.fixture()
def app(apply_migrations: None) -> FastAPI:
    """
    Create a fresh database on each test case.
    """
    from app.main import get_application

    return get_application()


# @pytest.fixture()
# async def client(app: FastAPI, engine) -> AsyncClient:
#     """
#     Create a new Httpx AsyncClient that uses the `db_session` fixture to override
#     the `get_db` dependency that is injected into routes.
#     """

#     def _get_test_db():
#         try:
#             db_session: AsyncSession = AsyncSession(engine)
#             async with db_session as session:
#                 yield session
#         finally:
#             session.rollback()
#             session.close()

#     app.dependency_overrides["get_db_session"] = _get_test_db

#     with AsyncClient(app) as client:
#         yield client


@pytest.fixture(scope="function")
@pytest.mark.asyncio
async def db_session(apply_migrations) -> AsyncGenerator[AsyncSession, None]:

    async with async_session() as session:
        try:
            yield session
        finally:
            await session.rollback()
            await session.close()


# @pytest.fixture(scope="function")
# @pytest.mark.asyncio
# async def db_ctx(apply_migrations) -> AsyncGenerator[ContextVar, None]:

#     # async with async_session() as session:
#     # Set the injected db_session dependency to the db_session context object
#     db_session_context.set(async_session())
#     yield copy_context()
