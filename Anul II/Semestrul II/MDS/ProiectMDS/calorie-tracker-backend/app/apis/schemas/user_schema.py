from typing import List

from pydantic import BaseModel, Field

from app.apis.schemas.base_schema import EntityID
from app.apis.utils.enums import HeightMetric, WeightMetric


class UserBase(EntityID):
    g_id: str = Field(..., max_length=255)
    email: str = Field(..., max_length=255)
    picture: str | None = Field(None, max_length=255)
    name: str = Field(..., max_length=255)
    pref_height_metric: HeightMetric
    height: float | None
    pref_weight_metric: WeightMetric
    weight: float | None
    target_weight: float | None
    target_calories: int | None

    class Config:
        """Map Pydantic model with ORM model"""

        orm_mode = True
        allow_population_by_field_name = True


class UsersList(BaseModel):
    users: List[UserBase]


class UserUpdate(BaseModel):
    name: str | None = Field(..., max_length=255)
    pref_height_metric: HeightMetric | None
    height: float | None
    pref_weight_metric: WeightMetric | None
    weight: float | None
    target_weight: float | None
    target_calories: int | None

    class Config:
        """Map Pydantic model with ORM model"""

        orm_mode = True
        allow_population_by_field_name = True
