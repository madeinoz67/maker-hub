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

from app.models.modelbase import SqlAlchemyBase


class ProjectModel(SqlAlchemyBase):
    __tablename__ = "project"

    id: str = sa.Column(sa.String, primary_key=True)
    created_date: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True
    )
    last_updated: datetime.datetime = sa.Column(
        sa.DateTime, default=datetime.datetime.now, index=True
    )
    name: str = sa.Column(sa.String, index=True)
    description: str = sa.Column(sa.String, index=True)

    # TODO: Project Parts Join
    # if parts is None:
    #     parts = []
    # self.parts = parts

    def __repr__(self):
        return "<Project {}>".format(self.id)
