from typing import List

from sqlalchemy import select

from app.database import async_session
from app.models import Product, User


async def get_all_products() -> List[Product]:
    async with async_session() as session:
        return (await session.scalars(select(Product))).all()


async def get_all_users() -> List[User]:
    async with async_session() as session:
        return (await session.scalars(select(User))).all()
