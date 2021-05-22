import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from app.viewmodels.home.index_viewmodel import IndexViewModel
from app.viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get("/")
@template()
def index(request: Request):
    vm = IndexViewModel(request)
    return vm.to_dict()


@router.get("/about")
@template()
def about(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()


@router.get("/help")
@template()
def help(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
