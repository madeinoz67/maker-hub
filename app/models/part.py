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

import sqlalchemy as sa
from nanoid import generate

from app.core.config import settings
from app.models.modelbase import SqlAlchemyBase

_alphabet = settings.NANOID_ALPHABET
_size = settings.NANOID_SIZE


def nanoid() -> str:
    """Wrapper for nanoid generation

    Returns:
        str: nanoid
    """
    return generate(_alphabet, _size)


class PartModel(SqlAlchemyBase):
    __tablename__ = "part"

    id: str = sa.Column(
        sa.String(length=settings.NANOID_SIZE),
        primary_key=True,
        autoincrement=False,
        default=nanoid,
    )
    name: str = sa.Column(sa.String, index=True, default=id)
    description: str = sa.Column(sa.String, nullable=True, index=True)
    created_at: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True
    )
    updated_at: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True
    )
    notes: str = sa.Column(sa.String, nullable=True)
    footprint: str = sa.Column(sa.String, nullable=True, index=True)
    manufacturer: str = sa.Column(sa.String, nullable=True, index=True)
    mpn: str = sa.Column(
        sa.String, nullable=True, index=True
    )  # Manufacturers Part Number

    # # stock relationship
    # stock: List[Stock] = orm.relationship(
    #     Stock, order_by=[Stock.last_updated], back_populates="part"
    # )

    def __repr__(self):
        return "<Part {}>".format(self.id)
