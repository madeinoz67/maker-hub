import sqlalchemy as sa

from app.models.modelbase import SqlAlchemyBase


class LocationModel(SqlAlchemyBase):
    __tablename__ = "locations"

    id: str = sa.Column(sa.String, primary_key=True)
    name: str = sa.Column(sa.String)

    def __repr__(self):
        return "<Location {}>".format(self.id)
