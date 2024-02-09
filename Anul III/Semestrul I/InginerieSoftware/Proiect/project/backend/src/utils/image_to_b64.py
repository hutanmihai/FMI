from base64 import b64encode

import cv2 as cv
import numpy as np


def convert_numpy_image_to_base64(image: np.ndarray, type: str) -> str:
    """Converts a numpy array to a base64 encoded image.

    Args:
        image (np.ndarray): The numpy array of the image.

    Returns:
        str: The base64 encoded image.
    """
    _, image = cv.imencode(f".{type}", image)
    image = b64encode(image).decode("utf-8")
    return image
