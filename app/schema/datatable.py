from typing import List, Optional

from pydantic import BaseModel

from app.schema.part import PartPublicSchema


class Search(BaseModel):
    value: str = ""
    regex: bool = False


class Order(BaseModel):
    column: int
    dir: str = "asc"


class Column(BaseModel):
    name: str
    data: str
    searchable: bool = True
    orderable: bool = True
    search: Search


class DataTableBase(BaseModel):
    draw: int


class DataTableRequest(DataTableBase):
    start: int
    length: int
    search: Search
    order: List[Order]
    columns: List[Column]


class DataTableResponseBase(DataTableBase):
    recordsTotal: int
    recordsFiltered: int
    error: Optional[str] = None


class PartDataTableResponse(DataTableBase):
    data: List[PartPublicSchema]


# Example DataTable generated Query
# {
#     "draw": 1,
#     "columns": [
#         {
#             "data": "id",
#             "name": "",
#             "searchable": false,
#             "orderable": false,
#             "search": {"value": "", "regex": false},
#         },
#         {
#             "data": "name",
#             "name": "",
#             "searchable": true,
#             "orderable": true,
#             "search": {"value": "", "regex": false},
#         },
#         {
#             "data": "description",
#             "name": "",
#             "searchable": true,
#             "orderable": true,
#             "search": {"value": "", "regex": false},
#         },
#     ],
#     "order": [{"column": 1, "dir": "asc"}],
#     "start": 0,
#     "length": 100,
#     "search": {"value": "", "regex": false},
# }
