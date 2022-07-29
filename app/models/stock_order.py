import datetime

from app.models.part import Part


class StockOrder:
    def __init__(
        self,
        part: Part,
        quantity: int,
        source: str,
        order_number: str = None,
        date_ordered: datetime.datetime,
        comment: str = None,
        deliver_date: datetime = None,
    ):
        self.part = part
        self.source = source
        self.order_number = order_number
        self.date_ordered = date_ordered
        self.quantity = quantity
        self.deliver_date = deliver_date
        self.comment = comment
