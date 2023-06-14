from datetime import date
from typing import List

from pydantic import UUID4, BaseModel, Field, validator

from app.apis.schemas.base_schema import EntityID
from app.apis.schemas.product_schema import ProductBase


def validate_date(date_str: str) -> date:
    try:
        return date.fromisoformat(date_str)
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")


class ProductDiaryBase(ProductBase):
    quantity_grams: float = Field(..., gt=0)


class ProductDiary(BaseModel):
    product_id: UUID4
    quantity_grams: float = Field(..., gt=0)


class ProductDiaryUpdate(BaseModel):
    product_id: UUID4
    quantity_grams: float | None = Field(None, gt=0)


class DiaryBase(EntityID):
    date: date
    total_calories: float
    total_fat: float
    total_carbs: float
    total_protein: float
    products: List[ProductDiaryBase]


class DiaryCreate(BaseModel):
    date: date
    products: List[ProductDiary] | None

    _validate_date = validator("date", allow_reuse=True, pre=True)(validate_date)


class DiaryUpdate(BaseModel):
    product: ProductDiaryUpdate
