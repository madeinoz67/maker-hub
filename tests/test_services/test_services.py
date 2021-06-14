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
