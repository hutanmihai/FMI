import numpy as np
from rembg import remove


def remove_background(image: np.ndarray) -> np.ndarray:
    return remove(image)
