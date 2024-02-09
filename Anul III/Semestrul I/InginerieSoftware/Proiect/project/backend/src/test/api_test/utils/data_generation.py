from random import choice, randint
from test.api_test.constants import ACCEPTED_IMAGE_VALUES


def get_random_image_base64() -> str:
    return choice(ACCEPTED_IMAGE_VALUES)


def get_random_string() -> str:
    return "".join(choice("abcdefghijklmnopqrstuvwxyz") for _ in range(10))


def get_int_inside_of_range(range: tuple[int, int] = (0, 100)) -> int:
    return randint(range[0], range[1])


def get_negative_int() -> int:
    return randint(-100, -1)


def get_positive_int() -> int:
    return randint(1, 100)


def get_random_accepted_blur_type() -> str:
    return choice(["gaussian", "median", "bilateral", "blur"])
