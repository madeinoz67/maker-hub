import sqlalchemy as sa
import sqlalchemy.orm as orm
from app.models.modelbase import SqlAlchemyBase


class Location(SqlAlchemyBase):
    __tablename__ = "locations"

    id: str = sa.Column(sa.String, primary_key=True)
    name: str = sa.Column(sa.String)


def __repr__(self):
    return "<Location {}>".format(self.id)
