from typing import List

from app.models import BaseModel, Product, User


def assert_api_validation_error(content: dict, expected_breaking_fields: List[str]):
    for i, _ in enumerate(expected_breaking_fields):
        assert content["detail"][i]["loc"][0] == "body"
        assert content["detail"][i]["loc"][1] == expected_breaking_fields[i]


def assert_api_path_param_validation_error(
    content: dict, expected_breaking_fields: List[str]
):
    for i, _ in enumerate(expected_breaking_fields):
        assert content["detail"][i]["loc"][0] == "path"
        assert content["detail"][i]["loc"][1] == expected_breaking_fields[i]


def assert_api_error(content: dict, expected_description: str):
    assert content["detail"] == expected_description


def assert_http_exception_error(content: dict, expected_detail: str):
    assert content["detail"] == expected_detail


def assert_base_product_response(actual_product: Product, expected_product: Product):
    assert actual_product.id is not None
    assert actual_product.name == expected_product.name
    assert actual_product.calories == expected_product.calories
    assert actual_product.fat == expected_product.fat
    assert actual_product.carbs == expected_product.carbs
    assert actual_product.protein == expected_product.protein
    assert actual_product.upvotes == expected_product.upvotes
    assert actual_product.downvotes == expected_product.downvotes


def assert_base_user_response(actual_user: User, expected_user: User):
    assert actual_user.id is not None
    assert actual_user.g_id == expected_user.g_id
    assert actual_user.name == expected_user.name
    assert actual_user.email == expected_user.email
    assert actual_user.picture == expected_user.picture
    assert actual_user.pref_height_metric == expected_user.pref_height_metric
    assert actual_user.height == expected_user.height
    assert actual_user.pref_weight_metric == expected_user.pref_weight_metric
    assert actual_user.weight == expected_user.weight
    assert actual_user.target_weight == expected_user.target_weight
    assert actual_user.target_calories == expected_user.target_calories


def assert_list_all_products_response(
    actual_products: List[Product], expected_products: List[Product]
):
    assert actual_products is not None
    assert len(actual_products) == len(expected_products)

    for actual_product, expected_product in zip(actual_products, expected_products):
        assert actual_product.id is not None
        assert actual_product.name == expected_product.name
        assert actual_product.calories == expected_product.calories
        assert actual_product.fat == expected_product.fat
        assert actual_product.carbs == expected_product.carbs
        assert actual_product.protein == expected_product.protein
        assert actual_product.upvotes == expected_product.upvotes
        assert actual_product.downvotes == expected_product.downvotes


def assert_list_all_users_response(
    actual_users: List[User], expected_users: List[User]
):
    assert actual_users is not None
    assert len(actual_users) == len(expected_users)

    for actual_user, expected_user in zip(actual_users, expected_users):
        assert actual_user.id is not None
        assert actual_user.g_id == expected_user.g_id
        assert actual_user.name == expected_user.name
        assert actual_user.email == expected_user.email
        assert actual_user.picture == expected_user.picture
        assert actual_user.pref_height_metric == expected_user.pref_height_metric
        assert actual_user.height == expected_user.height
        assert actual_user.pref_weight_metric == expected_user.pref_weight_metric
        assert actual_user.weight == expected_user.weight
        assert actual_user.target_weight == expected_user.target_weight
        assert actual_user.target_calories == expected_user.target_calories


def assert_id_did_not_change(actual: BaseModel, expected: BaseModel):
    assert actual.id == str(expected.id)
