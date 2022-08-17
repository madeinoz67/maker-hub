from typing import Optional

import fastapi
from fastapi import Depends, Response, status
from loguru import logger

from app.api.exceptions import DuplicatedEntryError, NoResultsFound
from app.core.config import settings
from app.models.datatable import DataTableRequest
from app.models.part import (
    PartCreateModel,
    PartPublicModel,
    PartPublicResponseModel,
    PartTableResponse,
    PartUpdateModel,
)
from app.services import part_service

router = fastapi.APIRouter()


@router.get(
    "/",
    response_model=PartPublicResponseModel,
    status_code=status.HTTP_200_OK,
    name="parts_list",
)
async def parts_list(
    q: Optional[str] = None,
    limit: Optional[int] = 100,
    offset: Optional[int] = 0,
) -> PartPublicResponseModel:
    """# List Parts

    ## Args:
    ### q (string, optional):
    Part query string.

    If not defined then all parts are returned in the PartPublicResponseModel

    Defaults to None

    ### limit (integer, optional):
    Used in conjunction with offset to return a subset of the results.

    Defaults to 100.

    e.g. limit=100,offset=0 will return the results returned from offset 0 to
    offset 100.

    ### offset (integer, optional):
    Used in conjunction with limit to return a subset of the results.

    e.g. offset=100 will return the 101th result onwards.

    Defaults to 0.

    ## Raises:
    ### NoResultsFound:
    No results found.

    ## Returns:
    ### PartPublicResponseModel:
    Response returned
    """

    raise NoResultsFound()


@router.post(
    "/",
    response_model=PartPublicModel,
    status_code=status.HTTP_201_CREATED,
    name="part_create",
)
async def part_create(
    details: PartCreateModel,
    __body: bool = True,
) -> PartPublicModel:
    """# Add a new part.

    At a minimum this will create a new part in the database for the part name
    in the request body and assign it a unique string ID.

    ## Args:
    ### __body (bool, optional):
    - If True then will return a body as part of the response.

    - If False then will not return a body in the response.

    Defaults to True.

    ### details (PartCreateModel):
    The details used to create the new part.

    The part ID in the database will be replaced with this new part.

    - name: (string, required) The name of the part.

    ## Raises:
    - DuplicatedEntryError: If the part already exists.

    ## Returns:
    - PartPublicModel: The newly created part.

    """
    raise NoResultsFound()


@router.delete("/{part_id}", name="part_delete")
async def part_delete(part_id: str) -> Response:
    """# Delete a Part

    ## Args:
    **part_id** (string): ID of part to delete

    ## Raises:
    **NoResultsFound:** If the part does not exist.

    ## Returns:
    **200 Success:** The part has been deleted.
    """
    raise NoResultsFound()


@router.get(
    "/{part_id}",
    response_model=PartPublicModel,
)
async def part_read(
    part_id: str,
) -> PartPublicModel:
    """# Read a part.

    ## Args:
    ### part_id (string, required):
    The ID of the part to read.

    ## Raises:
    ### NoResultsFound:
    No results found.

    ## Returns:
    ### PartPublicModel:
    The part.
    """

    raise NoResultsFound()


@router.put("/{part_id}", response_model=PartPublicModel, name="part_update")
async def part_update(
    part_id: str,
    details: PartUpdateModel,
    __body: bool = True,
) -> PartPublicModel:
    """# Part Update
    Updates all of the parts fields at the same time.
    ## Args:
    ### part_id (string):
    ID of part to update in the database

    ### details (PartUpdateModel):
    New part information to update the current part ID with.

    The part in the database will be updated exactly how this model is completed.

    ### __body (bool, optional):
    - If True then will return a response body as part of the response.

    - If False then will not return a response body as part of the response.

    Defaults to True.

    ## Raises:
    ### NoResultsFound:
    Could not find the part ID in the database

    ## Returns:
    ### PartPublicModel:
    Returns the newly created part in the response body with the updated part information
    """
    raise NoResultsFound()


@router.patch("/{part_id}", response_model=PartPublicModel, name="part_update")
async def part_update(
    part_id: str,
    details: PartUpdateModel,
    __body: bool = True,
) -> PartPublicModel:
    """# Part Update

    Updates specific fields of a part.

    ## Args:
    ### part_id (str):
    ID of part to update in the database

    ### details (PartUpdateModel):
    New part information to update the current part ID with.

    ### __body (bool, optional):
    - If True then will return a response body as part of the response.

    - If False then will not return a response body as part of the response.

    Defaults to True.

    ## Raises:
    ### NoResultsFound:
    Could not find the part ID in the database

    ## Returns:
    ### PartPublicModel:
    Returns the newly created part in the response body with the updated part information
    """
    raise NoResultsFound()


@router.post("/datatable")
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
