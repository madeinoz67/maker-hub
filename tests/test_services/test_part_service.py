# import asyncio
# import os
# from unittest import mock

import pytest
from loguru import logger  # noqa:
from sqlalchemy.ext.asyncio import AsyncSession  # noqa:

from app.models.part import PartModel
from app.services import part_service


@pytest.mark.asyncio
async def test_add_art(
    part_create_schema_factory,
    db_session,
):

    obj_in = part_create_schema_factory

    item: PartModel = await part_service.create_part(db_session, obj_in)  # noqa:

    assert item.name == obj_in.name
