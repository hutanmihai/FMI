import numpy as np

from src.constants import (
    BOX_SIZE,
    PREPROCESS_PATCHES,
    BOARD_HEIGHT,
    BOARD_WIDTH,
    BOARD_INTEREST,
    SHOW_TEMPLATES_ON_GENERATION,
    VERTICAL_TEMPLATES_PATH,
    HORIZONTAL_TEMPLATES_PATH,
    CENTER_TEXT_POSITIONS,
    CENTER_TEXT_PATH,
)

import cv2 as cv

from src.utils.board_extraction import extract_board
from src.utils.helpers import preprocess_patch, show_image
from src.utils.readers import get_auxiliary_images


def extract_box_content(image: np.ndarray, line: int, column: int) -> np.ndarray:
    line_start = line * BOX_SIZE
    line_end = line_start + BOX_SIZE
    column_start = column * BOX_SIZE
    column_end = column_start + BOX_SIZE

    return image[line_start:line_end, column_start:column_end]


def create_median_image(images: list[np.ndarray]) -> np.ndarray:
    # Convert the list of images to a NumPy array
    images_array = np.array(images, dtype=np.float32)

    # Calculate the median of the images
    median_image = np.median(images_array, axis=0).astype(np.uint8)

    num = 16
    # reduce image size by num pixels on each side
    median_image = median_image[num:-num, num:-num]

    if PREPROCESS_PATCHES:
        median_image = preprocess_patch(median_image)

    return median_image


def check_if_position_is_of_interest(
    position: tuple[int, int],
    board_interest: dict[str, dict[int, list[tuple[int, int]]]],
    mode: str,
) -> int:
    interest = board_interest[mode]
    for key, value in interest.items():
        if position in value:
            return key
    return False


def generate_center_templates():
    image = get_auxiliary_images()["empty"]
    image = extract_board(image)

    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            if (i, j) in CENTER_TEXT_POSITIONS:
                box_content = extract_box_content(image, i, j)
                if SHOW_TEMPLATES_ON_GENERATION:
                    show_image(box_content, title=f"Center text {i} {j}")
                path = CENTER_TEXT_PATH / f"{i}_{j}.jpg"
                cv.imwrite(str(path), box_content)


def generate_templates():
    """Generate templates for the project."""
    generate_center_templates()

    auxiliary_images = get_auxiliary_images()

    vertical_image = auxiliary_images["vertical"]
    horizontal_image = auxiliary_images["horizontal"]

    vertical_image = extract_board(vertical_image)
    horizontal_image = extract_board(horizontal_image)

    dict_vertical = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

    dict_horizontal = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            value_vertical = check_if_position_is_of_interest((i, j), BOARD_INTEREST, "vertical")
            value_horizontal = check_if_position_is_of_interest((i, j), BOARD_INTEREST, "horizontal")

            if value_vertical is not False:
                box_content = cv.cvtColor(extract_box_content(vertical_image, i, j), cv.COLOR_BGR2GRAY)
                dict_vertical[value_vertical].append(box_content)

            if value_horizontal is not False:
                box_content = cv.cvtColor(extract_box_content(horizontal_image, i, j), cv.COLOR_BGR2GRAY)
                dict_horizontal[value_horizontal].append(box_content)

    median_images_vertical = []
    median_images_horizontal = []

    for key, value in dict_vertical.items():
        median_image = create_median_image(value)
        if SHOW_TEMPLATES_ON_GENERATION:
            show_image(median_image, title=f"Vertical {key}")
        median_images_vertical.append(median_image)
        path = VERTICAL_TEMPLATES_PATH / f"{key}.jpg"
        cv.imwrite(str(path), median_image)

    for key, value in dict_horizontal.items():
        median_image = create_median_image(value)
        if SHOW_TEMPLATES_ON_GENERATION:
            show_image(median_image, title=f"Horizontal {key}")
        median_images_horizontal.append(median_image)
        path = HORIZONTAL_TEMPLATES_PATH / f"{key}.jpg"
        cv.imwrite(str(path), median_image)
