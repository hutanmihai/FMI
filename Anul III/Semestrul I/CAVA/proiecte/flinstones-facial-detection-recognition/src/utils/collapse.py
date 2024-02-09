import timeit

from src.constants import (
    COLLAPSED_ANNOTATIONS_PATH,
    TRAIN_IMAGES_PATHS,
    TRAIN_ANNOTATIONS_PATHS,
    COLLAPSED_IMAGES_PATH,
    TRAIN_DATA_PATH,
)
from src.utils.helpers import check_if_dirs_exist
from src.utils.readers import get_annotations
import cv2 as cv


def collapse():
    start_time = timeit.default_timer()
    check_if_dirs_exist([TRAIN_DATA_PATH, COLLAPSED_IMAGES_PATH])
    zipped_paths = zip(TRAIN_ANNOTATIONS_PATHS, TRAIN_IMAGES_PATHS)
    print("Collapsing images and annotations...")
    with open(COLLAPSED_ANNOTATIONS_PATH, "w") as f:
        for i, (annotation_path, images_path) in enumerate(zipped_paths):
            annotations = get_annotations(annotation_path)
            new_annotations = {}
            for image_name, annotation in annotations.items():
                # Index image with new name
                new_image_name = str(i * 1000 + int(image_name.split(".")[0])).zfill(4) + ".jpg"

                # Save image with new name in the collapsed images folder path
                image = cv.imread(str(images_path / image_name))
                cv.imwrite(str(COLLAPSED_IMAGES_PATH / new_image_name), image)

                new_annotations[new_image_name] = annotation

            for image_name, annotation in new_annotations.items():
                for box, character in annotation:
                    f.write(f"{image_name} {box[0]} {box[1]} {box[2]} {box[3]} {character}\n")
    print("-" * 50)
    print("Successfully collapsed images and annotations!")
    print(f"Collapsing took {timeit.default_timer() - start_time} seconds.\n")
