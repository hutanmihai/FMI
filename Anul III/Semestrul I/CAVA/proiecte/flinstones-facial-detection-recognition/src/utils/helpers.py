import os
from pathlib import Path

import cv2 as cv
import numpy as np

from src.constants import SOLUTION_PATH, SOLUTION_TASK1_PATH, SOLUTION_TASK2_PATH, IOU_THRESHOLD


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


def check_if_dirs_exist(paths: list[Path]) -> None:
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)


def write_solution(
    detections: np.ndarray,
    detection_path: Path,
    scores: np.ndarray,
    scores_path: Path,
    file_names: np.ndarray,
    file_names_path: Path,
) -> None:
    check_if_dirs_exist([SOLUTION_PATH, SOLUTION_TASK1_PATH, SOLUTION_TASK2_PATH])
    np.save(detection_path, detections)
    np.save(scores_path, scores)
    np.save(file_names_path, file_names)


def intersection_over_union(bbox_a, bbox_b):
    x_a = max(bbox_a[0], bbox_b[0])
    y_a = max(bbox_a[1], bbox_b[1])
    x_b = min(bbox_a[2], bbox_b[2])
    y_b = min(bbox_a[3], bbox_b[3])

    inter_area = max(0, x_b - x_a + 1) * max(0, y_b - y_a + 1)

    box_a_area = (bbox_a[2] - bbox_a[0] + 1) * (bbox_a[3] - bbox_a[1] + 1)
    box_b_area = (bbox_b[2] - bbox_b[0] + 1) * (bbox_b[3] - bbox_b[1] + 1)

    iou = inter_area / float(box_a_area + box_b_area - inter_area)

    return iou


def non_maximal_suppression(image_detections, image_scores):
    sorted_indices = np.argsort(image_scores)[::-1]
    sorted_image_detections = image_detections[sorted_indices]
    sorted_scores = image_scores[sorted_indices]

    is_maximal = np.ones(len(image_detections)).astype(bool)
    for i in range(len(sorted_image_detections) - 1):
        if is_maximal[i]:
            for j in range(i + 1, len(sorted_image_detections)):
                if is_maximal[j]:
                    if intersection_over_union(sorted_image_detections[i], sorted_image_detections[j]) > IOU_THRESHOLD:
                        is_maximal[j] = False
                    elif (  # verificam daca detectia este complet in interiorul detectiei cu scor mai mare
                        sorted_image_detections[i][0] <= sorted_image_detections[j][0]
                        and sorted_image_detections[i][1] <= sorted_image_detections[j][1]
                        and sorted_image_detections[i][2] >= sorted_image_detections[j][2]
                        and sorted_image_detections[i][3] >= sorted_image_detections[j][3]
                    ):
                        is_maximal[j] = False
                    else:  # verificam daca centrul detectiei este in mijlocul detectiei cu scor mai mare
                        c_x = (sorted_image_detections[j][0] + sorted_image_detections[j][2]) / 2
                        c_y = (sorted_image_detections[j][1] + sorted_image_detections[j][3]) / 2
                        if (
                            sorted_image_detections[i][0] <= c_x <= sorted_image_detections[i][2]
                            and sorted_image_detections[i][1] <= c_y <= sorted_image_detections[i][3]
                        ):
                            is_maximal[j] = False

    return sorted_image_detections[is_maximal], sorted_scores[is_maximal]
