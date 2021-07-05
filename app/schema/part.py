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

import datetime
from typing import List, Optional

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


class PartPublicResponseSchema(CoreSchema):
    count: int = 0
    next: Optional[HttpUrl] = None
    previous: Optional[HttpUrl] = None
    results: List[PartPublicSchema] = []
