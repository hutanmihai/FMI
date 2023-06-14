from fastapi import Depends

from app.repositories.sqlalchemy_repo import SQLAlchemyRepository
from app.services.abstract_srv import AbstractService


class HealthSrv(AbstractService):
    _repository: SQLAlchemyRepository

    def __init__(self, repo: SQLAlchemyRepository = Depends(SQLAlchemyRepository)):
        super().__init__(repo)

    async def is_healthy(self) -> bool:
        return await self._repository.ping()
