from pydantic import BaseModel


class TokenSchema(BaseModel):
    token: str

    class Config:
        schema_extra = {
            "token": "<jwt token>",
        }
