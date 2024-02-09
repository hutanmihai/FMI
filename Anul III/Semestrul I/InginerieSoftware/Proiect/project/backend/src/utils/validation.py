from pydantic import Base64Bytes, BaseModel, ValidationError


class ValidationModel(BaseModel):
    image: Base64Bytes


def validate_image_base64(image: str) -> bool:
    try:
        ValidationModel(image=image)
    except ValidationError:
        return False

    return True
