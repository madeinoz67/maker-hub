import datetime
from typing import List

from loguru import logger
from nanoid import generate
from sqlalchemy import delete, func, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.config import settings
from app.db.session import db_session_context
from app.models.part import PartModel
from app.schema.datatable import DataTableRequest, PartDataTableResponse
from app.schema.part import PartCreateSchema, PartUpdateSchema

# async def get_part_datatable(request: DataTableRequest) -> PartDataTableResponse:
#     """generates data for the datatable request

#     Will perform, sorting of column, search all searchable columns and paginate results.

#     Args:
#         request (DataTableRequest): request from the datable

#     Returns:
#         List[Part]: [description]
#     """

#     async with db_session.create_async_session() as session:
#         # session.add(part)
#         await session.commit()
#     return []

_alphabet = settings.NANOID_ALPHABET
_size = settings.NANOID_SIZE


async def get_part_datatable(request: DataTableRequest) -> PartDataTableResponse:
    return PartDataTableResponse()


async def update_part(part_id: str, part: PartUpdateSchema):

    part.updated_at = datetime.datetime.now()

    # get our db_session dependency
    db_session: AsyncSession = db_session_context.get()
    async with db_session as session:
        results = await session.execute(
            select(PartModel).filter(PartModel.id == part_id)
        )

        part = results.scalar_one_or_none()
        # part.name
        # part_to_update.description = part.description

        stmt = update(PartModel).where(PartModel.id == part_id)
        results = await session.execute(stmt)
        await session.commit()
    return results


async def delete_part(part_id: str):

    # get our db_session dependency
    db_session: AsyncSession = db_session_context.get()
    with db_session as session:

        try:
            stmt = delete(PartModel).where(PartModel.id == part_id)
            result = session.execute(stmt)
            await session.commit()
            return result
        except IntegrityError as ex:
            await session.rollback()
            logger.error("Part does not exist", ex)


async def create_part(details: PartCreateSchema) -> PartModel:
    """Creates a new Part and saves to db

    Args:
        details (PartCreate): details of Part to create

    Returns:
        part (PartPublic): the newly created Part
    """

    part = PartModel()

    part.id = generate(_alphabet, _size)

    if details.name is None:
        details.name = part.id
    part.name = details.name
    part.description = details.description
    part.notes = details.notes
    part.footprint = details.footprint
    part.manufacturer = details.manufacturer
    part.mpn = details.mpn

    # get our db_session dependency
    db_session: AsyncSession = db_session_context.get()
    async with db_session as session:
        session.add(part)
        try:
            await session.commit()

        except IntegrityError as ex:
            await session.rollback()
            logger.error("Part ID already exists in the database", ex)

    return part


async def get_part_count() -> int:

    # get our db_session dependency
    db_session: AsyncSession = db_session_context.get()
    async with db_session as session:
        query = select(func.count(PartModel.id))
        results = await session.execute(query)

    return results.scalar()


# TODO: Finish get total stock
async def get_total_stock() -> int:
    return 1_000


# TODO: Finish get part stock
async def get_stock_value() -> float:
    return 1_500.00


async def get_latest_parts(start: int = 0, limit: int = 5) -> List[PartModel]:

    start = max(0, start)
    limit = max(0, limit)

    logger.debug("Entering - get_latest_parts()")

    # get our db_session dependency
    db_session: AsyncSession = db_session_context.get()
    async with db_session as session:
        query = select(PartModel).order_by(PartModel.created_at.desc()).limit(limit)

        results = await session.execute(query)
        parts = results.scalars()

    return list(parts)
