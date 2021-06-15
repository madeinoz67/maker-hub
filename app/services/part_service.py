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

"""part_service.

All underlying functionality relating to Parts
"""

import datetime
from typing import List

from loguru import logger
from sqlalchemy import delete, func, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

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


async def get_part_datatable(request: DataTableRequest) -> PartDataTableResponse:
    """Retrieve a part datatable response .

    Used by the datatable component on the parts page
    see: (https://datatables.net/)

    Args:
        request (DataTableRequest):

    Returns:
        PartDataTableResponse:
    """
    return PartDataTableResponse()


async def update_part(part_id: str, part: PartUpdateSchema) -> PartModel:
    """Update a part .

    Args:
        part_id (str): NanoId of Part to update
        part (PartUpdateSchema): Information to update

    Returns:
        [PartModel]: update Part
    """
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


async def delete_part(db: AsyncSession, part_id: str):
    """Delete a part by ID.

    Args:
        part_id (str): NanoId Of Part being deleted

    Returns:
        [type]: [description]
    """
    # get our db_session dependency
    # db_session: AsyncSession = db_session_context.get()
    async with db as session:
        try:
            stmt = delete(PartModel).where(PartModel.id == part_id)
            result = await session.execute(stmt)
            await session.commit()
            return result
        except IntegrityError as ex:
            await session.rollback()
            logger.error("Part does not exist", ex)
            raise ex


async def create_part(db: AsyncSession, details: PartCreateSchema) -> PartModel:
    """Create a Part in the database .

    Args:
        db (AsyncSession): [databases session]
        details (PartCreateSchema): [schema containing new part details]

    Raises:
        ex: [IntegrityError - if a part with the same ID already exists in the
            database]

    Returns:
        PartModel: [newly created part model]
    """
    part = PartModel()

    part.name = details.name
    part.description = details.description
    part.notes = details.notes
    part.footprint = details.footprint
    part.manufacturer = details.manufacturer
    part.mpn = details.mpn

    # TODO: use contextvar for db dependencies when https://github.com/pytest-dev/pytest-asyncio/pull/161 is merged
    # db_session: AsyncSession = db_session_context.get()
    db_session: AsyncSession = db
    async with db_session as session:
        session.add(part)
        try:
            await session.commit()

        except IntegrityError as ex:
            await session.rollback()
            logger.error(f"Part ID {part.id} already exists in the database", ex)
            raise ex

    return part


async def get_part_count(db: AsyncSession) -> int:
    """Return the number of parts in the database .

    Args:
        db (AsyncSession): [db session]

    Returns:
        int: [count of parts in the database]
    """
    # TODO: use contextvar for db dependencies when https://github.com/pytest-dev/pytest-asyncio/pull/161 is merged
    # get our db_session dependency
    # db_session: AsyncSession = db_session_context.get()
    db_session = db
    async with db_session as session:
        query = select(func.count(PartModel.id))
        results = await session.execute(query)

    return results.scalar()


# TODO: Finish get total stock
async def get_total_stock() -> int:
    """Get the total stock for a part.

    Returns:
        int: [description]
    """
    return 1_000


# TODO: Finish get part stock
async def get_stock_value() -> float:
    """Get stock value .

    Returns:
        float: [description]
    """
    return 1_500.00


async def get_latest_parts(start: int = 0, limit: int = 5) -> List[PartModel]:
    """Get latest parts sorted by date.

    Args:
        start (int, optional): pagination parts being returned. Defaults to 0.
        limit (int, optional): number of parts to return. Defaults to 5.

    Returns:
        List[PartModel]: list of latest parts to be added, sorted by date.
    """
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
