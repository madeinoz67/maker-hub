import fastapi

from app.schema.datatable import DataTableRequest, DataTableResponse
from app.services import part_service

api = fastapi.APIRouter()


@api.post("/api/part/datatable", response_model=DataTableResponse)
async def table_datasource(request: DataTableRequest) -> DataTableResponse:
    """Parts Datatable Source

    Returns:
        [TableResponse]: [DataTable Ajax Response]
    """

    draw = request.draw

    data = await part_service.get_latest_parts(
        start=request.start, limit=request.length
    )
    return DataTableResponse(
        draw=draw, recordsTotal=100, recordsFiltered=100, data=data
    )
