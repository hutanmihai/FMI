import timeit
import argparse

import cv2 as cv
import numpy as np
import torch
from torchvision.transforms import transforms

from src.constants import (
    THRESHOLD,
    WINDOW_SIZE,
    MODEL_PATH,
    IMAGE_HEIGHT,
    SOLUTION_DETECTIONS_PATH,
    SOLUTION_SCORES_PATH,
    SOLUTION_FILE_NAMES_PATH,
    VALIDATION_IMAGES_PATH,
    TEST_IMAGES_PATH,
    IMAGE_WIDTH,
)
from src.utils.helpers import non_maximal_suppression, write_solution
from src.utils.readers import get_images
from skimage.transform import resize


def run_task1_cnn(is_test: bool = False):
    big_start_time = timeit.default_timer()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = torch.load(MODEL_PATH / "best_task1.pth")
    model.to(device)
    model.eval()

    # Initialize the scales that we will use to resize the image
    SCALES = [0.9, 0.5, 0.3]

    # Load the validation images
    if is_test:
        print("Running in test mode!")
        imgs = get_images(TEST_IMAGES_PATH)
    else:
        print("Running in validation mode!")
        imgs = get_images(VALIDATION_IMAGES_PATH)

    imgs = [cv.cvtColor(image, cv.COLOR_BGR2GRAY) for image in imgs]

    # Initialize the detections, scores and file names
    detections = None
    scores = np.array([])
    file_names = np.array([])

    for i, image in enumerate(imgs):
        start_time = timeit.default_timer()
        print(f"Processing image {i + 1}/{len(imgs)}...")
        image_scores = []
        image_detections = []
        image_name = str(i + 1).zfill(4) + ".jpg"

        for scale in SCALES:
            if scale * IMAGE_HEIGHT < WINDOW_SIZE:
                break

            # Resize the image
            resized_image = resize(image, [IMAGE_HEIGHT * scale, IMAGE_WIDTH * scale])

            NUM_COLS = resized_image.shape[1] - WINDOW_SIZE - 1
            NUM_ROWS = resized_image.shape[0] - WINDOW_SIZE - 1

            for y in range(0, NUM_ROWS, 2):
                for x in range(0, NUM_COLS, 2):
                    resized_patch = resized_image[y : y + WINDOW_SIZE, x : x + WINDOW_SIZE]
                    window_tensor = transforms.ToTensor()(resized_patch).unsqueeze(0).to(device)
                    window_tensor = window_tensor.to(torch.float32)
                    with torch.no_grad():
                        pred = model(window_tensor)
                        score = pred[0][0].item()

                    if score > THRESHOLD:
                        x_min = int(x / scale)
                        y_min = int(y / scale)
                        x_max = int((x + WINDOW_SIZE) / scale)
                        y_max = int((y + WINDOW_SIZE) / scale)
                        image_detections.append([x_min, y_min, x_max, y_max])
                        image_scores.append(score)

        if len(image_scores) > 0:
            image_detections, image_scores = non_maximal_suppression(np.array(image_detections), np.array(image_scores))
        if len(image_scores) > 0:
            if detections is None:
                detections = image_detections
            else:
                detections = np.concatenate((detections, image_detections))
            scores = np.append(scores, image_scores)
            file_names = np.append(file_names, np.repeat(image_name, len(image_scores)))

        end_time = timeit.default_timer()
        print(f"Process time for {i + 1}/{len(imgs)} was {end_time - start_time} seconds.")

    write_solution(
        detections,
        SOLUTION_DETECTIONS_PATH,
        scores,
        SOLUTION_SCORES_PATH,
        file_names,
        SOLUTION_FILE_NAMES_PATH,
    )

    print(f"Total time: {timeit.default_timer() - big_start_time} seconds.\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true", help="Flag to run in test mode")
    args = parser.parse_args()

    is_test = args.test
    run_task1_cnn(is_test)
