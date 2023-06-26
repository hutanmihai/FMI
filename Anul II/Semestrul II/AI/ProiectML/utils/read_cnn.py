import os

import numpy as np
import pandas as pd
from PIL import Image, ImageEnhance
from imblearn.over_sampling import SMOTE

image_size = (112, 112)


def read(id):
    image_resize = image_size
    data_dir_path = os.path.join(os.getcwd(), "../data/data/")
    img_path = os.path.join(data_dir_path, id)
    img = Image.open(img_path)
    img = img.resize(image_resize)
    img = img.convert("L")
    image = ImageEnhance.Contrast(img).enhance(2)
    image_arr = np.array(image).astype(np.float64)
    image_arr = image_arr / 255.0
    return image_arr


def read_test():
    test_dataframe = pd.read_csv(
        "../data_frames/test_dataframe.csv", sep=",", names=["id"]
    )
    test_images_ids = test_dataframe["id"].values
    test_images = []

    for img_id in test_images_ids:
        test_images.append(read(img_id))

    test_images = np.array(test_images).reshape((-1, image_size[0], image_size[1], 1))

    return np.array(test_images)


def read_validation():
    validation_dataframe = pd.read_csv(
        "../data_frames/validation_dataframe.csv", sep=",", names=["id", "class"]
    )
    validation_images_ids = validation_dataframe["id"].values
    validation_images = []
    validation_labels = validation_dataframe["class"].values

    for img_id in validation_images_ids:
        validation_images.append(read(img_id))

    validation_images = np.array(validation_images).reshape(
        (-1, image_size[0], image_size[1], 1)
    )
    validation_labels = np.array(validation_labels).reshape(-1, 1)

    return np.array(validation_images), np.array(validation_labels)


def read_train():
    train_dataframe = pd.read_csv(
        "../data_frames/train_dataframe.csv", sep=",", names=["id", "class"]
    )
    train_images_ids = train_dataframe["id"].values
    train_images = []
    train_labels = train_dataframe["class"].values

    for img_id in train_images_ids:
        train_images.append(read(img_id))

    train_images = np.array(train_images).reshape((-1, image_size[0], image_size[1], 1))
    train_labels = np.array(train_labels).reshape(-1, 1)

    return train_images, train_labels


def read_train_smote(slice_value: int = None):
    train_dataframe = pd.read_csv(
        "../data_frames/train_dataframe.csv", sep=",", names=["id", "class"]
    )

    if slice is None:
        train_images_ids = train_dataframe["id"].values
        train_labels = train_dataframe["class"].values

    else:
        train_images_ids_0 = train_dataframe[train_dataframe["class"] == 0][
            "id"
        ].values[:slice_value]
        train_images_labels_0 = train_dataframe[train_dataframe["class"] == 0][
            "class"
        ].values[:slice_value]
        train_images_ids_1 = train_dataframe[train_dataframe["class"] == 1]["id"].values
        train_images_labels_1 = train_dataframe[train_dataframe["class"] == 1][
            "class"
        ].values

        train_images_ids = np.concatenate((train_images_ids_0, train_images_ids_1))
        train_images_labels = np.concatenate(
            (train_images_labels_0, train_images_labels_1)
        )

        perm = np.random.permutation(len(train_images_ids))
        train_images_ids = train_images_ids[perm]
        train_labels = train_images_labels[perm]

    train_images = []

    for img_id in train_images_ids:
        train_images.append(read(img_id))

    train_images = np.array(train_images)
    train_labels = np.array(train_labels)

    train_images = train_images.reshape(train_images.shape[0], -1)

    sm = SMOTE(random_state=42, k_neighbors=10, sampling_strategy="auto")
    train_images_smote, train_labels_smote = sm.fit_resample(train_images, train_labels)

    train_images_smote = train_images_smote.reshape(
        (-1, image_size[0], image_size[1], 1)
    )
    train_labels_smote = train_labels_smote.reshape(-1, 1)

    return train_images_smote, train_labels_smote
