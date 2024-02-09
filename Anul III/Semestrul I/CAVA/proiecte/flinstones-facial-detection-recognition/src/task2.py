import argparse

import numpy as np
import cv2 as cv
import torch
from torchvision.transforms import transforms

from src.constants import (
    SOLUTION_DETECTIONS_PATH,
    SOLUTION_FILE_NAMES_PATH,
    VALIDATION_IMAGES_PATH,
    MODEL_PATH,
    LABELS_MAP,
    SOLUTION_DETECTIONS_BARNEY_PATH,
    SOLUTION_SCORES_BARNEY_PATH,
    SOLUTION_FILE_NAMES_BARNEY_PATH,
    SOLUTION_DETECTIONS_BETTY_PATH,
    SOLUTION_SCORES_BETTY_PATH,
    SOLUTION_FILE_NAMES_BETTY_PATH,
    SOLUTION_DETECTIONS_FRED_PATH,
    SOLUTION_SCORES_FRED_PATH,
    SOLUTION_FILE_NAMES_FRED_PATH,
    SOLUTION_DETECTIONS_WILMA_PATH,
    SOLUTION_SCORES_WILMA_PATH,
    SOLUTION_FILE_NAMES_WILMA_PATH,
    TEST_IMAGES_PATH,
    WINDOW_SIZE,
)


def run_task2_cnn(is_test: bool = False):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = torch.load(MODEL_PATH / "best_task2.pth")
    model.to(device)
    model.eval()

    detections = np.load(SOLUTION_DETECTIONS_PATH)
    file_names = np.load(SOLUTION_FILE_NAMES_PATH)

    if is_test:
        print("Running in test mode!")
        images_path = TEST_IMAGES_PATH
    else:
        print("Running in validation mode!")
        images_path = VALIDATION_IMAGES_PATH

    solutions = {
        "barney": [np.array([]), np.array([]), np.array([])],
        "betty": [np.array([]), np.array([]), np.array([])],
        "fred": [np.array([]), np.array([]), np.array([])],
        "wilma": [np.array([]), np.array([]), np.array([])],
    }

    for file_name, detection in zip(file_names, detections):
        image = cv.imread(str(images_path / file_name))
        cropped_box = cv.resize(
            image[detection[1] : detection[3], detection[0] : detection[2]], (WINDOW_SIZE, WINDOW_SIZE)
        )
        cropped_box = cv.cvtColor(cropped_box, cv.COLOR_BGR2RGB)
        tensor = transforms.ToTensor()(cropped_box).unsqueeze(0).to(device)
        with torch.no_grad():
            output = model(tensor)
            predicted = torch.argmax(output).item()
        score = output[0][predicted].item()
        character = list(LABELS_MAP.keys())[list(LABELS_MAP.values()).index(predicted)]

        print(f"Predicted: {character} with score: {score}")

        if character != "unknown":
            solutions[character][0] = np.append(solutions[character][0], np.array(detection))
            solutions[character][1] = np.append(solutions[character][1], score)
            solutions[character][2] = np.append(solutions[character][2], file_name)

    for character in solutions.keys():
        solutions[character][0] = solutions[character][0].reshape(-1, 4).astype(np.int32)
        if character == "unknown":
            continue
        if character == "barney":
            np.save(SOLUTION_DETECTIONS_BARNEY_PATH, solutions[character][0])
            np.save(SOLUTION_SCORES_BARNEY_PATH, solutions[character][1])
            np.save(SOLUTION_FILE_NAMES_BARNEY_PATH, solutions[character][2])
        elif character == "betty":
            np.save(SOLUTION_DETECTIONS_BETTY_PATH, solutions[character][0])
            np.save(SOLUTION_SCORES_BETTY_PATH, solutions[character][1])
            np.save(SOLUTION_FILE_NAMES_BETTY_PATH, solutions[character][2])
        elif character == "fred":
            np.save(SOLUTION_DETECTIONS_FRED_PATH, solutions[character][0])
            np.save(SOLUTION_SCORES_FRED_PATH, solutions[character][1])
            np.save(SOLUTION_FILE_NAMES_FRED_PATH, solutions[character][2])
        elif character == "wilma":
            np.save(SOLUTION_DETECTIONS_WILMA_PATH, solutions[character][0])
            np.save(SOLUTION_SCORES_WILMA_PATH, solutions[character][1])
            np.save(SOLUTION_FILE_NAMES_WILMA_PATH, solutions[character][2])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="Flag to run in test mode")
    args = parser.parse_args()
    is_test = args.test

    run_task2_cnn(is_test)
