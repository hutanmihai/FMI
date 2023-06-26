import os
from time import time

import keras.backend as kb
import numpy as np
import pandas as pd
from keras.callbacks import (
    ReduceLROnPlateau,
    EarlyStopping,
    TensorBoard,
    ModelCheckpoint,
)
from keras.layers import (
    Dense,
    Dropout,
    Flatten,
    Conv2D,
    MaxPooling2D,
    BatchNormalization,
    ReLU,
)
from keras.losses import binary_crossentropy
from keras.models import Sequential
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report
from sklearn.utils import class_weight

# CONSTANTS
DATA_DIR_PATH = os.path.join(os.getcwd(), "data/data/")
BATCH_SIZE = 32
IMAGE_SIZE = (224, 224)


# This function was in a different module locally and ran only one time for easier and faster reading in my iterations
def generate_dataframes():
    train_labels_file = "data/train_labels.txt"
    train_df = pd.read_csv(train_labels_file, header=0, names=["id", "class"], sep=",")
    train_df["id"] = train_df["id"].astype(str)
    train_df["class"] = train_df["class"].astype(str)

    validation_labels_file = "data/validation_labels.txt"
    validation_df = pd.read_csv(
        validation_labels_file, header=0, names=["id", "class"], sep=","
    )
    validation_df["id"] = validation_df["id"].astype(str)
    validation_df["class"] = validation_df["class"].astype(str)

    train_df["id"] = train_df["id"].apply(lambda x: str(x).zfill(6) + ".png")
    validation_df["id"] = validation_df["id"].apply(lambda x: str(x).zfill(6) + ".png")

    test_dataframe = pd.DataFrame()
    test_dataframe["id"] = [str(i).zfill(6) + ".png" for i in range(17001, 22149 + 1)]

    train_df.to_csv(
        "../data_frames/train_dataframe.csv",
        index=False,
        header=False,
        columns=["id", "class"],
    )
    validation_df.to_csv(
        "../data_frames/validation_dataframe.csv",
        index=False,
        header=False,
        columns=["id", "class"],
    )
    test_dataframe.to_csv(
        "../data_frames/test_dataframe.csv", index=False, header=False, columns=["id"]
    )


# Read dataframes which contain the image namefiles and their labels
def read_dataframes():
    test_dataframe = pd.read_csv(
        "data_frames/test_dataframe.csv", sep=",", names=["id"]
    ).astype(str)
    validation_dataframe = pd.read_csv(
        "data_frames/validation_dataframe.csv", sep=",", names=["id", "class"]
    ).astype(str)
    train_dataframe = pd.read_csv(
        "data_frames/train_dataframe.csv", sep=",", names=["id", "class"]
    ).astype(str)
    return test_dataframe, validation_dataframe, train_dataframe


# The data is unbalanced, so we calculate the class weights to use them in training
def calculate_class_weights():
    train = train_dataframe["class"].values
    class_weights = class_weight.compute_class_weight(
        class_weight="balanced", classes=np.unique(train), y=train
    )
    class_weights = {0: class_weights[0], 1: class_weights[1]}
    print(class_weights)
    return class_weights


# DATA GENERATORS
def create_generators():
    # Augment data using ImageDataGenerator parameters
    train_data_gen = ImageDataGenerator(
        rescale=1.0 / 255.0,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.1,
        rotation_range=15,
        fill_mode="nearest",
        horizontal_flip=True,
    )

    validation_data_gen = ImageDataGenerator(rescale=1.0 / 255.0)

    test_data_gen = ImageDataGenerator(rescale=1.0 / 255.0)

    # Create generators from dataframes and the directory where the images are
    # Convert them to grayscale and get them in batches of 32
    train_generator = train_data_gen.flow_from_dataframe(
        dataframe=train_dataframe,
        directory=DATA_DIR_PATH,
        x_col="id",
        y_col="class",
        target_size=IMAGE_SIZE,
        color_mode="grayscale",
        batch_size=BATCH_SIZE,
        class_mode="binary",
        shuffle=True,
    )

    validation_generator = validation_data_gen.flow_from_dataframe(
        dataframe=validation_dataframe,
        directory=DATA_DIR_PATH,
        x_col="id",
        y_col="class",
        target_size=IMAGE_SIZE,
        color_mode="grayscale",
        batch_size=BATCH_SIZE,
        class_mode="binary",
        shuffle=False,
    )

    test_generator = test_data_gen.flow_from_dataframe(
        dataframe=test_dataframe,
        directory=DATA_DIR_PATH,
        x_col="id",
        y_col=None,
        target_size=IMAGE_SIZE,
        color_mode="grayscale",
        batch_size=BATCH_SIZE,
        class_mode=None,
        shuffle=False,
    )

    return train_generator, validation_generator, test_generator


