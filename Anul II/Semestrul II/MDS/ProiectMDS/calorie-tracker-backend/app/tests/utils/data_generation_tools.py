from random import choice as random_choice
from random import randint, random
from string import ascii_lowercase
from uuid import uuid4

from app.apis.utils.enums import HeightMetric, WeightMetric
from app.models import Product, User


def generate_random_string(length: int):
    return "".join(random_choice(ascii_lowercase) for i in range(length))


def get_random_string_of_length_bigger_than_255():
    return generate_random_string(256)


def get_random_float():
    return random() * 10


def get_g_id():
    g_id: str = ""
    for _ in range(20):
        x = randint(0, 9)
        g_id += str(x)
    return g_id


def get_random_int():
    return randint(0, 10)


def generate_id():
    return str(uuid4())


def get_random_email():
    return generate_random_string(15) + "@email.com"


def get_random_name():
    return generate_random_string(15)


def get_product_instance():
    product = Product()
    product.id = generate_id()
    product.name = get_random_name()
    product.calories = get_random_float()
    product.fat = get_random_float()
    product.protein = get_random_float()
    product.carbs = get_random_float()
    product.upvotes = get_random_int()
    product.downvotes = get_random_int()
    return product


def get_user_instance():
    user = User()
    user.id = generate_id()
    user.g_id = get_g_id()
    user.email = get_random_email()
    user.name = get_random_name()
    user.picture = None
    user.pref_height_metric = HeightMetric.cm if random() < 0.5 else HeightMetric.feet
    user.height = get_random_float()
    user.pref_weight_metric = WeightMetric.kg if random() < 0.5 else WeightMetric.lbs
    user.weight = get_random_float()
    user.target_weight = get_random_float()
    user.target_calories = get_random_int()
    return user
