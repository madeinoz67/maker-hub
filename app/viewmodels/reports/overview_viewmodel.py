from starlette.requests import Request

from app.services import part_service, project_service, storage_service
from app.viewmodels.shared.viewmodel import ViewModelBase


class OverviewViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

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
        # Parts Stats
        self.total_parts = await part_service.get_part_count()
        self.total_stock = await part_service.get_total_stock()
        self.stock_value = await part_service.get_stock_value()

        # Location Stats
        self.locations_total = await storage_service.get_location_count()
        self.locations_used = await storage_service.get_locations_used()

        # Project Stats
        self.project_count = await project_service.get_project_count()
