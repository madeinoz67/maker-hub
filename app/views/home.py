import fastapi
from fastapi import Depends
from fastapi_chameleon import template
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from app.db.session import db_session_context, get_db_session
from app.viewmodels.home.index_viewmodel import IndexViewModel
from app.viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get("/", include_in_schema=False)
@template()
async def index(request: Request, db: AsyncSession = Depends(get_db_session)):
    # Set the injected db_session dependency to the db_session context object
    db_session_context.set(db)
    vm = IndexViewModel(request, db)
    await vm.load()
    return vm.to_dict()


@router.get("/about", include_in_schema=False)
@template()
def about(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()


@router.get("/help", include_in_schema=False)
@template()
def help(request: Request):
    vm = ViewModelBase(request)
    return vm.to_dict()
