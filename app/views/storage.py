import fastapi
from fastapi import Depends
from fastapi_chameleon import template
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from app.db.session import db_session_context, get_db_session
from app.viewmodels.shared.viewmodel import ViewModelBase
from app.viewmodels.storage.storagelist_viewmodel import StoragelistViewModel

router = fastapi.APIRouter()


@router.get("/storage", include_in_schema=False)
@template()
async def storagelist(
    request: Request, db_session: AsyncSession = Depends(get_db_session)
):
    # Set the injected db_session dependency to the db_session context object
    db_session_context.set(db_session)
    vm = StoragelistViewModel(request)
    vm.load()
    return vm.to_dict()


@router.get("/storage/create", include_in_schema=False)
@template()
def create(request: Request, db_session: AsyncSession = Depends(get_db_session)):
    # Set the injected db_session dependency to the db_session context object
    db_session_context.set(db_session)
    vm = ViewModelBase(request)
    return vm.to_dict()
