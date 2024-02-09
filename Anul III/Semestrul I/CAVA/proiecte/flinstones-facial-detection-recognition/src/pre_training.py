from src.utils.collapse import collapse
from src.utils.generate_positives_negatives import extract_train_and_validation_patches
from src.utils.visualize import visualize_images_with_boxes, visualize_images_with_boxes_and_detections
from src.constants import (
    VALIDATION_IMAGES_PATH,
    VALIDATION_ANNOTATIONS_PATH,
    COLLAPSED_IMAGES_PATH,
    COLLAPSED_ANNOTATIONS_PATH,
)

if __name__ == "__main__":
    # Collapse the images and annotations
    collapse()
    # Extract positives and negatives for training and validation
    extract_train_and_validation_patches()

    # Uncomment to visualize the images with boxes
    # visualize_images_with_boxes(COLLAPSED_IMAGES_PATH, COLLAPSED_ANNOTATIONS_PATH)
    # visualize_images_with_boxes(VALIDATION_IMAGES_PATH, VALIDATION_ANNOTATIONS_PATH)
