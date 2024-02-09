from schemas.image import Image


def image_response(image_encoded: str, prefix: str | None = None) -> Image:
    """
    Returns the Image Response depending on the prefix if it is None or str
    :param image_encoded:
    :param prefix:
    :return:
    """
    if prefix is None:
        return Image(image=image_encoded)
    return Image(image=f"{prefix},{image_encoded}")
