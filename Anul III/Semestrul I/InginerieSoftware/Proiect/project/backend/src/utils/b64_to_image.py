from base64 import b64decode

import cv2 as cv
import numpy as np


def convert_base64_to_numpy_image(image_encoded: str) -> np.ndarray:
    """Converts a base64 encoded image to a numpy array.

    Args:
        image (str): The base64 encoded image.

    Returns:
        np.ndarray: The numpy array of the image.
    """
    image_decoded: bytes = b64decode(image_encoded)
    np_data: np.ndarray = np.frombuffer(image_decoded, np.uint8)
    image: np.ndarray = cv.imdecode(np_data, cv.IMREAD_COLOR)

    return image
