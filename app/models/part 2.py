import datetime

from typing import List

import sqlalchemy as sa
import sqlalchemy.orm as orm
from app.models.modelbase import SqlAlchemyBase

from app.models.stock import Stock


class Part(SqlAlchemyBase):
    __tablename__ = "parts"

    id: str = sa.Column(sa.String, primary_key=True)
    created_date: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True
    )
    last_updated: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True
    )
    name: str = sa.Column(sa.String, index=True)
    description: str = sa.Column(sa.String, index=True)
    notes: str = sa.Column(sa.String, nullable=True)
    footprint: str = sa.Column(sa.String, nullable=True, index=True)
    manufacturer: str = sa.Column(sa.String, nullable=True, index=True)
    mpn: str = sa.Column(
        sa.String, nullable=True, index=True
    )  # Manufacturers Part Number

    # stock relationship
    stock: List[Stock] = orm.relationship(
        Stock, order_by=[Stock.last_updated], back_populates="part"
    )


def __repr__(self):
    return "<Part {}>".format(self.id)
