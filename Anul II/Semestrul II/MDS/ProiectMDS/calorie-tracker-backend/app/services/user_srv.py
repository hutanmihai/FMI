from typing import List
from uuid import UUID

from fastapi import Depends

from app.apis.utils.enums import HeightMetric, WeightMetric
from app.models import User
from app.repositories.errors import EntityNotFound, EntityNotUnique
from app.repositories.user_repo import UserRepository
from app.services.abstract_srv import AbstractService
from app.services.errors import UserAlreadyExists, UserNotFound


class UserSrv(AbstractService):
    def __init__(self, repo: UserRepository = Depends(UserRepository)):
        super().__init__(repo)

    # Get user by id
    async def get_user(self, user_id: UUID) -> User:
        try:
            return await self._repository.get(User, user_id)
        except EntityNotFound:
            raise UserNotFound()

    # Create new user in the database
    async def new_user(self, g_id: str, email: str, name: str, picture: str) -> User:
        instance = User(g_id=g_id, email=email, name=name, picture=picture)
        try:
            return await self._repository.create(instance)
        except EntityNotUnique:
            raise UserAlreadyExists()

    # Get user by email
    async def get_user_by_email(self, email: str) -> User:
        try:
            return await self._repository.get_by_email(email)
        except EntityNotFound:
            raise UserNotFound()

    # Update user
    async def update_user(
        self,
        user_id: UUID,
        name: str | None,
        pref_height_metric: HeightMetric | None,
        height: float | None,
        pref_weight_metric: WeightMetric | None,
        weight: float | None,
        target_weight: float | None,
        target_calories: int | None,
    ) -> User:
        try:
            instance = await self.get_user(user_id)
        except EntityNotFound:
            raise UserNotFound()

        instance.name = name or instance.name
        instance.pref_height_metric = pref_height_metric or instance.pref_height_metric
        instance.height = height or instance.height
        instance.pref_weight_metric = pref_weight_metric or instance.pref_weight_metric
        instance.weight = weight or instance.weight
        instance.target_weight = target_weight or instance.target_weight
        instance.target_calories = target_calories or instance.target_calories

        return await self._repository.update(instance)

    # Get all users
    async def get_all_users(self) -> List[User]:
        return await self._repository.list(User)

    # Delete user
    async def delete_user(self, user_id: UUID) -> None:
        try:
            instance = await self._repository.get(User, user_id)
            await self._repository.delete(instance)
        except EntityNotFound:
            raise UserNotFound()
