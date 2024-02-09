from pprint import pprint

from apis.health import router as health_router
from apis.image_editing import router as image_editing_router
from fastapi import FastAPI
from settings import settings
from starlette.middleware.cors import CORSMiddleware
from uvicorn import run as uvicorn_run


def register_api_routers(app: FastAPI) -> FastAPI:
    """Register API handlers."""
    app.include_router(health_router)
    app.include_router(image_editing_router)
    return app


def add_middleware(app: FastAPI) -> FastAPI:
    """Add middleware to FastAPI application."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


def create_app() -> FastAPI:
    """Create FastAPI application."""
    app = FastAPI(
        title=settings.APP_NAME,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSION,
    )
    app = register_api_routers(app)
    app = add_middleware(app)
    return app


app: FastAPI = create_app()

if __name__ == "__main__":
    """Run FastAPI application."""
    pprint(f"Open SWAGGER at http://{settings.APP_HOST}:{settings.APP_PORT}/docs")
    uvicorn_run(app, host=settings.APP_HOST, port=settings.APP_PORT)
