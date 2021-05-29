import datetime
from typing import Optional

from pydantic import HttpUrl

from app.schema.core import CoreSchema, IDSchemaMixin


class PartBase(CoreSchema):
    name: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[str] = None
    footprint: Optional[str] = None
    manufacturer: Optional[str] = None
    mpn: Optional[str] = None

    class Config:
        orm_mode = True


class PartCreate(PartBase):
    name: str


class PartUpdate(PartBase):
    pass


class PartInDB(IDSchemaMixin, PartBase):
    name: str


class PartPublic(IDSchemaMixin, PartBase):
    href: Optional[HttpUrl] = None
    created_at: datetime.datetime
    updated_at: datetime.datetime
