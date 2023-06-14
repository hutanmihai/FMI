from typing import List

from pydantic import BaseModel, Field

from app.apis.schemas.base_schema import EntityID


class ProductBase(EntityID):
    name: str = Field(..., max_length=255)
    calories: float
    fat: float
    carbs: float
    protein: float
    upvotes: int
    downvotes: int

    class Config:
        """Map Pydantic model with ORM model"""

        orm_mode = True
        allow_population_by_field_name = True


class ProductsList(BaseModel):
    products: List[ProductBase]


class ProductCreate(BaseModel):
    name: str = Field(..., max_length=255)
    calories: float
    fat: float
    carbs: float
    protein: float

    class Config:
        """Map Pydantic model with ORM model"""

        orm_mode = True
        allow_population_by_field_name = True


class ProductUpdate(BaseModel):
    name: str | None = Field(None, max_length=255)
    calories: float | None
    fat: float | None
    carbs: float | None
    protein: float | None
    upvotes: int | None
    downvotes: int | None

    class Config:
        """Map Pydantic model with ORM model"""

        orm_mode = True
        allow_population_by_field_name = True
