import fastapi

from app.schema.datatable import DataTableRequest, PartDataTableResponse
from app.services import part_service

from app.schema.part import Part
from typing import Optional

api = fastapi.APIRouter()


@api.post("/api/part/datatable", response_model=PartDataTableResponse)
async def table_datasource(request: DataTableRequest) -> PartDataTableResponse:
    """Servers side processing for Parts List Datatable

    This performs the server-side processing for the Part List Datatable

    """

    draw = request.draw

    data = await part_service.get_part_datatable(request)
    return PartDataTableResponse(
        draw=draw, recordsTotal=100, recordsFiltered=100, data=data
    )


@api.post("/api/part/create", response_model=Part)
async def create_part(
    name: str,
    description: str,
    notes: Optional[str] = None,
    footprint: Optional[str] = None,
    manufacturer: Optional[str] = None,
    mpn: Optional[str] = None,
) -> Part:
    """Creates a new part

    This will create a new part and assign it a unique string Id.
    """

    part = await part_service.create_part(
        name=name,
        description=description,
        notes=notes,
        footprint=footprint,
        manufacturer=manufacturer,
        mpn=mpn,
    )
    return part
