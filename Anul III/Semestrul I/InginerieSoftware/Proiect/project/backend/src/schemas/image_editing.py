from typing import Literal

from pydantic import Field
from schemas.image import Image


class BlurImagePayload(Image):
    value: int = Field(..., ge=0, le=100, description="Blur Value")
    type: Literal["gaussian", "median", "bilateral", "blur"] = Field(..., description="Blur Type")


class ObjectRemovalPayload(Image):
    x0: int = Field(..., ge=0, description="Top Left X Coordinate")
    y0: int = Field(..., ge=0, description="Top Left Y Coordinate")
    width: int = Field(..., ge=0, description="Width of the Rectangle")
    height: int = Field(..., ge=0, description="Height of the Rectangle")
