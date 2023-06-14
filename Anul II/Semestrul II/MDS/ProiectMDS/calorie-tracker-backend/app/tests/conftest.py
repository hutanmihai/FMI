import asyncio
from typing import AsyncGenerator

import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app import models
from app.app import app
from app.database import async_engine, async_session
from app.scripts.create_admin import insert_admin


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session", autouse=True)
async def db_tables() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(models.BaseModel.metadata.drop_all)
        await conn.run_sync(models.BaseModel.metadata.create_all)


@pytest_asyncio.fixture(scope="session", autouse=True)
async def insert_admin_data() -> None:
    await insert_admin()


@pytest_asyncio.fixture
async def session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as sess:
        yield sess


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        yield client
