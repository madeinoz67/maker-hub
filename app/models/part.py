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


class PartPublicModel(IDModelMixin, PartBaseModel):
    id: str
    href: Optional[HttpUrl] = None

    class Config:
        schema_extra = {
            "example": {
                "id": "1",
                "href": "http://localhost:8000/api/v1/parts/1",
                "name": "Part 1",
                "description": "Part 1 description",
                "footprint": "SOT23",
                "tags": ["tag1", "tag2"],
                "stock": [
                    {
                        "quantity": 1,
                        "price": 1.0,
                        "currency": "USD",
                        "comments": None,
                        "storage_id": 1234,
                        "timestamp": "2020-01-01T01:00:00Z",
                    }
                ],
                "created_at": "2020-01-01T01:00:00",
                "updated_at": "2020-01-01T01:00:00",
            }
        }


class PartPublicResponseModel(CoreModel):
    count: int = 0
    next: Optional[HttpUrl] = None
    previous: Optional[HttpUrl] = None
    results: List[PartPublicModel] = []

    class Config:
        schema_extra = {
            "example": {
                "count": 20,
                "next": "http://localhost:8000/api/v1/parts/21",
                "previous": None,
                "results": [
                    {
                        "id": "1",
                        "href": "http://localhost:8000/api/v1/parts/1",
                        "name": "Part 1",
                        "description": "Part 1 description",
                        "footprint": "SOT23",
                        "tags": ["tag1", "tag2"],
                        "stock": [
                            {
                                "quantity": 1,
                                "price": 1.0,
                                "currency": "USD",
                                "comments": None,
                                "storage_id": 1234,
                                "timestamp": "2020-01-01T01:20:00Z",
                            }
                        ],
                        "created_at": "2020-01-01T01:00:00",
                        "updated_at": "2020-01-01T01:20:00",
                    }
                ],
            }
        }


class PartTableResponse(DataTableResponseBase):
    data: List[PartPublicModel] = []


class PartCreateModel(PartBaseModel):
    name: str

    class Config:
        schema_extra = {
            "example": {
                "name": "Part 1",
                "description": "Part 1 description",
                "footprint": "SOT23",
                "tags": ["tag1", "tag2"],
            }
        }


class PartUpdateModel(PartBaseModel):
    pass

    class Config:
        schema_extra = {
            "example": {
                "name": "Part 1",
                "description": "Part 1 description",
                "footprint": "SOT23",
                "tags": ["tag1", "tag2"],
            }
        }


class PartDB(IDModelMixin, PartBaseModel, Document):
    pass
