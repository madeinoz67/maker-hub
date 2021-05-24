import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from app.viewmodels.storage.storagelist_viewmodel import StoragelistViewModel
from app.viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get("/storage")
@template()
async def storagelist(request: Request):
    vm = StoragelistViewModel(request)
    vm.load()
    return vm.to_dict()


@router.get("/storage/create")
@template()
def create(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
