import pytest

from app.services import part_service, project_service, storage_service


@pytest.mark.asyncio
class TestPartservice:
    """Test part service"""

    async def test_get_part_count(self):
        assert await part_service.get_part_count() == 283

    async def test_get_total_stock(self):
        assert await part_service.get_total_stock() == 1000

    async def test_get_stock_value(self):
        assert await part_service.get_stock_value() == 1_500

    async def test_get_latest_parts_returns_a_list(self):
        assert type(await part_service.get_latest_parts()) == list

    async def test_get_latest_parts_limits(self):
        result = len(await part_service.get_latest_parts())
        assert result == 5

        result = len(await part_service.get_latest_parts(limit=10))
        assert result == 10

        result = len(await part_service.get_latest_parts(start=5, limit=10))
        assert result == 10


@pytest.mark.asyncio
class TestProjectservice:
    """Test project service"""

    async def test_get_project_count(self):
        assert await project_service.get_project_count() == 34

    async def test_get_latest_projects_returns_a_list(self):
        assert type(await project_service.get_latest_projects()) == list

    async def test_get_latest_parts_limits(self):
        result = len(await project_service.get_latest_projects())
        assert result == 5

        result = len(await project_service.get_latest_projects(limit=10))
        assert result == 10

        result = len(await project_service.get_latest_projects(start=5, limit=10))
        assert result == 5

        result = len(await project_service.get_latest_projects(start=-1))
        assert result == 5

        result = len(await project_service.get_latest_projects(limit=-1))
        assert result == 0

        result = len(await project_service.get_latest_projects(limit=0))
        assert result == 0


@pytest.mark.asyncio
class TestStorageservice:
    async def test_get_location_count(self):
        assert await storage_service.get_location_count() == 234

    async def test_get_locations_used(self):
        assert await storage_service.get_locations_used() == 230
