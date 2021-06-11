# import asyncio
# import os
# from unittest import mock

import pytest
from loguru import logger  # noqa:
from sqlalchemy.ext.asyncio import AsyncSession  # noqa:

from app.models.part import PartModel
from app.services import part_service


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

    # @pytest.mark.asyncio
    # async def test_count(self, db_session, populate_part_tbl):

    #     assert await part_service.get_part_count(db_session) == 10
