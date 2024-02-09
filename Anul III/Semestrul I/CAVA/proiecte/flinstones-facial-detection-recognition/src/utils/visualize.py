from pathlib import Path

import cv2 as cv
import numpy as np

from src.constants import (
    COLOR_CHARACTER_MAPPING,
    SOLUTION_DETECTIONS_PATH,
    SOLUTION_SCORES_PATH,
    SOLUTION_FILE_NAMES_PATH,
    VALIDATION_ANNOTATIONS_PATH,
    VALIDATION_IMAGES_PATH,
)
from src.utils.helpers import show_image
from src.utils.readers import get_annotations, get_images


def visualize_images_with_boxes(images_path: Path, annotations_path: Path):
    images = get_images(images_path)
    annotations = get_annotations(annotations_path)
    for image_name in annotations.keys():
        image: np.ndarray = images[int(image_name.split(".")[0]) - 1]
        for coordinates, character in annotations[image_name]:
            xmin, ymin, xmax, ymax = coordinates
            cv.rectangle(image, (xmin, ymin), (xmax, ymax), COLOR_CHARACTER_MAPPING[character], 1)
        show_image(image, title=image_name)


def visualize_images_with_boxes_and_detections(gt_path: Path):
    detections = np.load(SOLUTION_DETECTIONS_PATH)
    scores = np.load(SOLUTION_SCORES_PATH)
    file_names = np.load(SOLUTION_FILE_NAMES_PATH)

    annotations = get_annotations(gt_path)

    files = {}
    for file_name in file_names:
        image = cv.imread(str(VALIDATION_IMAGES_PATH / file_name))
        files[file_name] = image

    for k, v in annotations.items():
        for box, character in v:
            try:
                cv.rectangle(files[k], (box[0], box[1]), (box[2], box[3]), COLOR_CHARACTER_MAPPING[character], 2)
            except KeyError:
                # No face detected in this image
                pass

    for file_name, detection, score in zip(file_names, detections, scores):
        file_name = file_name
        image = files[file_name]
        cv.rectangle(image, (detection[0], detection[1]), (detection[2], detection[3]), (0, 255, 0), 2)
        cv.putText(
            image,
            "score:" + str(score)[:4],
            (detection[0], detection[1]),
            cv.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            1,
        )
        show_image(image)
