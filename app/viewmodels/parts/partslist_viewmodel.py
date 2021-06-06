from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from app.services import part_service
from app.viewmodels.shared.viewmodel import ViewModelBase


class PartslistViewModel(ViewModelBase):
    def __init__(self, request: Request, db: AsyncSession) -> None:
        super().__init__(request)

        self.db = db

    async def load(self) -> None:

        self.part_count = await part_service.get_part_count(self.db)
