import datetime
from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as orm

from app.models.modelbase import SqlAlchemyBase


class Project(SqlAlchemyBase):
    __tablename__ = "projects"

    id: str = sa.Column(sa.String, primary_key=True)
    created_date: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True
    )
    last_updated: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True
    )
    name: str = sa.Column(sa.String, index=True)
    description: str = sa.Column(sa.String, index=True)

    # TODO: Project Parts Join
    # if parts is None:
    #     parts = []
    # self.parts = parts


def __repr__(self):
    return f"<Project {self.id}>"
