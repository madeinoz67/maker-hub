import datetime
from typing import List, Optional

from beanie import Document
from pydantic import BaseModel


class Part(BaseModel):
    id: str
    name: str
    description: str
    notes: Optional[str] = None
    footprint: Optional[str] = None


class PartDB(Part, Document):
    created_date: datetime.datetime = datetime.datetime.now()
    last_updated: datetime.datetime = datetime.datetime.now()
