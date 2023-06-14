from typing import List

from pydantic import UUID4, BaseModel, Field

from app.apis.schemas.base_schema import EntityID
from app.apis.schemas.product_schema import ProductBase


class ProductMealBase(ProductBase):
    quantity_grams: float = Field(..., gt=0)


class ProductMeal(BaseModel):
    product_id: UUID4
    quantity_grams: float = Field(..., gt=0)


class ProductMealUpdate(BaseModel):
    product_id: UUID4
    quantity_grams: float | None = Field(None, gt=0)


class MealBase(EntityID):
    name: str = Field(..., max_length=255)
    total_calories: float
    total_fat: float
    total_carbs: float
    total_protein: float
    products: List[ProductMealBase]

    class Config:
        """Map Pydantic model with ORM model"""

        orm_mode = True
        allow_population_by_field_name = True


class MealCreate(BaseModel):
    name: str = Field(..., max_length=255)
    products: List[ProductMeal] | None

    class Config:
        """Map Pydantic model with ORM model"""

        orm_mode = True
        allow_population_by_field_name = True


class MealUpdate(BaseModel):
    name: str | None
    product: ProductMealUpdate | None

    class Config:
        """Map Pydantic model with ORM model"""

        orm_mode = True
        allow_population_by_field_name = True
