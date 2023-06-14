from pydantic import UUID4, BaseModel


class EntityID(BaseModel):
    id: UUID4
