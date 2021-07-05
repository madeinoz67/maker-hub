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

# import asyncio
# import os
# from unittest import mock

import pytest
from loguru import logger  # noqa:
from sqlalchemy.ext.asyncio import AsyncSession  # noqa:
from sqlalchemy.future import select

from app.models.part import PartModel
from app.services import part_service
from tests.factories import PartModelFactory


class TestPartService:
    @pytest.mark.asyncio
    async def test_add_single_part(
        self,
        part_create_schema_factory,
        db_session,
    ):

        obj_in = part_create_schema_factory.build()

        item: PartModel = await part_service.create_part(db_session, obj_in)  # noqa:

        assert item.name == obj_in.name
        assert item.id is not None
        assert len(item.id) == 26

    @pytest.mark.asyncio
    async def test_add_multi_parts(
        self,
        part_create_schema_factory,
        db_session,
    ):

        obj_in = part_create_schema_factory.build()

        item1: PartModel = await part_service.create_part(db_session, obj_in)  # noqa:

        assert item1.name == obj_in.name
        assert item1.id is not None
        assert len(item1.id) == 26

        obj_in = part_create_schema_factory.build()

        item2: PartModel = await part_service.create_part(db_session, obj_in)  # noqa:

        assert item2.name == obj_in.name
        assert item2.id is not None
        assert len(item2.id) == 26

        assert item1.id != item2.id

    @pytest.mark.asyncio
    async def test_part_count(self, db_session, part_create_schema_factory):

        assert await part_service.get_part_count(db_session) == 0

        await part_service.create_part(db_session, part_create_schema_factory.build())

        assert await part_service.get_part_count(db_session) == 1

    @pytest.mark.asyncio
    async def test_part_delete(self, db_session, part_model_factory: PartModelFactory):

        async with db_session as session:
            part_model_factory._meta.sqlalchemy_session = session

            part: PartModel = part_model_factory.create()
            result = await session.execute(
                select(PartModel).where(PartModel.id == part.id)
            )
            assert result.scalar_one() is not None

            await part_service.delete_part(session, part.id)

            result = await session.execute(select(PartModel))
            assert result.scalar_one_or_none() is None

    # @pytest.mark.asyncio
    # async def test_part_update(
    #     self,
    #     db_session,
    #     part_update_schema_factory: PartUpdateSchemaFactory,
    #     part_model_factory: PartModelFactory,
    # ):

    #     async with db_session as session:
    #         part_model_factory._meta.sqlalchemy_session = session

    #         part: PartModel = part_model_factory.create()
    #         result = await session.execute(
    #             select(PartModel).where(PartModel.id == part.id)
    #         )
    #         assert result.scalar_one() is not None
