#
# Copyright 2021 Stephen Eaton
#
# This file is part of Maker-Hub.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


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
) -> dict:
    """Storage List page route.

    Args:
        request (Request): Incoming web request.
        db_session (AsyncSession, optional): DB dependency injection. Defaults to Depends(get_db_session).

    Returns:
        dict: [description]
    """
    # Set the injected db_session dependency to the db_session context object
    db_session_context.set(db_session)
    vm = StoragelistViewModel(request)
    await vm.load()
    return vm.to_dict()


@router.get("/storage/create", include_in_schema=False)
@template()
def create(
    request: Request, db_session: AsyncSession = Depends(get_db_session)
) -> dict:
    """Storage create Page Route .

    Args:
        request (Request): Incoming Web Request
        db_session (AsyncSession, optional): DB Dependency injection. Defaults to Depends(get_db_session).

    Returns:
        [dict]: [description]
    """
    # Set the injected db_session dependency to the db_session context object
    db_session_context.set(db_session)
    vm = ViewModelBase(request)
    return vm.to_dict()
