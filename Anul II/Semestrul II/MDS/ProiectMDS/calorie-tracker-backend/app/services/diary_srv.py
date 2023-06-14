from typing import List, Tuple
from uuid import UUID, uuid4

from fastapi import Depends

from app.models import Diary, DiaryProduct, Product
from app.repositories.diary_repo import DiaryRepository
from app.repositories.errors import EntityNotFound, EntityNotUnique
from app.services.abstract_srv import AbstractService
from app.services.errors import DiaryAlreadyExists, DiaryNotFound


class DiarySrv(AbstractService):
    _repository: DiaryRepository

    def __init__(self, repo: DiaryRepository = Depends(DiaryRepository)):
        super().__init__(repo)

    async def new_diary(
        self, user_id: UUID, date: str, products: List[Tuple[Product, float]]
    ):
        instance = Diary(date=date, user_id=user_id, products=products)
        try:
            return await self._repository.create(instance)
        except EntityNotUnique:
            raise DiaryAlreadyExists()

    async def list_diaries(self, user_id):
        return await self._repository.list_diaries(user_id)

    async def get_diary(self, user_id: UUID, diary_id: UUID):
        try:
            return await self._repository.get(user_id, diary_id)
        except EntityNotFound:
            raise DiaryNotFound()

    async def delete_diary(self, user_id, diary_id: UUID):
        try:
            await self.get_diary(user_id, diary_id)
        except EntityNotFound:
            raise DiaryNotFound()
        return await self._repository.delete(user_id, diary_id)

    async def update_diary(
        self, user_id, diary_id, product_id, quantity_grams, product
    ):
        try:
            instance: Diary = await self.get_diary(user_id, diary_id)
        except EntityNotFound:
            raise DiaryNotFound()

        # If quantity_grams is None it means we want to delete the product from the diary
        if product_id and not quantity_grams:
            await instance.delete_diary_product(product, self._repository.db_session)

        # If the product is already in the diary, update the quantity
        elif product in [
            diary_product.product for diary_product in instance.diary_products
        ]:
            instance.update_diary_product(product, quantity_grams)

        # If the product is not in the diary, add it
        else:
            instance.add_diary_product(product, quantity_grams)

        return await self._repository.update(instance)
