import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from app.viewmodels.shared.viewmodel import ViewModelBase
from app.viewmodels.storage.storagelist_viewmodel import StoragelistViewModel

router = fastapi.APIRouter()


@router.get("/storage", include_in_schema=False)
@template()
async def storagelist(request: Request):
    vm = StoragelistViewModel(request)
    vm.load()
    return vm.to_dict()


@router.get("/storage/create", include_in_schema=False)
@template()
def create(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
