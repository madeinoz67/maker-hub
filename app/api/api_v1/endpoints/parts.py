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


@router.post("/", response_model=PartPublicSchema, name="part:create", tags=["Parts"])
async def create_one(
    details: PartCreateSchema,
    __body: bool = True,
    db: AsyncSession = Depends(get_db_session),
) -> PartPublicSchema:
    """Adds a new part

    This will create a new part and assign it a unique string Id at a minimum.
    if no name is given the id will be assigned to the name.
    """

    # TODO: use contextvar for db dependencies when https://github.com/pytest-dev/pytest-asyncio/pull/161 is merged
    # Set the injected db_session dependency to the db_session context object
    # db_session_context.set(db_session)

    try:
        part = await part_service.create_part(
            db,
            details
            # name,
            # description,
            # notes=partDetail.notes,
            # footprint=partDetail.footprint,
            # manufacturer=partDetail.manufacturer,
            # mpn=partDetail.mpn,
        )

        part.href = (
            f'{__host}:{__port}{router.url_path_for("get_part", part_id=part.id)}'
        )
        if __body:
            return part
        else:
            return Response()
    except IntegrityError as ex:
        # await session.rollback()
        logger.error(f"The Part ID ({part.part_id}) already exists.", ex)
        raise DuplicatedEntryError("The Part ID already exists")


@router.post(
    "/datatable", response_model=PartDataTableResponse, name="part:tablesource"
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


@router.delete("/{part_id}", name="part:delete")
async def delete_part(
    part_id: str, db_session: AsyncSession = Depends(get_db_session)
) -> Response:

    # Set the injected db_session dependency to the db_session context object
    db_session_context.set(db_session)

    result = await part_service.delete_part(part_id)
    # if result != part_id:
    #     raise HTTPException(status_code=404, detail="part not deleted")
    return Response(status_code=status.HTTP_204_NO_CONTENT, content=result)


@router.get("/", response_model=PartPublicSchema, name="part:getall")
async def get_all():
    return Response(status_code=status.HTTP_204_NO_CONTENT, content=[])


@router.get("/{part_id}", response_model=PartPublicSchema, name="part:get")
async def get_part(
    part_id: str, db_session: AsyncSession = Depends(get_db_session)
) -> PartPublicSchema:
    # Set the injected db_session dependency to the db_session context object
    db_session_context.set(db_session)

    # result = await part_service.delete_part(part_id)
    # if result != part_id:
    #     raise HTTPException(status_code=404, detail="part not deleted")
    return Response(status_code=status.HTTP_204_NO_CONTENT, content=[])


@router.patch("/{part_id}", response_model=PartPublicSchema, name="part:update")
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
