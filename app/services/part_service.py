import datetime

from fastapi import Depends
from loguru import logger
from nanoid import generate
from sqlalchemy import delete, func, update
from sqlalchemy.exc import IntegrityError

from app.core import config
from app.db import db_session
from app.models.part import PartModel
from app.schema.part import PartCreate, PartUpdate

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

_alphabet = config.get_settings().nanoid_alphabet
_size = config.get_settings().nanoid_size


def PartService(BaseDBService):
    """Part Service

    Defines the Parts Service

    """

    __instance = None

    def getInstance() -> PartService:
        """Static access method"""

        if PartService.__instance is None:
            PartService()
        return PartService.__instance

    def __init__(self):
        super(PartService, self).__init__()
        if PartService.__instance is not None:
            raise Exception(
                "This class is a singleon, you must call PartService.getInstance() to return its instance"
            )
        else:
            PartService.__instance = self


async def update_part(part_id: str, part: PartUpdate):

    part.last_updated = datetime.datetime.now()
    async with db_session.create_async_session() as session:
        results = await session.execute(select(Part).filter(Part.id == part_id))

        part = results.scalar_one_or_none()
        # part.name
        # part_to_update.description = part.description

        stmt = update(Part).where(Part.id == part_id)
        results = await session.execute(stmt)
        await session.commit()
    return results


async def delete_part(part_id: str):
    with db_session.create_async_session() as session:

        try:
            stmt = delete(Part).where(Part.id == part_id)
            result = session.execute(stmt)
            await session.commit()
            return result
        except IntegrityError as ex:
            await session.rollback()
            logger.error("Part does not exist", ex)


async def create_part(details: PartCreate) -> PartModel:
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

    async with db_session.create_session() as session:
        session.add(part)
        try:
            await session.commit()

        except IntegrityError as ex:
            await session.rollback()
            logger.error("Part ID already exists in the database", ex)

    return part


def get_part_count() -> int:

    async with db_session.create_session() as session:
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
    async with db_session.create_async_session() as session:
        query = select(PartModel).order_by(PartModel.created_at.desc()).limit(limit)

        results = await session.execute(query)
        parts = results.scalars()

    return list(parts)
