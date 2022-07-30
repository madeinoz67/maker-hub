import datetime
from typing import List, Optional

from beanie import Document
from pydantic import BaseModel


class Part(Document):
    id: str
    created_date: datetime.datetime = datetime.datetime.now()
    last_updated: datetime.datetime = datetime.datetime.now()
    name: str
    description: str
    notes: Optional[str]
    footprint: Optional[str]


def __repr__(self):
    return f"<Part {self.id}>"
