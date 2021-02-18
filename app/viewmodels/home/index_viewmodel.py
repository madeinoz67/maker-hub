from typing import List

from starlette.requests import Request

from app.services import part_service, project_service, storage_service
from app.viewmodels.shared.viewmodel import ViewModelBase


class IndexViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.part_count: int = part_service.part_count()
        self.location_count: int = storage_service.location_count()
        self.project_count: int = project_service.project_count()
        self.latest_parts = part_service.latest_parts(limit=7)
        self.latest_projects = project_service.latest_projects(limit=7)
