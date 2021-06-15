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
import sqlalchemy.orm as orm

from app.models.modelbase import SqlAlchemyBase


class StockModel(SqlAlchemyBase):
    __tablename__ = "stock"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    created_date: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True
    )
    last_updated: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True
    )
    quantity: int = sa.Column(sa.Integer)
    comment: str = sa.Column(sa.String, nullable=True)

    # Part relationship
    part_id: str = sa.Column(sa.String, sa.ForeignKey("part.id"))
    part = orm.relation("PartModel")

    # TODO: Add Location relationship
    # location: List[Location] = orm.relationship(
    #     Location, order_by=[Location.name], back_populates="stock"
    # )
