import abc
from typing import List
from uuid import UUID

from app.models.base import BaseModel


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    async def create(self, instance: BaseModel) -> BaseModel:
        raise NotImplementedError

    @abc.abstractmethod
    async def get(self, model_cls: BaseModel, entity_id: UUID) -> BaseModel:
        raise NotImplementedError

    @abc.abstractmethod
    async def update(self, instance: BaseModel) -> BaseModel:
        raise NotImplementedError

    @abc.abstractmethod
    async def list(self, model_cls: BaseModel) -> List[BaseModel]:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, instance: BaseModel) -> None:
        raise NotImplementedError
