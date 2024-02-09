def process_prefix(image_encoded: str) -> tuple[str, str, str] | tuple[str, None, None]:
    try:
        prefix, image = image_encoded.split(",")

        type: str = prefix.split(";")[0].split("/")[1]
    except ValueError:
        image: str = image_encoded
        prefix: str | None = None
        type: str = "png"

    return image, type, prefix
