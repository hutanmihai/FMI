import uuid

from sqlalchemy import FLOAT, INT, VARCHAR, Column
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Product(BaseModel):
    __tablename__ = "product"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(VARCHAR(255), nullable=False)
    calories = Column(FLOAT(precision=None, decimal_return_scale=2), nullable=False)
    fat = Column(FLOAT(precision=None, decimal_return_scale=2), nullable=False)
    carbs = Column(FLOAT(precision=None, decimal_return_scale=2), nullable=False)
    protein = Column(FLOAT(precision=None, decimal_return_scale=2), nullable=False)
    upvotes = Column(INT(), nullable=False)
    downvotes = Column(INT(), nullable=False)
    meal_products = relationship(
        "MealProduct", back_populates="product", cascade="all, delete"
    )
    diary_products = relationship(
        "DiaryProduct", back_populates="product", cascade="all, delete"
    )
