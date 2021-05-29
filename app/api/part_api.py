from typing import Optional

import fastapi
from fastapi import Depends, HTTPException, Response, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.exceptions import DuplicatedEntryError
from app.core import config
from app.models.db_session import get_session
from app.schema.datatable import DataTableRequest, PartDataTableResponse
from app.schema.part import PartCreate, PartPublic, PartUpdate
from app.services import part_service

api = fastapi.APIRouter()

__host = config.get_settings().host
__port = config.get_settings().port


@api.post("/api/parts/datatable", response_model=PartDataTableResponse, tags=["Parts"])
async def table_datasource(request: DataTableRequest) -> PartDataTableResponse:
    """Servers side processing for Parts List Datatable

    This performs the server-side processing for the Part List Datatable

    """

    draw = request.draw

    data = await part_service.get_part_datatable(request)
    return PartDataTableResponse(
        draw=draw, recordsTotal=100, recordsFiltered=100, data=data
    )


@api.post("/api/parts/add", response_model=PartPublic, tags=["Parts"])
async def add_part(details: PartCreate, __body: bool = True) -> PartPublic:
    """Adds a new part

    This will create a new part and assign it a unique string Id.
    """

    try:
        part = await part_service.create_part(
            details
            # name,
            # description,
            # notes=partDetail.notes,
            # footprint=partDetail.footprint,
            # manufacturer=partDetail.manufacturer,
            # mpn=partDetail.mpn,
        )

        part.href = f'{__host}:{__port}{api.url_path_for("get_part", part_id=part.id)}'
        if __body:
            return part
        else:
            return Response()
    except IntegrityError as ex:
        # await session.rollback()
        raise DuplicatedEntryError("The Part ID already exists")


@api.delete("/api/parts/delete/{part_id}", tags=["Parts"])
async def delete_part(part_id: str) -> Response:

    result = await part_service.delete_part(part_id)
    # if result != part_id:
    #     raise HTTPException(status_code=404, detail="part not deleted")
    return Response(status_code=status.HTTP_204_NO_CONTENT, content=result)


@api.get("/api/parts/{part_id}", response_model=PartPublic, tags=["Parts"])
async def get_part(part_id: str) -> PartPublic:

    # result = await part_service.delete_part(part_id)
    # if result != part_id:
    #     raise HTTPException(status_code=404, detail="part not deleted")
    return Response(status_code=status.HTTP_204_NO_CONTENT, content=[])


@api.patch("/api/parts/update/{part_id}", response_model=PartPublic, tags=["Parts"])
async def update_part(
    part_id: str,
    details: PartUpdate,
    __body: bool = True,
) -> PartPublic:

    part = await part_service.update_part(part_id, details)
    part.href = f'{__host}:{__port}{api.url_path_for("get_part", part_id=part.id)}'
    return Response(status_code=status.HTTP_204_NO_CONTENT, content=part)
