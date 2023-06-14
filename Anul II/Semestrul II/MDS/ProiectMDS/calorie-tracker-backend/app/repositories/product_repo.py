from sqlalchemy import select

from app.models import Product
from app.repositories.sqlalchemy_repo import SQLAlchemyRepository


class ProductRepository(SQLAlchemyRepository):
    """Product repository"""

    async def search_product(self, product_string):
        products = await self.db_session.execute(
            select(Product).where(Product.name.like(f"%{product_string}%"))
        )
        return products.scalars().all()
