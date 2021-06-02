import logging
import pathlib
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

# we're appending the app directory to our path here so that we can import config easily
sys.path.append(str(pathlib.Path(__file__).resolve().parents[3]))

# app specific imports
import app.models.__all_models  # noqa:
from app.core import config as cfg

# noinspection PyUnresolvedReferences
from app.models.modelbase import SqlAlchemyBase

# Alembic Config object, which provides access to values within the .ini file
config = context.config

# Interpret the config file for logging
fileConfig(config.config_file_name)
logger = logging.getLogger("alembic.env")

DATABASE_URL = cfg.get_settings().DATABASE_URL  # maker-hub environment variable

# we don't need to run alembic sqlite in async mode so strip out sqlite async driver
if DATABASE_URL:
    if DATABASE_URL.__contains__("sqlite+aiosqlite"):
        logger.info(
            "DETECTED aiosqlite driver, stripping from DATABASE_URL for migration"
        )
        DATABASE_URL = DATABASE_URL.replace("+aiosqlite", "")

    config.set_main_option("sqlalchemy.url", DATABASE_URL)
else:
    logger.warning(
        "Environment variable DATABASE_URL is missing - use default alembic.ini configuration"
    )
logger.info(f"Database URL: {DATABASE_URL}")

target_metadata = SqlAlchemyBase.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    logger.info("Running migrations offline")
    run_migrations_offline()
else:
    logger.info("Running migrations online")
    run_migrations_online()
