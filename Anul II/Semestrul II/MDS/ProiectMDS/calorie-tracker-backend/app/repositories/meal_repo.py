from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.models import Meal, MealProduct
from app.repositories.errors import EntityNotFound
from app.repositories.sqlalchemy_repo import SQLAlchemyRepository


class MealRepository(SQLAlchemyRepository):
    """Meal repository"""

    async def list_meals(self, user_id):
        """List meals"""
        stmt = (
            select(Meal)
            .where(Meal.user_id == user_id)
            .options(joinedload(Meal.meal_products).joinedload(MealProduct.product))
        )
        result = await self.db_session.execute(stmt)
        return result.scalars().unique().all()

    async def get(self, user_id, meal_id):
        """Get meal"""
        stmt = (
            select(Meal)
            .where(Meal.id == meal_id and Meal.user_id == user_id)
            .options(joinedload(Meal.meal_products).joinedload(MealProduct.product))
        )
        result = await self.db_session.execute(stmt)
        res = result.scalars().unique().one_or_none()
        if not res:
            raise EntityNotFound()
        return res

    async def delete(self, user_id, meal_id):
        """Delete meal"""
        stmt = select(Meal).where(Meal.id == meal_id and Meal.user_id == user_id)
        result = await self.db_session.execute(stmt)
        meal = result.scalars().unique().one_or_none()
        if meal:
            await self.db_session.delete(meal)
            await self.db_session.commit()
        else:
            raise EntityNotFound()
        return meal

    async def update(self, instance):
        """Update meal"""
        self.db_session.add(instance)
        await self.db_session.commit()
        return instance
