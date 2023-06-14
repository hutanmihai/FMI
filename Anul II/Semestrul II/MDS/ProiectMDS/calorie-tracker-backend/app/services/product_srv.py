from typing import List
from uuid import UUID, uuid4

from fastapi import Depends

from app.models import Product
from app.repositories.errors import EntityNotFound
from app.repositories.product_repo import ProductRepository
from app.services.abstract_srv import AbstractService
from app.services.errors import ProductNotFound


class ProductSrv(AbstractService):
    def __init__(self, repo: ProductRepository = Depends(ProductRepository)):
        super().__init__(repo)

    # Get product by id
    async def get_product(self, product_id: UUID) -> Product:
        try:
            return await self._repository.get(Product, product_id)
        except EntityNotFound:
            raise ProductNotFound()

    # Create new product in the database
    async def new_product(
        self, name: str, calories: float, protein: float, fat: float, carbs: float
    ) -> Product:
        instance = Product(
            id=uuid4(),
            name=name,
            calories=calories,
            protein=protein,
            fat=fat,
            carbs=carbs,
            upvotes=0,
            downvotes=0,
        )
        return await self._repository.create(instance)

    # List all products
    async def list_products(self) -> List[Product]:
        return await self._repository.list(Product)

    # Update product
    async def update_product(
        self,
        product_id: UUID,
        name: str | None,
        calories: float | None,
        protein: float | None,
        fat: float | None,
        carbs: float | None,
        upvotes: int | None,
        downvotes: int | None,
    ) -> Product:
        try:
            instance = await self.get_product(product_id)
        except EntityNotFound:
            raise ProductNotFound()

        instance.name = name or instance.name
        instance.calories = calories or instance.calories
        instance.protein = protein or instance.protein
        instance.fat = fat or instance.fat
        instance.carbs = carbs or instance.carbs
        instance.upvotes = upvotes or instance.upvotes
        instance.downvotes = downvotes or instance.downvotes
        return await self._repository.update(instance)

    # Delete product
    async def delete_product(self, product_id: UUID) -> None:
        try:
            instance = await self.get_product(product_id)
        except EntityNotFound:
            raise ProductNotFound()
        return await self._repository.delete(instance)

    async def search_product(self, product_string):
        return await self._repository.search_product(product_string)
