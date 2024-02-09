from typing import Sequence

import numpy as np
import cv2 as cv

from src.constants import (
    LOWERB_BOARD,
    UPPERB_BOARD,
    BOARD_WIDTH,
    BOX_SIZE,
    BOARD_HEIGHT,
    SHOW_BOARD_EXTRACTION_POINTS,
    SHOW_BOARD_LINES,
    SHOW_BOARD_EXTRACTION_STEPS,
)
from src.utils.helpers import get_lines, show_image, get_mask


########################################################################################################################
# SHOW FUNCTIONS
########################################################################################################################
def show_board_lines(image: np.ndarray) -> None:
    lines_horizontal, lines_vertical = get_lines()
    for line in lines_vertical:
        cv.line(image, line[0], line[1], (0, 255, 0), 5)
    for line in lines_horizontal:
        cv.line(image, line[0], line[1], (0, 0, 255), 5)
    show_image(image, "Lines")


def show_board_extraction_points(
    image: np.ndarray,
    top_left: tuple[int, int],
    bottom_left: tuple[int, int],
    top_right: tuple[int, int],
    bottom_right: tuple[int, int],
) -> None:
    image_copy = image.copy()
    cv.circle(image_copy, tuple(top_left), 20, (0, 0, 255), -1)
    cv.circle(image_copy, tuple(top_right), 20, (0, 0, 255), -1)
    cv.circle(image_copy, tuple(bottom_left), 20, (0, 0, 255), -1)
    cv.circle(image_copy, tuple(bottom_right), 20, (0, 0, 255), -1)
    show_image(image_copy)


########################################################################################################################


def find_extreme_points(
    contours: Sequence[np.ndarray],
) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]:
    max_area = 0

    # Default the entire image
    top_left = (0, 0)
    bottom_right = (3072, 4080)
    top_right = (3072, 0)
    bottom_left = (0, 4080)

    for i in range(len(contours)):
        if len(contours[i]) > 3:
            possible_top_left = None
            possible_bottom_right = None
            for point in contours[i].squeeze():
                if possible_top_left is None or point[0] + point[1] < possible_top_left[0] + possible_top_left[1]:
                    possible_top_left = point

                if (
                    possible_bottom_right is None
                    or point[0] + point[1] > possible_bottom_right[0] + possible_bottom_right[1]
                ):
                    possible_bottom_right = point

            diff = np.diff(contours[i].squeeze(), axis=1)
            possible_top_right = contours[i].squeeze()[np.argmin(diff)]
            possible_bottom_left = contours[i].squeeze()[np.argmax(diff)]
            if (
                cv.contourArea(
                    np.array(
                        [
                            [possible_top_left],
                            [possible_top_right],
                            [possible_bottom_right],
                            [possible_bottom_left],
                        ]
                    )
                )
                > max_area
            ):
                max_area = cv.contourArea(
                    np.array(
                        [
                            [possible_top_left],
                            [possible_top_right],
                            [possible_bottom_right],
                            [possible_bottom_left],
                        ]
                    )
                )
                top_left = possible_top_left
                bottom_right = possible_bottom_right
                top_right = possible_top_right
                bottom_left = possible_bottom_left

    return top_left, bottom_left, top_right, bottom_right


def sharpen_image(image: np.ndarray) -> np.ndarray:
    image_copy = image.copy()

    mask = get_mask(image, LOWERB_BOARD, UPPERB_BOARD)
    mask_copy = mask.copy()

    image_m_blur = cv.medianBlur(mask, 5)
    image_g_blur = cv.GaussianBlur(image_m_blur, (3, 3), 5)
    image_sharpened = cv.addWeighted(image_m_blur, 1.5, image_g_blur, -0.8, 0)
    sharpen_copy = image_sharpened.copy()

    _, thresh = cv.threshold(image_sharpened, 151, 255, cv.THRESH_BINARY)
    threshold_copy = thresh.copy()

    kernel = np.ones((3, 3), np.uint8)
    thresh = cv.erode(thresh, kernel, iterations=4)
    erosion_copy = thresh.copy()

    thresh = cv.dilate(thresh, kernel, iterations=3)
    dilatation_copy = thresh.copy()

    if SHOW_BOARD_EXTRACTION_STEPS:
        show_image(image_copy, "Original")
        show_image(mask_copy, "Mask")
        show_image(sharpen_copy, "Sharpened")
        show_image(threshold_copy, "Threshold")
        show_image(erosion_copy, "Eroded")
        show_image(dilatation_copy, "Dilated")

    return thresh


def get_image_contours(image: np.ndarray):
    image_copy = image.copy()

    edges = cv.Canny(image, 200, 400, apertureSize=7)
    edges_copy = edges.copy()

    contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if SHOW_BOARD_EXTRACTION_STEPS:
        cv.drawContours(image_copy, contours, -1, (0, 255, 0), 3)

        show_image(edges_copy, "Edges")
        show_image(image_copy, "Contours")

    return contours


def extract_board_coordinates(
    image: np.ndarray,
) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]:
    sharpened_image = sharpen_image(image)
    contours = get_image_contours(sharpened_image)

    return find_extreme_points(contours)


def extract_board(image: np.ndarray) -> np.ndarray:
    top_left, bottom_left, top_right, bottom_right = extract_board_coordinates(image)
    width = BOARD_WIDTH * BOX_SIZE
    height = BOARD_HEIGHT * BOX_SIZE

    if SHOW_BOARD_EXTRACTION_POINTS:
        show_board_extraction_points(image, top_left, bottom_left, top_right, bottom_right)

    puzzle = np.array([top_left, top_right, bottom_right, bottom_left], dtype="float32")
    destination_of_puzzle = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype="float32")

    M = cv.getPerspectiveTransform(puzzle, destination_of_puzzle)

    result = cv.warpPerspective(image, M, (width, height))

    if SHOW_BOARD_LINES:
        show_board_lines(result)

    return result
