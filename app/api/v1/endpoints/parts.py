from typing import Optional

import fastapi
from fastapi import Depends, Response, status
from loguru import logger

from app.api.exceptions import DuplicatedEntryError
from app.core.config import settings
from app.models.datatable import DataTableRequest
from app.models.part import PartPublicResponseModel, PartTableResponse
from app.services import part_service

router = fastapi.APIRouter()


@router.get(
    "/",
    response_model=PartPublicResponseModel,
    status_code=status.HTTP_200_OK,
    name="parts_list",
)
async def parts_list(
    id: Optional[str] = None,
    name: Optional[str] = None,
    q: Optional[str] = None,
    limit: Optional[int] = 100,
    offset: Optional[int] = 0,
) -> PartPublicResponseModel:
    """List parts."""

    return PartPublicResponseModel()


@router.post("/datatable")
async def table_datasource(request: DataTableRequest) -> PartTableResponse:
    """Parts Datatable Source

    Returns:
        [TableResponse]: [DataTable Ajax Response]
    """

    draw = request.draw

    data = await part_service.get_latest_parts(
        start=request.start, limit=request.length
    )
    return PartTableResponse(
        draw=draw, recordsTotal=100, recordsFiltered=100, data=data
    )
