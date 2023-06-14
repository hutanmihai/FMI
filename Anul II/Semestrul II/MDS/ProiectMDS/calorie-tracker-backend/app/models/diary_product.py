import uuid

from sqlalchemy import FLOAT, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class DiaryProduct(BaseModel):
    __tablename__ = "diary_product"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    diary_id = Column(ForeignKey("diary.id"), nullable=False)
    product_id = Column(ForeignKey("product.id"), nullable=False)
    quantity_grams = Column(
        FLOAT(precision=None, decimal_return_scale=2), nullable=False
    )
    diary = relationship("Diary", back_populates="diary_products")
    product = relationship("Product", back_populates="diary_products")

    @property
    def calories(self) -> float:
        return round(self.product.calories * (self.quantity_grams / 100), 2)

    @property
    def protein(self) -> float:
        return round(self.product.protein * (self.quantity_grams / 100), 2)

    @property
    def fat(self) -> float:
        return round(self.product.fat * (self.quantity_grams / 100), 2)

    @property
    def carbs(self) -> float:
        return round(self.product.carbs * (self.quantity_grams / 100), 2)
