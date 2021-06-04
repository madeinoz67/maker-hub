import datetime
from typing import Optional

from pydantic import HttpUrl

from app.schema.core import CoreSchema, IDSchemaMixin


class PartBaseSchema(CoreSchema):
    name: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[str] = None
    footprint: Optional[str] = None
    manufacturer: Optional[str] = None
    mpn: Optional[str] = None
    created_at: Optional[datetime.datetime] = None
    updated_at: Optional[datetime.datetime] = None

    class Config:
        orm_mode = True


class PartCreateSchema(PartBaseSchema):
    name: str


class PartUpdateSchema(PartBaseSchema):
    pass


class PartInDBSchema(IDSchemaMixin, PartBaseSchema):
    name: str


class PartPublicSchema(IDSchemaMixin, PartBaseSchema):
    id: str
    href: Optional[HttpUrl] = None
