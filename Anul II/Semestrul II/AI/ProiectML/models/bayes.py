import numpy as np
from sklearn.naive_bayes import CategoricalNB
from time import time
from sklearn import preprocessing
from sklearn.metrics import f1_score
from utils.write import write

if __name__ == "__main__":
    start_time = time()

    train_images = np.load("../numpy_data/train_data.npy")
    train_labels = np.load("../numpy_data/train_labels.npy")
    validation_images = np.load("../numpy_data/validation_data.npy")
    validation_labels = np.load("../numpy_data/validation_labels.npy")
    test_images = np.load("../numpy_data/test_data.npy")

    scaler = preprocessing.StandardScaler()
    scaler.fit(train_images)
    train_images = scaler.transform(train_images)
    validation_images = scaler.transform(validation_images)
    test_images = scaler.transform(test_images)

    bins = np.linspace(start=0, stop=255, num=3)
    train_images_bins = np.digitize(train_images, bins)
    validation_images_bins = np.digitize(validation_images, bins)
    test_images_bins = np.digitize(test_images, bins)

    model = CategoricalNB()
    model.fit(train_images_bins, train_labels)

    print(
        f1_score(
            validation_labels, model.predict(validation_images_bins), average="binary"
        )
    )

    predicted_labels = model.predict(test_images_bins)
    write(predicted_labels)

    end_time = time() - start_time
    print(f"------------------- {end_time} seconds -------------------")
