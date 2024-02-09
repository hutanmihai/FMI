import numpy as np

from src.constants import VERTICAL_TEMPLATES_PATH, HORIZONTAL_TEMPLATES_PATH
from src.utils.helpers import get_patch
import cv2 as cv


########################################################################################################################
# CLASSIFICATION
########################################################################################################################
def classify(image: np.ndarray, position: tuple[int, int]) -> int:
    """
    Classifies a patch.
    :param patch: the patch to classify
    :return: the value of the patch
    """
    patch = get_patch(image, position, 2)

    maxi = -np.inf
    poz = -1
    for j in range(0, 7):
        path_vertical = VERTICAL_TEMPLATES_PATH / f"{str(j)}.jpg"
        path_horizontal = HORIZONTAL_TEMPLATES_PATH / f"{str(j)}.jpg"
        img_template_vertical = cv.imread(str(path_vertical))
        img_template_horizontal = cv.imread(str(path_horizontal))
        img_template_vertical = cv.cvtColor(img_template_vertical, cv.COLOR_BGR2GRAY)
        img_template_horizontal = cv.cvtColor(img_template_horizontal, cv.COLOR_BGR2GRAY)
        corr_vertical = cv.matchTemplate(patch, img_template_vertical, cv.TM_CCOEFF_NORMED)
        corr_vertical = np.max(corr_vertical)
        corr_horizontal = cv.matchTemplate(patch, img_template_horizontal, cv.TM_CCOEFF_NORMED)
        corr_horizontal = np.max(corr_horizontal)

        if corr_vertical > maxi:
            maxi = corr_vertical
            poz = j

        if corr_horizontal > maxi:
            maxi = corr_horizontal
            poz = j

    return poz
