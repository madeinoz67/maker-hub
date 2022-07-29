from typing import List

from starlette.requests import Request

from app.services import project_service
from app.viewmodels.shared.viewmodel import ViewModelBase


class ProjectlistViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.project_count: int = 0
        self.projects: List = []

    def load(self):
        self.project_count: int = project_service.get_project_count()
        self.projects = project_service.get_latest_projects(limit=30)
