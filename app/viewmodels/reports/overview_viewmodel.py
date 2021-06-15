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

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from app.services import part_service, project_service, storage_service
from app.viewmodels.shared.viewmodel import ViewModelBase


class OverviewViewModel(ViewModelBase):
    """Report Overview View Model Class ."""

    def __init__(self, request: Request, db: AsyncSession) -> None:
        super().__init__(request)

        self.db = db
        # Parts Stats
        self.total_parts: int = 0
        self.total_stock: int = 0
        self.stock_value: float

        # Location Stats
        self.locations_total: int = 0
        self.locations_used: int = 0
        # Project Stats
        self.project_count: int = 0

    async def load(self):
        """Load service data into the view model ."""
        # Parts Stats
        self.total_parts = await part_service.get_part_count(self.db)
        self.total_stock = await part_service.get_total_stock()
        self.stock_value = await part_service.get_stock_value()

        # Location Stats
        self.locations_total = await storage_service.get_location_count()
        self.locations_used = await storage_service.get_locations_used()

        # Project Stats
        self.project_count = await project_service.get_project_count()
