from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.models import Diary, DiaryProduct
from app.repositories.errors import EntityNotFound
from app.repositories.sqlalchemy_repo import SQLAlchemyRepository


class DiaryRepository(SQLAlchemyRepository):
    """Diary repository"""

    async def list_diaries(self, user_id):
        """List diaries"""
        stmt = (
            select(Diary)
            .where(Diary.user_id == user_id)
            .options(joinedload(Diary.diary_products).joinedload(DiaryProduct.product))
        )
        result = await self.db_session.execute(stmt)
        return result.scalars().unique().all()

    async def get(self, user_id, diary_id):
        """Get diary"""
        stmt = (
            select(Diary)
            .where(Diary.id == diary_id and Diary.user_id == user_id)
            .options(joinedload(Diary.diary_products).joinedload(DiaryProduct.product))
        )
        result = await self.db_session.execute(stmt)
        res = result.scalars().unique().one_or_none()
        if not res:
            raise EntityNotFound()
        return res

    async def delete(self, user_id, diary_id):
        """Delete diary"""
        stmt = select(Diary).where(Diary.id == diary_id and Diary.user_id == user_id)
        result = await self.db_session.execute(stmt)
        meal = result.scalars().unique().one_or_none()
        if meal:
            await self.db_session.delete(meal)
            await self.db_session.commit()
        else:
            raise EntityNotFound()
        return meal

    async def update(self, instance):
        """Update diary"""
        self.db_session.add(instance)
        await self.db_session.commit()
        return instance
