import uuid
from typing import List, Tuple

from fastapi import Depends
from sqlalchemy import DATE, FLOAT, Column, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship

from app.database import async_session
from app.models.base import BaseModel
from app.models.diary_product import DiaryProduct
from app.models.product import Product


class Diary(BaseModel):
    __tablename__ = "diary"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(ForeignKey("user.id"), nullable=False)
    date = Column(DATE(), nullable=False)
    total_calories = Column(
        FLOAT(precision=None, decimal_return_scale=2), nullable=False
    )
    total_fat = Column(FLOAT(precision=None, decimal_return_scale=2), nullable=False)
    total_carbs = Column(FLOAT(precision=None, decimal_return_scale=2), nullable=False)
    total_protein = Column(
        FLOAT(precision=None, decimal_return_scale=2), nullable=False
    )
    diary_products = relationship(
        "DiaryProduct", back_populates="diary", cascade="all, delete"
    )

    __table_args__ = (
        UniqueConstraint("user_id", "date", name="unique_user_date_diary"),
    )

    def __init__(self, date: str, user_id: UUID, products: List[Tuple[Product, float]]):
        self.date = date
        self.user_id = user_id
        self.diary_products = []
        self.total_calories = 0
        self.total_protein = 0
        self.total_fat = 0
        self.total_carbs = 0

        for product, quantity_grams in products:
            diary_product = DiaryProduct(
                diary=self, product=product, quantity_grams=quantity_grams
            )
            self.diary_products.append(diary_product)
            self.total_calories += diary_product.calories
            self.total_protein += diary_product.protein
            self.total_fat += diary_product.fat
            self.total_carbs += diary_product.carbs

        self.total_calories = round(self.total_calories, 2)
        self.total_protein = round(self.total_protein, 2)
        self.total_fat = round(self.total_fat, 2)
        self.total_carbs = round(self.total_carbs, 2)

    def add_diary_product(self, product: Product, quantity_grams: float):
        diary_product = DiaryProduct(
            diary=self, product=product, quantity_grams=quantity_grams
        )
        self.total_calories += diary_product.calories
        self.total_protein += diary_product.protein
        self.total_fat += diary_product.fat
        self.total_carbs += diary_product.carbs

        self.total_calories = round(self.total_calories, 2)
        self.total_protein = round(self.total_protein, 2)
        self.total_fat = round(self.total_fat, 2)
        self.total_carbs = round(self.total_carbs, 2)

    async def delete_diary_product(self, product: Product, session):
        for diary_product in self.diary_products:
            if diary_product.product_id == product.id:
                self.total_calories -= diary_product.calories
                self.total_protein -= diary_product.protein
                self.total_fat -= diary_product.fat
                self.total_carbs -= diary_product.carbs

                self.diary_products.remove(diary_product)

                self.total_calories = round(self.total_calories, 2)
                self.total_protein = round(self.total_protein, 2)
                self.total_fat = round(self.total_fat, 2)
                self.total_carbs = round(self.total_carbs, 2)

                await session.delete(diary_product)

                break

    def update_diary_product(self, product: Product, quantity_grams: float):
        for diary_product in self.diary_products:
            if diary_product.product_id == product.id:
                self.total_calories -= diary_product.calories
                self.total_protein -= diary_product.protein
                self.total_fat -= diary_product.fat
                self.total_carbs -= diary_product.carbs

                diary_product.quantity_grams = quantity_grams

                self.total_calories += diary_product.calories
                self.total_protein += diary_product.protein
                self.total_fat += diary_product.fat
                self.total_carbs += diary_product.carbs

                self.total_calories = round(self.total_calories, 2)
                self.total_protein = round(self.total_protein, 2)
                self.total_fat = round(self.total_fat, 2)
                self.total_carbs = round(self.total_carbs, 2)
                break
