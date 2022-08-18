import datetime
from typing import Dict, List, Optional

import pymongo
from beanie import Document, Indexed
from pydantic import Field, HttpUrl, root_validator

from app.core.config import settings
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
    description: Optional[str]
    footprint: Optional[str]
    stock: Optional[List[PartStockItem]]
    tags: Optional[List[str]]
    notes: Optional[str]
    name: Optional[str]
    mpn: Optional[str]
    manufacturer: Optional[str]
    created_at: Optional[datetime.datetime] = Field(datetime.datetime.now())
    updated_at: Optional[datetime.datetime] = Field(datetime.datetime.now())


class PartDB(PartBaseModel, Document):
    class Settings:
        name = "parts"
        indexes = [
            [
                ("name", pymongo.TEXT),
                ("description", pymongo.TEXT),
            ],
        ]


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


class PartUpdateModel(PartDB):
    class Config:
        schema_extra = {
            "example": {
                "name": "Part 1",
                "description": "Part 1 description",
                "footprint": "SOT23",
                "tags": ["tag1", "tag2"],
            }
        }


class PartPublicResponseModel(PartDB):
    href: Optional[HttpUrl]

    @root_validator
    def build_href(cls, values) -> Dict:
        if values["id"] is not None:
            values[
                "href"
            ] = f'{settings.BASE_URL}{settings.API_V1_STR}/parts/{values["id"]}'
        return values

    class Config:
        fields = {"id": "id"}
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


class PartListPublicResponseModel(CoreModel):
    count: int = 0
    next: Optional[HttpUrl] = None
    previous: Optional[HttpUrl] = None
    results: List[PartPublicResponseModel] = []

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
    data: List[PartPublicResponseModel] = []
