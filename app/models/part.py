import datetime
from typing import List, Optional

from beanie import Document
from pydantic import Field, HttpUrl

from app.models.core import CoreModel, IDModelMixin
from app.models.datatable import DataTableResponseBase


class PartStockItem(CoreModel):
    comments: Optional[str] = Field(None)
    currency: Optional[str] = Field(None)
    price: float = Field(0.0)
    quantity: int = Field(1)
    storage_id: Optional[str] = Field(None)
    timestamp: Optional[datetime.datetime] = Field(datetime.datetime.now())


class PartBaseModel(CoreModel):
    description: Optional[str] = Field(None)
    footprint: Optional[str] = Field(None)
    stock: Optional[List[PartStockItem]] = Field(None)
    tags: Optional[List[str]] = Field(None)
    notes: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    mpn: Optional[str] = Field(None)
    manufacturer: Optional[str] = Field(None)
    created_at: Optional[datetime.datetime] = Field(datetime.datetime.now())
    updated_at: Optional[datetime.datetime] = Field(datetime.datetime.now())


class PartPublicModel(IDModelMixin):
    description: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    href: Optional[HttpUrl] = None


class PartPublicResponseModel(CoreModel):
    count: int = 0
    next: Optional[HttpUrl] = None
    previous: Optional[HttpUrl] = None
    results: List[PartPublicModel] = []


class PartTableResponse(DataTableResponseBase):
    data: List[PartPublicModel] = []


class PartDB(IDModelMixin, PartBaseModel, Document):
    pass