# F1 Score function to use in metrics during training for visualization
def score(actual_values, predictions):
    prod = actual_values * predictions
    # True positives
    tp = kb.sum(kb.round(prod))
    # False positives
    fp = kb.sum(kb.round((1 - actual_values) * predictions))
    # False negatives
    fn = kb.sum(kb.round((actual_values * (1 - predictions))))
    # Precision
    precision = tp / (tp + fp + 1e-9)  # 1e-9 to avoid division by zero
    # Recall
    recall = tp / (tp + fn + 1e-9)  # 1e-9 to avoid division by zero
    # F1 Score
    f1_val = (
        2 * (precision * recall) / (precision + recall + 1e-9)
    )  # 1e-9 to avoid division by zero
    return f1_val


# Callbacks used in training
def generate_callbacks():
    # Reduce learning rate after patience epochs of no improvement in loss
    learn_rate = ReduceLROnPlateau(
        monitor="loss",
        factor=0.5,
        patience=5,
        verbose=1,
        mode="auto",
        min_delta=1e-7,
        cooldown=1,
        min_lr=1e-7,
    )

    # Prevent overfitting by stopping training and restoring best weights
    early_stop = EarlyStopping(
        monitor="val_score",
        min_delta=1e-4,
        patience=60,
        verbose=1,
        mode="max",
        baseline=None,
        restore_best_weights=True,
    )

    # Visualize plots in real time while training
    tensorboard = TensorBoard(log_dir=f"logs/{time()}")

    # Save model after each epoch
    checkpoint_path = "saved_models/model_weights.{epoch:02d}.h5"
    checkpoint = ModelCheckpoint(checkpoint_path, verbose=0)
    return learn_rate, early_stop, tensorboard, checkpoint


# CNN Model
def create_model():
    dropout = 0.2
    kernel_size = 3
    model = Sequential(
        [
            Conv2D(
                filters=32,
                kernel_size=kernel_size,
                padding="same",
                input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 1),
            ),
            BatchNormalization(),
            ReLU(),
            Conv2D(filters=32, kernel_size=kernel_size, padding="same"),
            BatchNormalization(),
            ReLU(),
            MaxPooling2D(),
            Dropout(dropout),
            Conv2D(filters=64, kernel_size=kernel_size, padding="same"),
            BatchNormalization(),
            ReLU(),
            Conv2D(filters=64, kernel_size=kernel_size, padding="same"),
            BatchNormalization(),
            ReLU(),
            MaxPooling2D(),
            Dropout(dropout),
            Conv2D(filters=128, kernel_size=kernel_size, padding="same"),
            BatchNormalization(),
            ReLU(),
            Conv2D(filters=128, kernel_size=kernel_size, padding="same"),
            BatchNormalization(),
            ReLU(),
            Conv2D(filters=128, kernel_size=kernel_size, padding="same"),
            BatchNormalization(),
            ReLU(),
            MaxPooling2D(),
            Dropout(dropout),
            Conv2D(filters=256, kernel_size=kernel_size, padding="same"),
            BatchNormalization(),
            ReLU(),
            Conv2D(filters=256, kernel_size=kernel_size, padding="same"),
            BatchNormalization(),
            ReLU(),
            Conv2D(filters=256, kernel_size=kernel_size, padding="same"),
            BatchNormalization(),
            ReLU(),
            MaxPooling2D(),
            Dropout(dropout),
            Flatten(),
            Dense(256),
            ReLU(),
            BatchNormalization(),
            Dense(256),
            ReLU(),
            BatchNormalization(),
            Dense(1, activation="sigmoid"),
        ]
    )
    print(model.summary())
    return model


# Function used to write the predicted labels from test images to a CSV file for submission
def write(predicted_labels):
    labels = [int(i) for i in predicted_labels]

    # Create a DataFrame with the predicted labels
    ids = [f"0{i}" for i in range(17001, 22149 + 1)]
    predictions_df = pd.DataFrame({"id": ids, "class": labels})

    # Write the DataFrame to a CSV file
    predictions_df.to_csv("../submission.csv", index=False)


if __name__ == "__main__":
    generate_dataframes()
    test_dataframe, validation_dataframe, train_dataframe = read_dataframes()
    train_generator, validation_generator, test_generator = create_generators()
    learn_rate, early_stop, tensorboard, checkpoint = generate_callbacks()
    model = create_model()

    # Compile the model
    model.compile(
        optimizer=Adam(learning_rate=0.001), loss=binary_crossentropy, metrics=[score]
    )

    start = time()

    # Train model
    model.fit(
        train_generator,
        epochs=500,
        batch_size=BATCH_SIZE,
        verbose=1,
        validation_data=validation_generator,
        class_weight=calculate_class_weights(),
        callbacks=[early_stop, tensorboard, learn_rate, checkpoint],
    )

    print(f"--------------------------- {time() - start} ---------------------------")

    # Prediction and classification report for validation data
    val_predicted_labels = model.predict(validation_generator, verbose=1)
    val_predicted_labels = (
        np.round(val_predicted_labels)
        .astype(int)
        .reshape(
            -1,
        )
    )
    val_classes = validation_generator.classes
    print(classification_report(val_classes, val_predicted_labels))

    # Predict and write in submission.csv test data labels
    predicted_labels = model.predict(test_generator, verbose=1)
    predicted_labels = (
        np.round(predicted_labels)
        .astype(int)
        .reshape(
            -1,
        )
    )

    write(predicted_labels)

    print(f"-----------------------------------------------------")
