import datetime

from app.models.modelbase import SqlAlchemyBase
from app.models.part import PartModel


class StockOrderModel(SqlAlchemyBase):
    __tablename__ = "stockorder"

    def __init__(
        self,
        part: PartModel,
        quantity: int,
        source: str,
        order_number: str = None,
        date_ordered: datetime.datetime = None,
        comment: str = None,
        deliver_date: datetime.datetime = None,
    ):
        self.part = part
        self.source = source
        self.order_number = order_number
        self.date_ordered = date_ordered
        self.quantity = quantity
        self.deliver_date = deliver_date
        self.comment = comment
