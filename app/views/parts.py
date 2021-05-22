import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from app.viewmodels.parts.partslist_viewmodel import PartslistViewModel
from app.viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get("/parts")
@template()
def partslist(request: Request):
    vm = PartslistViewModel(request)
    return vm.to_dict()


@router.get("/parts/create")
@template()
def create(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
