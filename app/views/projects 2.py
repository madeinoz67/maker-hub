import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from app.viewmodels.projects.projectslist_viewmodel import ProjectlistViewModel
from app.viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get("/projects")
@template()
def projectlist(request: Request):
    vm = ProjectlistViewModel(request)
    return vm.to_dict()


@router.get("/projects/create")
@template()
def create(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
