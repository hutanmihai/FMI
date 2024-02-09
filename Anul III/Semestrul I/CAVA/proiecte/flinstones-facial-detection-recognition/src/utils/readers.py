from collections import defaultdict
from glob import glob
from pathlib import Path

import cv2 as cv
import numpy as np


def get_images(path: Path) -> list[np.ndarray]:
    images_glob = sorted(glob(str(path / "*.jpg")))
    images = [cv.imread(str(image)) for image in images_glob]
    return images


def get_annotations(path: Path) -> dict[str, list[tuple[tuple[int, int, int, int], str]]]:
    dictionary = defaultdict(list)
    with open(path, "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.split(" ")
        image_name: str = line[0]
        xmin: int = int(line[1])
        ymin: int = int(line[2])
        xmax: int = int(line[3])
        ymax: int = int(line[4])
        character: str = line[5].rstrip()
        dictionary[image_name].append(((xmin, ymin, xmax, ymax), character))

    return dictionary
