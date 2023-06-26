import numpy as np
from PIL import Image, ImageFilter
from time import time


def clean_line(line: str) -> (str, str):
    image_id, image_class = line.split(",")
    image_id.rstrip()
    image_class.rstrip("\n")
    image_class.strip()
    return image_id, image_class


def get_labels_counter():
    train_txt = "../data/train_labels.txt"
    validation_txt = "../data/validation_labels.txt"

    dictionar_train = {0: 0, 1: 0}
    dictionar_validation = {0: 0, 1: 0}

    with open(train_txt, "r") as f:
        f.readline()
        line = f.readline()
        while line != "":
            image_id, image_class = clean_line(line)
            dictionar_train[int(image_class)] += 1
            line = f.readline()

    with open(validation_txt, "r") as f:
        f.readline()
        line = f.readline()
        while line != "":
            image_id, image_class = clean_line(line)
            dictionar_validation[int(image_class)] += 1
            line = f.readline()

    return dictionar_train, dictionar_validation


if __name__ == "__main__":
    start_time = time()

    dictionar_train, dictionar_validation = get_labels_counter()

    print(dictionar_train)
    print(dictionar_validation)

    print(dictionar_train[0] / dictionar_train[1])
    print(dictionar_validation[0] / dictionar_validation[1])

    print(
        (dictionar_train[0] + dictionar_validation[0])
        / (dictionar_train[1] + dictionar_validation[1])
    )

    end_time = time() - start_time
    print(f"------------------- {end_time} seconds -------------------")
