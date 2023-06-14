from pydantic import BaseModel


class ApiError(BaseModel):
    detail: str

    class Config:
        schema_extra = {
            "example": {
                "detail": "<error description>",
            }
        }
