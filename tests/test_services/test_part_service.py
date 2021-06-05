# import asyncio
# import os
# from unittest import mock

import pytest
from sqlalchemy.ext.asyncio import AsyncSession  # noqa:

from app.models.part import PartModel
from app.schema.part import PartCreateSchema
from app.services import part_service


@pytest.mark.asyncio
async def test_part_get(
    db_session,
):
    obj_in = PartCreateSchema(name="testpart")

    item: PartModel = await part_service.create_part(obj_in)  # noqa:

    # assert item == item2
    pass
