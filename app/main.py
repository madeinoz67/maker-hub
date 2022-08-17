import os

import fastapi_chameleon
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from starlette.staticfiles import StaticFiles

from app.api.v1.api import api_v1_router
from app.core.config import settings
from app.db.db_config import db
from app.views import home, parts, projects, reports, storage


def get_application() -> FastAPI:
    """Return a new application that will be used to instantiate the application .
    Returns:
        FastAPI: FastAPI Application
    """

    app_settings = settings.fastapi_settings.dict()
    app = FastAPI(**app_settings)
    app.add_event_handler("startup", db.initialize_db)
    logger.info(f"FastAPI Settings: {app_settings}")
    return app


app = get_application()


def main():
    configure(dev_mode=True)


def configure(dev_mode: bool):
    configure_middleware()
    configure_templates(dev_mode)
    configure_routes()


def configure_middleware() -> None:
    """Configure the middleware to use for the application ."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


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
    folder = os.path.dirname(__file__)
    static_folder = os.path.join(folder, "static")
    static_folder = os.path.abspath(static_folder)
    app.mount("/static", StaticFiles(directory=static_folder), name="static")

    # API endpoints
    app.include_router(api_v1_router, prefix=settings.API_V1_STR)

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
    configure(DEV_MODE)
    logger.info(f"Development Mode is: {DEV_MODE}")
