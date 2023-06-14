from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run as uvicorn_run

from app.apis.diary_api import router as diary_router
from app.apis.health_api import router as health_router
from app.apis.login import router as login_router
from app.apis.meal_api import router as meal_router
from app.apis.product_api import router as product_router
from app.apis.user_api import router as user_router
from app.scripts.create_admin import insert_admin
from app.settings import settings


def _register_api_handlers(app: FastAPI) -> FastAPI:
    """Register API handlers."""
    app.include_router(health_router)
    app.include_router(login_router)
    app.include_router(product_router)
    app.include_router(user_router)
    app.include_router(meal_router)
    app.include_router(diary_router)
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
    """Create and return FastAPI application."""
    app = FastAPI()
    app = _register_api_handlers(app)
    app = add_middleware(app)
    return app


app: FastAPI = create_app()


@app.on_event("startup")
async def startup_event():
    """Insert admin on startup."""
    await insert_admin()


async def run_app(app: FastAPI = app) -> None:
    """Run FastAPI application."""
    uvicorn_run(app, host=settings.app_host, port=int(settings.app_port))
