from starlette.requests import Request

from app.services import storage_service
from app.viewmodels.shared.viewmodel import ViewModelBase


class StoragelistViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.project_count: int = 0

    async def load(self):
        self.project_count = await storage_service.get_location_count()
