from pydantic import BaseModel

from typing import Optional

import datetime


class Part(BaseModel):
    id: str
    name: str
    description: str
    created_date: datetime.datetime
    last_updated: datetime.datetime
    notes: Optional[str] = None
    footprint: Optional[str] = None
    manufacturer: Optional[str] = None
    mpn: Optional[str] = None

    class Config:
        orm_mode = True
