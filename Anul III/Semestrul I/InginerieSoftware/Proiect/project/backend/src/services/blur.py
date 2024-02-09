from typing import Literal

import cv2 as cv
import numpy as np


def blur_image(image: np.ndarray, blur_type: Literal["gaussian", "median", "bilateral", "blur"], value: int):
    if value <= 20:
        kernel_size = 3
    elif value <= 40:
        kernel_size = 5
    elif value <= 60:
        kernel_size = 7
    elif value <= 80:
        kernel_size = 9
    else:
        kernel_size = 11

    """Blurs an image."""
    if blur_type == "gaussian":
        return cv.GaussianBlur(image, (kernel_size, kernel_size), 0)
    elif blur_type == "median":
        return cv.medianBlur(image, kernel_size)
    elif blur_type == "bilateral":
        return cv.bilateralFilter(image, kernel_size, 75, 75)
    elif blur_type == "blur":
        return cv.blur(image, (kernel_size, kernel_size))
