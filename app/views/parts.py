import fastapi
from fastapi import Depends
from fastapi_chameleon import template
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from app.db.session import db_session_context, get_db_session
from app.viewmodels.parts.partslist_viewmodel import PartslistViewModel
from app.viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get("/parts", include_in_schema=False)
@template()
async def partslist(
    request: Request, db_session: AsyncSession = Depends(get_db_session)
):
    # Set the injected db_session dependency to the db_session context object
    db_session_context.set(db_session)
    vm = PartslistViewModel(request)
    await vm.load()
    return vm.to_dict()


@router.get("/parts/create", include_in_schema=False)
@template()
def create(request: Request, db_session: AsyncSession = Depends(get_db_session)):
    # Set the injected db_session dependency to the db_session context object
    db_session_context.set(db_session)
    vm = ViewModelBase(request)
    return vm.to_dict()
