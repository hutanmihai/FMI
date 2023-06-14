from typing import List, Tuple
from uuid import UUID, uuid4

from fastapi import Depends

from app.models import MealProduct, Product
from app.models.meal import Meal
from app.repositories.errors import EntityNotFound
from app.repositories.meal_repo import MealRepository
from app.services.abstract_srv import AbstractService
from app.services.errors import MealNotFound


class MealSrv(AbstractService):
    _repository: MealRepository

    def __init__(self, repo: MealRepository = Depends(MealRepository)):
        super().__init__(repo)

    async def new_meal(
        self, user_id: UUID, name: str, products: List[Tuple[Product, float]]
    ):
        instance = Meal(name=name, user_id=user_id, products=products)
        return await self._repository.create(instance)

    async def list_meals(self, user_id):
        return await self._repository.list_meals(user_id)

    async def get_meal(self, user_id: UUID, meal_id: UUID):
        try:
            return await self._repository.get(user_id, meal_id)
        except EntityNotFound:
            raise MealNotFound()

    async def delete_meal(self, user_id, meal_id: UUID):
        try:
            await self.get_meal(user_id, meal_id)
        except EntityNotFound:
            raise MealNotFound()
        return await self._repository.delete(user_id, meal_id)

    async def update_meal(
        self, user_id, meal_id, name, product_id, quantity_grams, product
    ):
        try:
            instance: Meal = await self.get_meal(user_id, meal_id)
        except EntityNotFound:
            raise MealNotFound()
        if name:
            instance.name = name
        # If quantity_grams is None it means we want to delete the product from the meal
        if product_id and not quantity_grams:
            await instance.delete_meal_product(product, self._repository.db_session)

        # If the product is already in the meal, update the quantity
        elif product in [
            meal_product.product for meal_product in instance.meal_products
        ]:
            instance.update_meal_product(product, quantity_grams)

        # If the product is not in the meal, add it
        else:
            instance.add_meal_product(product, quantity_grams)

        return await self._repository.update(instance)
