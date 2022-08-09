import fastapi

from app.models.datatable import DataTableRequest
from app.models.part import PartTableResponse
from app.services import part_service

router = fastapi.APIRouter()


@router.post("/api/part/datatable")
async def table_datasource(request: DataTableRequest) -> PartTableResponse:
    """Parts Datatable Source

    Returns:
        [TableResponse]: [DataTable Ajax Response]
    """

    draw = request.draw

    data = await part_service.get_latest_parts(
        start=request.start, limit=request.length
    )
    return PartTableResponse(
        draw=draw, recordsTotal=100, recordsFiltered=100, data=data
    )
