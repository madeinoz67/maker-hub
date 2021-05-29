from pathlib import Path
from typing import Callable, Optional

import sqlalchemy as sa
import sqlalchemy.orm as orm
from loguru import logger
from sqlalchemy.orm import Session, sessionmaker

from app.core import config
from app.models.modelbase import SqlAlchemyBase

__factory: Optional[Callable[[], Session]] = None


def global_init(db_file: str):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file.")

    folder = Path(db_file).parent
    folder.mkdir(parents=True, exist_ok=True)

    conn_str = "sqlite+pysqlite:///" + db_file.strip()

    logger.info(f"DB URL: {conn_str}")

    enable_sql_logging = config.get_settings().ENABLE_SQL_LOGGING

    engine = sa.create_engine(
        conn_str, echo=enable_sql_logging, connect_args={"check_same_thread": False}
    )

    __factory = orm.sessionmaker(bind=engine)


def create_session() -> Session:
    global __factory

    if not __factory:
        raise Exception("You must call global_init() before using this method.")

    session: Session = __factory()
    session.expire_on_commit = False

    return session


async def get_session() -> Session:
    session: Session = create_session()
    async with session:
        yield session
