import datetime
from typing import List

from beanie import Document


class Stock(Document):
    id: int
    created_date: datetime.datetime
    last_updated: datetime.datetime
    quantity: int
    comment: str

    # Part relationship
    # part_id: str


# TODO: Add Location relationship
# location: List[Location] = orm.relationship(
#     Location, order_by=[Location.name], back_populates="stock"
# )
