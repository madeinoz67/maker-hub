import fastapi
from fastapi import Depends
from fastapi_chameleon import template
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from app.db.session import db_session_context, get_db_session
from app.viewmodels.reports.overview_viewmodel import OverviewViewModel

router = fastapi.APIRouter()


@router.get("/reports", include_in_schema=False)
@template()
async def overview(
    request: Request, db_session: AsyncSession = Depends(get_db_session)
):
    # Set the injected db_session dependency to the db_session context object
    db_session_context.set(db_session)
    vm = OverviewViewModel(request)
    await vm.load()
    return vm.to_dict()
