import numpy as np
from fastapi import APIRouter, HTTPException
from schemas.image import Image
from schemas.image_editing import BlurImagePayload, ObjectRemovalPayload
from services.background_removal import remove_background
from services.blur import blur_image
from services.object_removal import remove_object
from starlette import status
from utils.b64_to_image import convert_base64_to_numpy_image
from utils.image_response import image_response
from utils.image_to_b64 import convert_numpy_image_to_base64
from utils.prefix import process_prefix
from utils.validation import validate_image_base64

router: APIRouter = APIRouter(tags=["Image Editing"])


@router.post(path="/blur", summary="Blur Image", status_code=status.HTTP_200_OK, response_model=Image)
async def blur(payload: BlurImagePayload):
    image = payload.image
    blur_type = payload.type
    blur_value = payload.value

    if not validate_image_base64(image):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Image")

    image, type, prefix = process_prefix(image)
    image_np: np.ndarray = convert_base64_to_numpy_image(image)
    blurred_image: np.ndarray = blur_image(image_np, blur_type, blur_value)
    image_encoded: str = convert_numpy_image_to_base64(blurred_image, type)

    return image_response(image_encoded, prefix)


@router.post(
    path="/object-removal", summary="Remove Object From Image", status_code=status.HTTP_200_OK, response_model=Image
)
async def object_removal(payload: ObjectRemovalPayload):
    image = payload.image
    x0 = payload.x0
    y0 = payload.y0
    w = payload.width
    h = payload.height

    if not validate_image_base64(image):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Image")

    # 487 164 26 97

    image, type, prefix = process_prefix(image)
    image_np: np.ndarray = convert_base64_to_numpy_image(image)
    new_image: np.ndarray = remove_object(image_np, x0, y0, w, h, debug=False)
    image_encoded: str = convert_numpy_image_to_base64(new_image, type)

    return image_response(image_encoded, prefix)


@router.post(
    path="/background-removal",
    summary="Remove Background From Image",
    status_code=status.HTTP_200_OK,
    response_model=Image,
)
async def background_removal(payload: Image):
    if not validate_image_base64(payload.image):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Image")
    image, type, prefix = process_prefix(payload.image)
    image_np: np.ndarray = convert_base64_to_numpy_image(image)
    new_image: np.ndarray = remove_background(image_np)
    image_encoded: str = convert_numpy_image_to_base64(new_image, type)

    return image_response(image_encoded, prefix)
