import os

import fastapi_chameleon
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from starlette.staticfiles import StaticFiles

from app.api import part_api
from app.core.config import settings
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
    configure(dev_mode=True)


def configure(dev_mode: bool):
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
    app.include_router(part_api.api)

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
