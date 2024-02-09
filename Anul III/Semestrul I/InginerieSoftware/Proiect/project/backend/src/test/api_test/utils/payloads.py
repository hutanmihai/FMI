async def get_blur_image_payload(
    image: str | None = None, value: int | None = None, type: str | None = None
) -> dict[str, str | int]:
    payload = {}
    if image is not None:
        payload["image"] = image
    if value is not None:
        payload["value"] = value
    if type is not None:
        payload["type"] = type

    return payload


async def get_object_removal_payload(
    image: str | None = None,
    x0: int | None = None,
    y0: int | None = None,
    width: int | None = None,
    height: int | None = None,
) -> dict[str, str | int]:
    payload = {}
    if image is not None:
        payload["image"] = image
    if x0 is not None:
        payload["x0"] = x0
    if y0 is not None:
        payload["y0"] = y0
    if width is not None:
        payload["width"] = width
    if height is not None:
        payload["height"] = height

    return payload


async def get_background_removal_payload(image: str | None = None) -> dict[str, str]:
    payload = {}
    if image is not None:
        payload["image"] = image

    return payload
