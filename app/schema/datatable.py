#
# Copyright 2021 Stephen Eaton
#
# This file is part of Maker-Hub.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights,
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
