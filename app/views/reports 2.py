import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from app.viewmodels.reports.overview_viewmodel import OverviewViewModel
from app.viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get("/reports")
@template()
def overview(request: Request):
    vm = OverviewViewModel(request)
    return vm.to_dict()
