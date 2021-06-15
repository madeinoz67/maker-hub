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

import os
from pathlib import Path

import fastapi_chameleon
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from starlette.staticfiles import StaticFiles

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.db import session
from app.views import home, parts, projects, reports, storage


def get_application() -> FastAPI:
    """Return a new application that will be used to instantiate the application .

    Returns:
        FastAPI: FastAPI Application
    """
    return FastAPI(
        title="Maker Hub",
        description="Open Source Personal Hub for Makers: Manage Parts, \
        projects, ideas, documentation, parts and footprints etc",
        debug=settings.DEBUG,
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
    )


app = get_application()


def main():
    """The Main function for running the dev server ."""
    configure(dev_mode=True)


def configure(dev_mode: bool):
    """Configure the application and configure the FastAPI application.

    Args:
        dev_mode (bool): Enables FastAPI development mode

    """
    configure_middleware()
    configure_templates(dev_mode)
    configure_routes()
    configure_db(dev_mode)


def configure_middleware() -> None:
    """Configure the middleware to use for the application ."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def configure_db(dev_mode: bool) -> None:
    """Configure the DB.

    Args:
        dev_mode (bool): Enables FastAPI development mode

    """
    # TODO filepath = utils.get_database_path(config.get_settings().DATABASE_URL)
    file = (Path(__file__).parent / "dbdata" / "maker-hub.db").absolute()
    session.global_init(file.as_posix())


def configure_templates(dev_mode: bool) -> None:
    """Configure the templates for the application.

    Args:
        dev_mode (bool): Enables FastAPI development mode
    """
    folder = os.path.dirname(__file__)
    template_folder = os.path.join(folder, "templates")
    template_folder = os.path.abspath(template_folder)
    fastapi_chameleon.global_init(template_folder, auto_reload=dev_mode)


def configure_routes() -> None:
    """Configure routes to the application."""
    folder = os.path.dirname(__file__)
    static_folder = os.path.join(folder, "static")
    static_folder = os.path.abspath(static_folder)
    app.mount("/static", StaticFiles(directory=static_folder), name="static")

    # API endpoints
    app.include_router(api_router, prefix=settings.API_V1_STR)

    # Webpages
    app.include_router(home.router)
    app.include_router(parts.router)
    app.include_router(projects.router)
    app.include_router(reports.router)
    app.include_router(storage.router)


if __name__ == "__main__":
    main()
else:

    DEV_MODE = settings.DEV_MODE
    configure(dev_mode=DEV_MODE)
    logger.info(f"Dev Mode is: {DEV_MODE}")
