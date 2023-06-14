from typing import List
from uuid import UUID

from asyncpg import ForeignKeyViolationError, UniqueViolationError
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.base import BaseModel
from app.repositories.abstract_repo import AbstractRepository
from app.repositories.errors import EntityNotFound, EntityNotUnique


class SQLAlchemyRepository(AbstractRepository):
    db_session: AsyncSession

    def __init__(self, db_session: AsyncSession = Depends(get_session)):
        self.db_session = db_session

    async def create(self, instance: BaseModel) -> BaseModel:
        try:
            self.db_session.add(instance)
            await self.db_session.commit()
        except IntegrityError as e:
            await self.db_session.rollback()
            self._handle_sqlalchemy_error(e)
        return instance

    async def get(self, model_cls: BaseModel, entity_id: UUID) -> BaseModel:
        instance = await self.db_session.get(entity=model_cls, ident=entity_id)
        if not instance:
            raise EntityNotFound()
        return instance

    async def update(self, instance: BaseModel) -> BaseModel:
        try:
            self.db_session.add(instance)
            await self.db_session.commit()
        except IntegrityError as e:
            await self.db_session.rollback()
            self._handle_sqlalchemy_error(e)
        return instance

    async def list(self, model_cls: BaseModel) -> List[BaseModel]:
        return await self.db_session.scalars(select(model_cls).limit(100))

    async def delete(self, instance: BaseModel) -> None:
        await self.db_session.delete(instance)
        await self.db_session.commit()

    @staticmethod
    def _handle_sqlalchemy_error(err: Exception) -> None:
        if isinstance(err, IntegrityError):
            if isinstance(err.orig.__cause__, ForeignKeyViolationError):
                raise EntityNotFound()
            elif isinstance(err.orig.__cause__, UniqueViolationError):
                raise EntityNotUnique()

    async def ping(self) -> bool:
        if await self.db_session.scalar(select(1)) == 1:
            return True
        return False
