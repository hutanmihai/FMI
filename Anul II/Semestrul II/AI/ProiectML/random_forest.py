from time import time

import numpy as np
import pandas as pd
from PIL import Image, ImageEnhance
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, classification_report


# This function is used to clean the line from the train_labels.txt and validation_labels.txt files so
# that we can extract the image_id and the image_class, not additional blank characters which might brake the code
def clean_line(line: str) -> (str, str):
    image_id, image_class = line.split(",")
    image_id.rstrip()
    image_class.rstrip("\n")
    image_class.strip()
    return image_id, image_class


# This function is used to generate a numpy array from an image on which we apply some transformations
# resizing (but actually using its real size), converting to grayscale and increasing the contrast
# and normalize values
def generate_numpy_array(image_path: str) -> np.ndarray:
    image = Image.open(image_path)
    image = image.resize((224, 224))
    image = image.convert("L")  # convert to grayscale
    image = ImageEnhance.Contrast(image).enhance(2)  # Increase the contrast

    return (
        np.asarray(image).astype(np.float64) / 255
    )  # Transform image to numpy array and normalize values


# This function is used to generate the numpy arrays for the train and validation data
# by calling the clean_line and generate_numpy_array functions
# and opening the train_labels.txt and validation_labels.txt files
# as well as reading the images from the data directory
def generate_numpy_arrays_for_train_and_validation():
    data_dir = "data/data/"
    train_txt = "../data/train_labels.txt"
    validation_txt = "../data/validation_labels.txt"

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

    number_of_read_images = 17000
    number_of_last_image = 22149

    for image_id in range(number_of_read_images + 1, number_of_last_image + 1):
        image_path = (
            data_dir + str(image_id).zfill(6) + ".png"
        )  # zfill is used to add leading zeros to the image_id
        test_data.append(generate_numpy_array(image_path))

    # SLICE DATA FOR UNDERSAMPLING
    slice_size = 6000
    train_data_0 = train_data_0[:slice_size]
    train_labels_0 = train_labels_0[:slice_size]

    # Concatenate the lists of numpy arrays of class 0 and class 1 after slicing
    train_data = train_data_0 + train_data_1
    train_labels = train_labels_0 + train_labels_1

    # Transform lists of numpy arrays to numpy arrays
    train_data = np.array(train_data).astype(np.float64)
    train_labels = np.array(train_labels).astype(np.float64)
    validation_data = np.array(validation_data).astype(np.float64)
    validation_labels = np.array(validation_labels).astype(np.float64)
    test_data = np.array(test_data).astype(np.float64)

    # Reshape the numpy arrays to 1D
    train_data = train_data.reshape(train_data.shape[0], -1)
    validation_data = validation_data.reshape(validation_data.shape[0], -1)
    test_data = test_data.reshape(test_data.shape[0], -1)

    return train_data, train_labels, validation_data, validation_labels, test_data


# Function used to write the predicted labels from test images to a CSV file for submission
def write(predicted_labels):
    labels = [int(i) for i in predicted_labels]

    # Create a DataFrame with the predicted labels
    ids = [f"0{i}" for i in range(17001, 22149 + 1)]
    predictions_df = pd.DataFrame({"id": ids, "class": labels})

    # Write the DataFrame to a CSV file
    predictions_df.to_csv("../submission.csv", index=False)


if __name__ == "__main__":
    start_time = time()

    # Read the train and validation data and labels and generate numpy arrays
    (
        train_images,
        train_labels,
        validation_images,
        validation_labels,
        test_images,
    ) = generate_numpy_arrays_for_train_and_validation()

    # Instantiate the model
    model = RandomForestClassifier()
    # Train the model
    model.fit(train_images, train_labels)

    # Print the F1 score
    print(
        f1_score(validation_labels, model.predict(validation_images), average="binary")
    )

    # Predict the labels for the test images
    predicted_labels = model.predict(test_images)
    # Write the predicted labels to a CSV file for submission
    write(predicted_labels)

    # Print the classification report
    print(classification_report(validation_labels, model.predict(validation_images)))

    end_time = time() - start_time
    print(f"------------------- {end_time} seconds -------------------")
