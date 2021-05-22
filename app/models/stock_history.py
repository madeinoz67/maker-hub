from app.models.location import Location
from app.models.part import Part
import datetime


class StockHistory:
    def __init__(self, part: Part, price, quantity: int, location: Location):
        self.price = price
        self.quantity = quantity
        self.locations = location
