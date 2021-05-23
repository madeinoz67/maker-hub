from starlette.requests import Request

from app.services import part_service, storage_service, project_service
from app.viewmodels.shared.viewmodel import ViewModelBase


class OverviewViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        # Parts Stats
        self.total_parts: int = part_service.get_part_count()
        self.total_stock: int = part_service.get_total_stock()
        self.stock_value: float = part_service.get_stock_value()

        # Location Stats
        self.locations_total: int = storage_service.get_location_count()
        self.locations_used: int = storage_service.get_locations_used()

        # Project Stats
        self.project_count: int = project_service.get_project_count()
