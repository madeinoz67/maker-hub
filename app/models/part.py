import datetime

import sqlalchemy as sa

from app.models.modelbase import SqlAlchemyBase


class PartModel(SqlAlchemyBase):
    __tablename__ = "part"

    id: str = sa.Column(sa.String, primary_key=True)
    name: str = sa.Column(sa.String, index=True)
    description: str = sa.Column(sa.String, nullable=True, index=True)
    created_at: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True
    )
    updated_at: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True
    )
    notes: str = sa.Column(sa.String, nullable=True)
    footprint: str = sa.Column(sa.String, nullable=True, index=True)
    manufacturer: str = sa.Column(sa.String, nullable=True, index=True)
    mpn: str = sa.Column(
        sa.String, nullable=True, index=True
    )  # Manufacturers Part Number

    # # stock relationship
    # stock: List[Stock] = orm.relationship(
    #     Stock, order_by=[Stock.last_updated], back_populates="part"
    # )

    def __repr__(self):
        return "<Part {}>".format(self.id)
