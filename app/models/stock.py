import datetime

import sqlalchemy as sa
import sqlalchemy.orm as orm

from app.models.modelbase import SqlAlchemyBase


class StockModel(SqlAlchemyBase):
    __tablename__ = "stock"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True
    )
    last_updated: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True
    )
    quantity: int = sa.Column(sa.Integer)
    comment: str = sa.Column(sa.String, nullable=True)

    # Part relationship
    part_id: str = sa.Column(sa.String, sa.ForeignKey("part.id"))
    part = orm.relation("PartModel")

    # TODO: Add Location relationship
    # location: List[Location] = orm.relationship(
    #     Location, order_by=[Location.name], back_populates="stock"
    # )
