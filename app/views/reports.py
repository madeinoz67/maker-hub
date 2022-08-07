import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from app.viewmodels.reports.overview_viewmodel import OverviewViewModel

router = fastapi.APIRouter()


@router.get("/reports", include_in_schema=False)
@template()
async def overview(request: Request):
    vm = OverviewViewModel(request)
    await vm.load()
    return vm.to_dict()
