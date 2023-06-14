from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm.session import sessionmaker

from app.settings import settings

async_engine = create_async_engine(settings.sqlalchemy_database_url, echo=True)
async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        async with session.begin():
            yield session
