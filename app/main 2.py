import os
import fastapi
import fastapi_chameleon
import uvicorn
from starlette.staticfiles import StaticFiles
from dotenv import load_dotenv

from app.views import home
from app.views import parts
from app.views import projects
from app.views import storage
from app.views import reports


app = fastapi.FastAPI()


def main():
    configure(dev_mode=True)


def configure(dev_mode: bool):
    configure_templates(dev_mode)
    configure_routes()


def configure_templates(dev_mode: bool):

    folder = os.path.dirname(__file__)
    template_folder = os.path.join(folder, "templates")
    template_folder = os.path.abspath(template_folder)
    fastapi_chameleon.global_init(template_folder, auto_reload=dev_mode)


def configure_routes():
    folder = os.path.dirname(__file__)
    static_folder = os.path.join(folder, "static")
    static_folder = os.path.abspath(static_folder)
    app.mount("/static", StaticFiles(directory=static_folder), name="static")
    app.include_router(home.router)
    app.include_router(parts.router)
    app.include_router(projects.router)
    app.include_router(reports.router)
    app.include_router(storage.router)


if __name__ == "__main__":
    main()
else:
    load_dotenv()

    DEV_MODE = os.getenv("DEV_MODE", "False") == "True"

    configure(dev_mode=DEV_MODE)
