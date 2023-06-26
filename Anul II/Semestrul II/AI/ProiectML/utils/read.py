import numpy as np
from PIL import Image, ImageEnhance
from time import time


def clean_line(line: str) -> (str, str):
    image_id, image_class = line.split(",")
    image_id.rstrip()
    image_class.rstrip("\n")
    image_class.strip()
    return image_id, image_class


def generate_numpy_array(image_path: str) -> np.ndarray:
    image = Image.open(image_path)
    image = image.resize((224, 224))
    image = image.convert("L")  # convert to grayscale
    image = ImageEnhance.Contrast(image).enhance(2)  # Increase the contrast

    return np.asarray(image).astype(np.float64) / 255


def generate_numpy_arrays_for_train_and_validation():
    data_dir = "../data/data/"
    save_dir = "../numpy_data/"
    train_txt = "../data/train_labels.txt"
    validation_txt = "../data/validation_labels.txt"

    train_data = []
    train_labels = []

    train_data_0 = []
    train_data_1 = []

    train_labels_0 = []
    train_labels_1 = []

    validation_data = []
    validation_labels = []

    test_data = []

    with open(train_txt, "r") as f:
        f.readline()
        line = f.readline()
        while line != "":
            image_id, image_class = clean_line(line)
            image_path = data_dir + image_id + ".png"
            array = generate_numpy_array(image_path)

            if int(image_class) == 0:
                train_data_0.append(array)
                train_labels_0.append(0)
            else:
                train_data_1.append(array)
                train_labels_1.append(1)

            # train_data.append(generate_numpy_array(image_path))
            # train_labels.append(bool(int(image_class)))
            line = f.readline()

    with open(validation_txt, "r") as f:
        f.readline()
        line = f.readline()
        while line != "":
            image_id, image_class = clean_line(line)
            image_path = data_dir + image_id + ".png"
            validation_data.append(generate_numpy_array(image_path))
            validation_labels.append(int(image_class))
            line = f.readline()

    # number_of_read_images = len(train_data) + len(validation_data)
    number_of_read_images = 17000
    number_of_last_image = 22149

    for image_id in range(number_of_read_images + 1, number_of_last_image + 1):
        image_path = data_dir + str(image_id).zfill(6) + ".png"
        test_data.append(generate_numpy_array(image_path))

    # SLICE DATA
    slice_size = 6000
    train_data_0 = train_data_0[:slice_size]
    train_labels_0 = train_labels_0[:slice_size]

    train_data = train_data_0 + train_data_1
    train_labels = train_labels_0 + train_labels_1

    train_data = np.array(train_data).astype(np.float64)
    train_labels = np.array(train_labels).astype(np.float64)
    validation_data = np.array(validation_data).astype(np.float64)
    validation_labels = np.array(validation_labels).astype(np.float64)
    test_data = np.array(test_data).astype(np.float64)

    np.save(save_dir + "train_data.npy", train_data.reshape(train_data.shape[0], -1))
    np.save(save_dir + "train_labels.npy", train_labels)
    np.save(
        save_dir + "validation_data.npy",
        validation_data.reshape(validation_data.shape[0], -1),
    )
    np.save(save_dir + "validation_labels.npy", validation_labels)
    np.save(save_dir + "test_data.npy", test_data.reshape(test_data.shape[0], -1))


if __name__ == "__main__":
    start_time = time()

    generate_numpy_arrays_for_train_and_validation()

    end_time = time() - start_time
    print(f"------------------- {end_time} seconds -------------------")
