import numpy as np

from src.constants import (
    LOWERB_PIECE,
    UPPERB_PIECE,
    SHOW_DETECTED_PIECES,
    CENTER_TEXT_POSITIONS,
    CENTER_TEXT_PATH,
)
from src.utils.helpers import get_lines, get_mask, show_image
import cv2 as cv


####################################################################################################
# SHOW FUNCTIONS
####################################################################################################


def visualize_detected_pieces(image: np.ndarray, positions: list[tuple[int, int]]) -> None:
    lines_horizontal, lines_vertical = get_lines()
    image_copy = image.copy()

    for i in range(len(lines_horizontal) - 1):
        for j in range(len(lines_vertical) - 1):
            y_min = lines_vertical[j][0][0]
            y_max = lines_vertical[j + 1][1][0]
            x_min = lines_horizontal[i][0][1]
            x_max = lines_horizontal[i + 1][1][1]
            if (i, j) in positions:
                cv.rectangle(
                    image_copy,
                    (y_min, x_min),
                    (y_max, x_max),
                    color=(255, 0, 0),
                    thickness=5,
                )

    show_image(image_copy, "Detected pieces")


####################################################################################################


def template_matching_on_center_text(image: np.ndarray, position: tuple[int, int]) -> bool:
    if position not in CENTER_TEXT_POSITIONS:
        return False

    template = cv.imread(str(CENTER_TEXT_PATH / f"{position[0]}_{position[1]}.jpg"))
    template_mask = get_mask(template, LOWERB_PIECE, UPPERB_PIECE)

    image_copy = image.copy()
    result = cv.matchTemplate(image_copy, template_mask, cv.TM_CCOEFF_NORMED)

    threshold = 0.27
    loc = np.where(result >= threshold)

    return len(loc[0]) > 0


def get_neighbours(position: tuple[int, int]) -> list[tuple[int, int]]:
    neighbours = []
    if position[0] > 0:
        neighbours.append((position[0] - 1, position[1]))
    if position[0] < 14:
        neighbours.append((position[0] + 1, position[1]))
    if position[1] > 0:
        neighbours.append((position[0], position[1] - 1))
    if position[1] < 14:
        neighbours.append((position[0], position[1] + 1))

    return neighbours


def detect_domino_pieces(mask: np.ndarray) -> list[tuple[int, int]]:
    lines_horizontal, lines_vertical = get_lines()

    domino_pieces_positions = []
    num = 15

    for i in range(len(lines_horizontal) - 1):
        for j in range(len(lines_vertical) - 1):
            if (i, j) in CENTER_TEXT_POSITIONS:
                patch = mask[
                    lines_horizontal[i][0][1] : lines_horizontal[i + 1][1][1],
                    lines_vertical[j][0][0] : lines_vertical[j + 1][1][0],
                ].copy()
                if template_matching_on_center_text(patch, (i, j)):
                    continue
            y_min = lines_vertical[j][0][0] + num
            y_max = lines_vertical[j + 1][1][0] - num
            x_min = lines_horizontal[i][0][1] + num
            x_max = lines_horizontal[i + 1][1][1] - num
            patch = mask[x_min:x_max, y_min:y_max].copy()
            medie_patch = np.mean(patch)
            if medie_patch > 110:
                domino_pieces_positions.append((i, j))

    return domino_pieces_positions


def get_positions(image: np.ndarray, domino_pieces_positions: list[tuple[int, int]]) -> list[tuple[int, int]]:
    mask = get_mask(image, LOWERB_PIECE, UPPERB_PIECE)

    positions = detect_domino_pieces(mask)

    if SHOW_DETECTED_PIECES:
        show_image(mask, "Mask")
        visualize_detected_pieces(image, positions)

    positions = [position for position in positions if position not in domino_pieces_positions]

    for position in positions:
        neighbours = get_neighbours(position)
        for neighbour in neighbours:
            if neighbour in positions and neighbour not in domino_pieces_positions:
                return [position, neighbour]

    return positions
