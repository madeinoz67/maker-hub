#
# Copyright 2021 Stephen Eaton
#
# This file is part of Maker-Hub.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from app.schema.part import PartPublicSchema
from app.services import part_service, project_service, storage_service
from app.viewmodels.shared.viewmodel import ViewModelBase


class IndexViewModel(ViewModelBase):
    """Index view model Class ."""

    def __init__(self, request: Request, db: AsyncSession) -> None:
        super().__init__(request)
        self.db = db
        self.part_count: int = 0
        self.location_count: int = 0
        self.project_count: int = 0
        self.latest_parts: List[PartPublicSchema] = []
        self.latest_projects: List[
            PartPublicSchema
        ] = []  # Todo: Change to correct Type once Project schema has been completed

    async def load(self) -> None:
        """Load service data into viewmodel ."""
        self.part_count = await part_service.get_part_count(self.db)
        self.location_count = await storage_service.get_location_count()
        self.project_count = await project_service.get_project_count()
        self.latest_parts = await part_service.get_latest_parts(limit=7)
        self.latest_projects = await project_service.get_latest_projects(limit=7)
