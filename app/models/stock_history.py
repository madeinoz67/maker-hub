from app.models.location import LocationModel
from app.models.modelbase import SqlAlchemyBase
from app.models.part import PartModel


class StockHistoryModel(SqlAlchemyBase):
    __tablename__ = "stockhistory"

    def __init__(self, part: PartModel, price, quantity: int, location: LocationModel):
        self.price = price
        self.quantity = quantity
        self.locations = location
        self.part = part
