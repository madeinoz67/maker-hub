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

"""conftest.py.

Pytest setup

"""

import os
import warnings
from contextvars import ContextVar  # noqa:
from typing import AsyncGenerator
from unittest import mock

import alembic
import pytest
from alembic.config import Config

# from example.routers.utils.db import get_db
from fastapi import FastAPI
from httpx import AsyncClient  # noqa:
from pytest_factoryboy import register
from sqlalchemy.ext.asyncio import AsyncSession

from .common import SQLALCHEMY_DATABASE_URL, async_session
from .factories import PartCreateSchemaFactory, PartModelFactory

# Default to using sqlite in memory for fast tests.
# Can be overridden by environment variable for testing in CI against other
# database engines

# SQLALCHEMY_DATABASE_URL = os.getenv(
#     "TEST_DATABASE_URL", "sqlite+aiosqlite:///./tests/files/test.db"
# )

# db_session_context: ContextVar[AsyncSession] = ContextVar("db_session_context")


# engine = create_async_engine(
#     SQLALCHEMY_DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
# )

# async_session = scoped_session(
#     sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
# )

# Register factories
register(PartCreateSchemaFactory)
register(PartModelFactory)

# see https://linw1995.com/en/blog/How-To-Write-Asynchronous-Code-With-Contextvars-Properly/
def apply_context(ctx):
    """Update the current context."""
    for var in ctx:
        var.set(ctx[var])


# Apply migrations at beginning and end of testing session
@pytest.fixture(scope="function")
def apply_migrations():
    """Fixture to Apply SQLAlchemy migrations to the current test environment."""
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
    """Fixture to Return the application object .

    Args:
        apply_migrations (None): fixture that applies DB migrations

    Returns:
        FastAPI:  application object
    """
    from app.main import get_application

    return get_application()


# @pytest.fixture()
# @pytest.mark.asyncio
# def client(app: FastAPI, engine) -> AsyncClient:
#     """
#     Create a new Httpx AsyncClient that uses the `db_session` fixture to override
#     the `get_db` dependency that is injected into routes.
#     """

#     def _get_test_db():
#         try:
#             db_session: AsyncSession = async_session()
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
    """Create a session for use with asyncio session .

    Args:
        apply_migrations ([type]): fixture used to perform migrations to DB

    Returns:
        AsyncGenerator[AsyncSession, None]:

    Yields:
        Iterator[AsyncGenerator[AsyncSession, None]]:
    """
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.rollback()
            await session.close()


@pytest.fixture
@pytest.mark.asyncio
async def populate_part_tbl(part_model_factory) -> None:
    """Populate the part table Fixture.

    Args:
        part_model_factory ([PartModelFactory]): Factory used to generate parts
    """
    part = part_model_factory.create_batch(10)  # noqa:

    # await async_session.commit()


# @pytest.fixture(scope="function")
# @pytest.mark.asyncio
# async def db_ctx(apply_migrations) -> AsyncGenerator[ContextVar, None]:

#     # async with async_session() as session:
#     # Set the injected db_session dependency to the db_session context object
#     db_session_context.set(async_session())
#     yield copy_context()
