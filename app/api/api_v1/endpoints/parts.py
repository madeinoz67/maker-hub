#
# Copyright 2021 Stephen Eaton
#
# This file is part of Maker-Hub.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the 'Software'), to deal
# in the Software without restriction, including without limitation the rights,
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""parts

V1 parts api routes
"""

import fastapi
from fastapi import Depends, Response, status
from loguru import logger
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.exceptions import DuplicatedEntryError
from app.core.config import settings
from app.db.session import db_session_context, get_db_session
from app.schema.datatable import DataTableRequest, PartDataTableResponse
from app.schema.part import PartCreateSchema, PartPublicSchema, PartUpdateSchema
from app.services import part_service

router = fastapi.APIRouter()

__host = settings.HOST
__port = settings.PORT


@router.post(
    "/",
    response_model=PartPublicSchema,
    status_code=status.HTTP_201_CREATED,
    name="add_part",
    tags=["Parts"],
)
async def add_one(
    details: PartCreateSchema,
    __body: bool = True,
    db: AsyncSession = Depends(get_db_session),
) -> PartPublicSchema:

    """Add a new part.

    This will create a new part and assign it a unique string Id at a minimum.
    if no name is given the id will be assigned to the name.
    """

    # TODO: use contextvar for db dependencies when https://github.com/pytest-dev/pytest-asyncio/pull/161 is merged
    # Set the injected db_session dependency to the db_session context object
    # db_session_context.set(db_session)

    try:
        part = await part_service.create_part(db, details)

        part.href = f'{__host}:{__port}{router.url_path_for("add_part")}'  # TODO: Reverse lookup not working
        if __body:
            return part
        else:
            return Response()
    except IntegrityError as ex:
        logger.error(f"The Part ID ({part.part_id}) already exists.", ex)
        raise DuplicatedEntryError(f"The Part with Id='{part.part_id}' already exists.")


@router.post(
    "/datatable", response_model=PartDataTableResponse, name="part_tablesource"
)
async def table_datasource(
    request: DataTableRequest,
    db_session: AsyncSession = Depends(get_db_session),
) -> PartDataTableResponse:
    """Servers side processing for Parts List Datatable

    This performs the server-side processing for the Part List Datatable

    """
    # Set the injected db_session dependency to the db_session context object
    db_session_context.set(db_session)

    draw = request.draw

    data = await part_service.get_part_datatable(request)
    return PartDataTableResponse(
        draw=draw, recordsTotal=100, recordsFiltered=100, data=data
    )


@router.delete("/{part_id}", name="delete_part")
async def delete_part(
    part_id: str, db_session: AsyncSession = Depends(get_db_session)
) -> Response:

    # Set the injected db_session dependency to the db_session context object
    db_session_context.set(db_session)

    result = await part_service.delete_part(db_session, part_id)
    # if result != part_id:
    #     raise HTTPException(status_code=404, detail="part not deleted")
    return Response(status_code=status.HTTP_204_NO_CONTENT, content=result)


@router.get("/", response_model=PartPublicSchema, name="get all parts")
async def get_all():
    return Response(status_code=status.HTTP_204_NO_CONTENT, content=[])


@router.get("/{part_id}", response_model=PartPublicSchema, name="get part")
async def get_part(
    part_id: str, db_session: AsyncSession = Depends(get_db_session)
) -> PartPublicSchema:
    # Set the injected db_session dependency to the db_session context object
    db_session_context.set(db_session)

    # result = await part_service.delete_part(part_id)
    # if result != part_id:
    #     raise HTTPException(status_code=404, detail="part not deleted")
    return Response(status_code=status.HTTP_204_NO_CONTENT, content=[])


@router.patch("/{part_id}", response_model=PartPublicSchema, name="update part")
async def update_part(
    part_id: str,
    details: PartUpdateSchema,
    __body: bool = True,
    db_session: AsyncSession = Depends(get_db_session),
) -> PartPublicSchema:
    # Set the injected db_session dependency to the db_session context object
    db_session_context.set(db_session)

    part = await part_service.update_part(part_id, details)
    part.href = f'{__host}:{__port}{router.url_path_for("get_part", part_id=part.id)}'
    return Response(status_code=status.HTTP_204_NO_CONTENT, content=part)
