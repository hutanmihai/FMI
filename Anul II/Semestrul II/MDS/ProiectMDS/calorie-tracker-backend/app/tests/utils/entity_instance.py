from app.auth.jwt_handler import token_encode
from app.database import async_session
from app.models import Product, User
from app.tests.utils.data_generation_tools import (
    get_product_instance,
    get_user_instance,
)


async def new_user() -> (User, str):
    async with async_session() as session:
        user: User = get_user_instance()
        session.add(user)
        actual_user = await session.get(User, user.id)
        await session.commit()
        token: str = token_encode(actual_user.id)
        return actual_user, token


async def new_product() -> Product:
    async with async_session() as session:
        product = get_product_instance()
        session.add(product)
        actual_product = await session.get(Product, product.id)
        await session.commit()
        return actual_product
