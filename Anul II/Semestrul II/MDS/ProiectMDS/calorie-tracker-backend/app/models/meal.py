import uuid
from typing import List, Tuple

from sqlalchemy import FLOAT, VARCHAR, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.base import BaseModel
from app.models.meal_product import MealProduct
from app.models.product import Product


class Meal(BaseModel):
    __tablename__ = "meal"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(VARCHAR(255), nullable=False)
    user_id = Column(ForeignKey("user.id"), nullable=False)
    total_calories = Column(
        FLOAT(precision=None, decimal_return_scale=2), nullable=False
    )
    total_fat = Column(FLOAT(precision=None, decimal_return_scale=2), nullable=False)
    total_carbs = Column(FLOAT(precision=None, decimal_return_scale=2), nullable=False)
    total_protein = Column(
        FLOAT(precision=None, decimal_return_scale=2), nullable=False
    )
    meal_products = relationship(
        "MealProduct", back_populates="meal", cascade="all, delete"
    )

    def __init__(self, name: str, user_id: UUID, products: List[Tuple[Product, float]]):
        self.name = name
        self.user_id = user_id
        self.meal_products = []
        self.total_calories = 0
        self.total_protein = 0
        self.total_fat = 0
        self.total_carbs = 0

        for product, quantity_grams in products:
            meal_product = MealProduct(
                meal=self, product=product, quantity_grams=quantity_grams
            )
            self.meal_products.append(meal_product)
            self.total_calories += meal_product.calories
            self.total_protein += meal_product.protein
            self.total_fat += meal_product.fat
            self.total_carbs += meal_product.carbs

        self.total_calories = round(self.total_calories, 2)
        self.total_protein = round(self.total_protein, 2)
        self.total_fat = round(self.total_fat, 2)
        self.total_carbs = round(self.total_carbs, 2)

    def add_meal_product(self, product: Product, quantity_grams: float):
        meal_product = MealProduct(
            meal=self, product=product, quantity_grams=quantity_grams
        )
        self.total_calories += meal_product.calories
        self.total_protein += meal_product.protein
        self.total_fat += meal_product.fat
        self.total_carbs += meal_product.carbs

        self.total_calories = round(self.total_calories, 2)
        self.total_protein = round(self.total_protein, 2)
        self.total_fat = round(self.total_fat, 2)
        self.total_carbs = round(self.total_carbs, 2)

    async def delete_meal_product(self, product: Product, session):
        for meal_product in self.meal_products:
            if meal_product.product_id == product.id:
                self.total_calories -= meal_product.calories
                self.total_protein -= meal_product.protein
                self.total_fat -= meal_product.fat
                self.total_carbs -= meal_product.carbs

                self.meal_products.remove(meal_product)

                self.total_calories = round(self.total_calories, 2)
                self.total_protein = round(self.total_protein, 2)
                self.total_fat = round(self.total_fat, 2)
                self.total_carbs = round(self.total_carbs, 2)

                await session.delete(meal_product)

                break

    def update_meal_product(self, product: Product, quantity_grams: float):
        for meal_product in self.meal_products:
            if meal_product.product_id == product.id:
                self.total_calories -= meal_product.calories
                self.total_protein -= meal_product.protein
                self.total_fat -= meal_product.fat
                self.total_carbs -= meal_product.carbs

                meal_product.quantity_grams = quantity_grams

                self.total_calories += meal_product.calories
                self.total_protein += meal_product.protein
                self.total_fat += meal_product.fat
                self.total_carbs += meal_product.carbs

                self.total_calories = round(self.total_calories, 2)
                self.total_protein = round(self.total_protein, 2)
                self.total_fat = round(self.total_fat, 2)
                self.total_carbs = round(self.total_carbs, 2)
                break
