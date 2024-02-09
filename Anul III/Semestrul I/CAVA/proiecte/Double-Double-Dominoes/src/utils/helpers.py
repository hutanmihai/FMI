import numpy as np

from src.constants import (
    PREPROCESS_PATCHES,
    SHOW_PATCHES,
    BOARD_WIDTH,
    BOX_SIZE,
    SHOW_PATCHES_PREPROCESSING,
)
import cv2 as cv


########################################################################################################################
# CORE SHOW IMAGE FUNCTION
########################################################################################################################


def show_image(image: np.ndarray, title: str = "image") -> None:
    """
    Shows the image.
    :param title: the title of the window, default is "image"
    :param image: the image to show
    :return:
    """
    cv.namedWindow(title, cv.WINDOW_KEEPRATIO)
    cv.imshow(title, image)
    cv.waitKey(0)
    cv.destroyAllWindows()


########################################################################################################################


def get_patch(image: np.ndarray, position: tuple[int, int], num: int) -> np.ndarray:
    lines_horizontal, lines_vertical = get_lines()

    y_min = lines_vertical[position[1]][0][0] + num
    y_max = lines_vertical[position[1] + 1][1][0] - num
    x_min = lines_horizontal[position[0]][0][1] + num
    x_max = lines_horizontal[position[0] + 1][1][1] - num

    patch = cv.cvtColor(image[x_min:x_max, y_min:y_max].copy(), cv.COLOR_BGR2GRAY)

    if PREPROCESS_PATCHES:
        patch = preprocess_patch(patch)

    if SHOW_PATCHES:
        show_image(patch, "Patch")

    return patch


########################################################################################################################
# MASK GETTER
########################################################################################################################
def get_mask(image: np.ndarray, lowerb: np.ndarray, upperb: np.ndarray) -> np.ndarray:
    img_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    mask = cv.inRange(img_hsv, lowerb, upperb)
    return mask


########################################################################################################################
# LINES GETTER
########################################################################################################################
def get_lines() -> tuple[list[list[tuple[int, int]]], list[list[tuple[int, int]]]]:
    lines_horizontal = []
    lines_vertical = []
    for i in range(0, BOARD_WIDTH * BOX_SIZE + 1, BOX_SIZE):
        lines_horizontal.append([(0, i), (BOARD_WIDTH * BOX_SIZE - 1, i)])
        lines_vertical.append([(i, 0), (i, BOARD_WIDTH * BOX_SIZE - 1)])

    return lines_horizontal, lines_vertical


########################################################################################################################
# HSV
########################################################################################################################
def find_color_values_using_trackbar(frame: np.ndarray) -> None:
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    cv.namedWindow("Frame", cv.WINDOW_KEEPRATIO)
    cv.namedWindow("Mask", cv.WINDOW_KEEPRATIO)
    cv.namedWindow("Res", cv.WINDOW_KEEPRATIO)

    def nothing(x):
        pass

    cv.namedWindow("Trackbar")
    cv.createTrackbar("LH", "Trackbar", 0, 255, nothing)
    cv.createTrackbar("LS", "Trackbar", 0, 255, nothing)
    cv.createTrackbar("LV", "Trackbar", 0, 255, nothing)
    cv.createTrackbar("UH", "Trackbar", 255, 255, nothing)
    cv.createTrackbar("US", "Trackbar", 255, 255, nothing)
    cv.createTrackbar("UV", "Trackbar", 255, 255, nothing)

    while True:
        l_h = cv.getTrackbarPos("LH", "Trackbar")
        l_s = cv.getTrackbarPos("LS", "Trackbar")
        l_v = cv.getTrackbarPos("LV", "Trackbar")
        u_h = cv.getTrackbarPos("UH", "Trackbar")
        u_s = cv.getTrackbarPos("US", "Trackbar")
        u_v = cv.getTrackbarPos("UV", "Trackbar")

        l = np.array([l_h, l_s, l_v])
        u = np.array([u_h, u_s, u_v])
        mask_table_hsv = cv.inRange(frame_hsv, l, u)

        res = cv.bitwise_and(frame, frame, mask=mask_table_hsv)
        cv.imshow("Frame", frame)
        cv.imshow("Mask", mask_table_hsv)
        cv.imshow("Res", res)

        if cv.waitKey(25) & 0xFF == ord("q"):
            cv.destroyAllWindows()
            break


########################################################################################################################
# PREPROCESS
########################################################################################################################
def preprocess_patch(image: np.ndarray) -> np.ndarray:
    image_copy = image.copy()

    # image = cv.GaussianBlur(image, (3, 3), 0)
    # image = cv.medianBlur(image, 3)
    # image = cv.bilateralFilter(image, 12, 50, 50)

    kernel = np.ones((3, 3), np.uint8)
    image = cv.dilate(image, kernel, iterations=4)
    image = cv.erode(image, kernel, iterations=5)

    if SHOW_PATCHES_PREPROCESSING:
        show_image(image_copy, "Original")
        show_image(image, "Patch")

    return image
