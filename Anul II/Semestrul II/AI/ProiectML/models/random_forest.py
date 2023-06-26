import numpy as np
from time import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, classification_report
from utils.write import write

if __name__ == "__main__":
    start_time = time()

    train_images = np.load("../numpy_data/train_data.npy")
    train_labels = np.load("../numpy_data/train_labels.npy")
    validation_images = np.load("../numpy_data/validation_data.npy")
    validation_labels = np.load("../numpy_data/validation_labels.npy")
    test_images = np.load("../numpy_data/test_data.npy")

    model = RandomForestClassifier()
    model.fit(train_images, train_labels)

    print(
        f1_score(validation_labels, model.predict(validation_images), average="binary")
    )

    predicted_labels = model.predict(test_images)
    write(predicted_labels)

    end_time = time() - start_time
    print(f"------------------- {end_time} seconds -------------------")

    print(classification_report(validation_labels, model.predict(validation_images)))
