from starlette.requests import Request

from app.services import part_service
from app.viewmodels.shared.viewmodel import ViewModelBase


class PartslistViewModel(ViewModelBase):
    def __init__(self, request: Request) -> None:
        super().__init__(request)

    async def load(self) -> None:

        self.part_count = await part_service.get_part_count()
