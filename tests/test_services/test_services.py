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

        obj_in = part_create_schema_factory

        item: PartModel = await part_service.create_part(db_session, obj_in)  # noqa:

        assert item.name == obj_in.name
        assert item.id is not None
        assert len(item.id) == 26

    @pytest.mark.asyncio
    async def test_part_count(self, db_session, part_create_schema_factory):

        assert await part_service.get_part_count(db_session) == 0

        await part_service.create_part(db_session, part_create_schema_factory)

        assert await part_service.get_part_count(db_session) == 1
