import numpy as np
import cv2 as cv

from src.constants import TRAIN_DATA_PATH, AUGMENT_DATA_PATH, SHOW_AUGMENTATION_STEPS
from src.utils.helpers import show_image
from src.utils.readers import get_images


def add_blur(image: np.ndarray) -> np.ndarray:
    return cv.GaussianBlur(image, (3, 3), 2)


def rotate_image(image: np.ndarray, angle: int) -> np.ndarray:
    random = np.random.randint(0, 2)
    if random == 0:
        angle = -angle

    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv.INTER_LINEAR)
    return result


def change_ilumination(image: np.ndarray) -> np.ndarray:
    random = np.random.randint(0, 2)
    if random == 0:
        return cv.addWeighted(image, 1.15, np.zeros(image.shape, image.dtype), 0, 0)
    else:
        return cv.addWeighted(image, 0.85, np.zeros(image.shape, image.dtype), 0, 0)


def augment_data():
    images = get_images(TRAIN_DATA_PATH)

    for k, image in images.items():
        image_copy = image.copy()
        image = add_blur(image)
        blur_copy = image.copy()
        image = change_ilumination(image)
        illumintation_copy = image.copy()
        image = rotate_image(image, 2)
        rotation_copy = image.copy()

        if SHOW_AUGMENTATION_STEPS:
            show_image(image_copy, "Original")
            show_image(blur_copy, "Blur")
            show_image(illumintation_copy, "Illumination")
            show_image(rotation_copy, "Rotation")

        game_number = str(k[0])
        turn_number = k[1]
        if turn_number < 10:
            turn_number = "0" + str(turn_number)

        cv.imwrite(f"{AUGMENT_DATA_PATH}/{game_number}_{turn_number}.jpg", image)
