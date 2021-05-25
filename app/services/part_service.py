from app.schema.datatable import PartDataTableResponse
from typing import List, Optional

from app.models import db_session
from app.models.part import Part

from sqlalchemy import func
from sqlalchemy.future import select
from app.schema.datatable import DataTableRequest, PartDataTableResponse

from nanoid import generate


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


async def create_part(
    name: str,
    description: str,
    notes: Optional[str] = None,
    footprint: Optional[str] = None,
    manufacturer: Optional[str] = None,
    mpn: Optional[str] = None,
) -> Part:
    """Creates a new Part and saves to db

    Args:
        name (str): name of the part
        description (str): description of the part

    Returns:
        part (Part): the new Part created with a unique Id
    """
    part = Part()
    part.id = generate(size=16)
    part.name = name
    part.description = description
    part.notes = notes
    part.footprint = footprint
    part.manufacturer = manufacturer
    part.mpn = mpn

    async with db_session.create_async_session() as session:
        session.add(part)
        await session.commit()
    return part


async def get_part_count() -> int:
    async with db_session.create_async_session() as session:
        query = select(func.count(Part.id))
        results = await session.execute(query)

    return results.scalar()


# TODO: Finish get total stock
async def get_total_stock() -> int:
    return 1_000


# TODO: Finish get part stock
async def get_stock_value() -> float:
    return 1_500.00


async def get_latest_parts(start: int = 0, limit: int = 5) -> List[Part]:

    start = max(0, start)
    limit = max(0, limit)

    async with db_session.create_async_session() as session:
        query = select(Part).order_by(Part.created_date.desc()).limit(limit)

        results = await session.execute(query)
        parts = results.scalars()

        return list(parts)
