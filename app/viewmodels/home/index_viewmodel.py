from starlette.requests import Request

from app.services import part_service, project_service, storage_service
from app.viewmodels.shared.viewmodel import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.part_count: int = part_service.get_part_count()
        self.location_count: int = storage_service.get_location_count()
        self.project_count: int = project_service.get_project_count()
        self.latest_parts = part_service.get_latest_parts(limit=7)
        self.latest_projects = project_service.get_latest_projects(limit=7)
