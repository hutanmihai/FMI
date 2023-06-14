from uuid import UUID

import pytest
from fastapi import status
from httpx import AsyncClient

from app.models import Product
from app.settings import settings
from app.tests.utils.asserts import (
    assert_api_error,
    assert_api_path_param_validation_error,
    assert_api_validation_error,
    assert_base_product_response,
    assert_id_did_not_change,
    assert_list_all_products_response,
)
from app.tests.utils.data_generation_tools import (
    generate_id,
    get_random_string_of_length_bigger_than_255,
)
from app.tests.utils.entity_instance import new_product
from app.tests.utils.entity_list_instances import get_all_products
from app.tests.utils.payloads import (
    get_create_product_payload,
    get_update_product_payload,
)

ADMIN_JWT = settings.admin_token


@pytest.mark.asyncio
async def test_get_product_with_valid_id_successfully_returns_product(
    client: AsyncClient,
):
    new_created_product = await new_product()

    expected_status_code = status.HTTP_200_OK
    expected_product = new_created_product

    response = await client.get(
        f"/product/{new_created_product.id}",
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )
    actual_product = Product(**response.json())

    assert response.status_code == expected_status_code
    assert_base_product_response(actual_product, expected_product)


@pytest.mark.asyncio
async def test_get_product_with_invalid_id_returns_error(client: AsyncClient):
    invalid_id = generate_id()

    expected_status_code = status.HTTP_404_NOT_FOUND
    expected_description = "Product not found"

    response = await client.get(
        f"/product/{invalid_id}", headers={"Authorization": f"Bearer {ADMIN_JWT}"}
    )

    assert response.status_code == expected_status_code
    assert_api_error(response.json(), expected_description)


@pytest.mark.asyncio
async def test_get_product_with_invalid_id_type_returns_error(client: AsyncClient):
    invalid_id = "invalid_id"

    expected_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    response = await client.get(
        f"/product/{invalid_id}", headers={"Authorization": f"Bearer {ADMIN_JWT}"}
    )

    assert response.status_code == expected_status_code
    assert_api_path_param_validation_error(response.json(), ["product_id"])


@pytest.mark.asyncio
async def test_get_all_products_successfully_returns_all_products(
    client: AsyncClient,
):
    await new_product()
    await new_product()

    expected_status_code = status.HTTP_200_OK
    expected_products = await get_all_products()

    response = await client.get(
        "/products", headers={"Authorization": f"Bearer {ADMIN_JWT}"}
    )
    actual_products = [Product(**product) for product in response.json()["products"]]

    assert response.status_code == expected_status_code
    assert_list_all_products_response(
        actual_products,
        expected_products,
    )


@pytest.mark.asyncio
async def test_create_product_with_valid_fields_successfully_creates_product(
    client: AsyncClient,
):
    name: str = "test_create_product"
    calories: float = 100.0
    fat: float = 100.0
    carbs: float = 100.0
    protein: float = 100.0
    request_payload = get_create_product_payload(name, calories, fat, protein, carbs)

    expected_status_code = status.HTTP_201_CREATED
    expected_product = Product(
        name=name,
        calories=calories,
        fat=fat,
        protein=protein,
        carbs=carbs,
        upvotes=0,
        downvotes=0,
    )

    response = await client.post(
        "/product",
        json=request_payload,
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )
    actual_product = Product(**response.json())

    assert response.status_code == expected_status_code
    assert_base_product_response(actual_product, expected_product)


@pytest.mark.asyncio
async def test_create_product_with_missing_required_args_returns_error(
    client: AsyncClient,
):
    name: None = None
    calories: None = None
    fat: None = None
    carbs: None = None
    protein: None = None
    request_payload = get_create_product_payload(name, calories, fat, protein, carbs)

    expected_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    expected_breaking_fields = ["name", "calories", "fat", "carbs", "protein"]

    response = await client.post(
        "/product",
        json=request_payload,
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )

    assert response.status_code == expected_status_code
    assert_api_validation_error(response.json(), expected_breaking_fields)


@pytest.mark.asyncio
async def test_create_product_with_invalid_name_returns_error(client: AsyncClient):
    name: str = get_random_string_of_length_bigger_than_255()
    calories: float = 100.0
    fat: float = 100.0
    carbs: float = 100.0
    protein: float = 100.0
    request_payload = get_create_product_payload(name, calories, fat, protein, carbs)

    expected_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    expected_breaking_field = "name"

    response = await client.post(
        "/product",
        json=request_payload,
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )

    assert response.status_code == expected_status_code
    assert_api_validation_error(response.json(), [expected_breaking_field])


@pytest.mark.asyncio
async def test_create_product_with_invalid_types_returns_error(client: AsyncClient):
    name: None = None
    calories: str = "abc"
    fat: str = "abc"
    carbs: str = "abc"
    protein: str = "abc"
    request_payload = get_create_product_payload(name, calories, fat, protein, carbs)

    expected_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    expected_breaking_fields = ["name", "calories", "fat", "carbs", "protein"]

    response = await client.post(
        "/product",
        json=request_payload,
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )

    assert response.status_code == expected_status_code
    assert_api_validation_error(response.json(), expected_breaking_fields)


@pytest.mark.asyncio
async def test_update_product_with_valid_fields_successfully_updates_product(
    client: AsyncClient,
):
    new_created_product = await new_product()
    name: str = "test_update_product"
    calories: float = 100.0
    fat: float = 100.0
    protein: float = 100.0
    carbs: float = 100.0
    upvotes: int = 10
    downvotes: int = 10
    request_payload = get_update_product_payload(
        name, calories, fat, protein, carbs, upvotes, downvotes
    )

    expected_status_code = status.HTTP_200_OK
    expected_product = new_created_product
    expected_product.name = name
    expected_product.calories = calories
    expected_product.fat = fat
    expected_product.protein = protein
    expected_product.carbs = carbs
    expected_product.upvotes = upvotes
    expected_product.downvotes = downvotes

    response = await client.put(
        f"/product/{new_created_product.id}",
        json=request_payload,
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )

    actual_product = Product(**response.json())
    assert response.status_code == expected_status_code
    assert_base_product_response(actual_product, expected_product)
    assert_id_did_not_change(actual_product, expected_product)


@pytest.mark.asyncio
async def test_update_product_with_missing_votes_successfully_updates_product(
    client: AsyncClient,
):
    new_created_product = await new_product()
    name: str = "test_update_product"
    calories: float = 100.0
    fat: float = 100.0
    protein: float = 100.0
    carbs: float = 100.0
    upvotes: None = None
    downvotes: None = None
    request_payload = get_update_product_payload(
        name, calories, fat, protein, carbs, upvotes, downvotes
    )

    expected_status_code = status.HTTP_200_OK
    expected_product = new_created_product
    expected_product.name = name
    expected_product.calories = calories
    expected_product.fat = fat
    expected_product.protein = protein
    expected_product.carbs = carbs

    response = await client.put(
        f"/product/{new_created_product.id}",
        json=request_payload,
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )

    actual_product = Product(**response.json())
    assert response.status_code == expected_status_code
    assert_base_product_response(actual_product, expected_product)
    assert_id_did_not_change(actual_product, expected_product)


@pytest.mark.asyncio
async def test_update_product_with_invalid_name_returns_error(client: AsyncClient):
    new_created_product = await new_product()
    name: str = get_random_string_of_length_bigger_than_255()
    calories: float = 100.0
    fat: float = 100.0
    protein: float = 100.0
    carbs: float = 100.0
    upvotes: int = 10
    downvotes: int = 10
    request_payload = get_update_product_payload(
        name, calories, fat, protein, carbs, upvotes, downvotes
    )

    expected_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    expected_breaking_field = "name"

    response = await client.put(
        f"/product/{new_created_product.id}",
        json=request_payload,
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )

    assert response.status_code == expected_status_code
    assert_api_validation_error(response.json(), [expected_breaking_field])


@pytest.mark.asyncio
async def test_update_product_with_invalid_args_types_returns_error(
    client: AsyncClient,
):
    new_created_product = await new_product()
    name: str = "test_update_product"
    calories: str = "abc"
    fat: str = "abc"
    protein: str = "abc"
    carbs: str = "abc"
    upvotes: str = "abc"
    downvotes: str = "abc"
    request_payload = get_update_product_payload(
        name, calories, fat, protein, carbs, upvotes, downvotes
    )

    expected_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    expected_breaking_fields = [
        "calories",
        "fat",
        "carbs",
        "protein",
        "upvotes",
        "downvotes",
    ]

    response = await client.put(
        f"/product/{new_created_product.id}",
        json=request_payload,
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )

    assert response.status_code == expected_status_code
    assert_api_validation_error(response.json(), expected_breaking_fields)


@pytest.mark.asyncio
async def test_update_product_with_not_existing_product_returns_error(
    client: AsyncClient,
):
    product_id: UUID = generate_id()
    name: str = "test_update_product"
    calories: float = 100.0
    fat: float = 100.0
    protein: float = 100.0
    carbs: float = 100.0
    upvotes: int = 10
    downvotes: int = 10
    request_payload = get_update_product_payload(
        name, calories, fat, protein, carbs, upvotes, downvotes
    )

    expected_status_code = status.HTTP_404_NOT_FOUND
    excpected_description = "Product not found"

    response = await client.put(
        f"/product/{product_id}",
        json=request_payload,
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )

    assert response.status_code == expected_status_code
    assert_api_error(response.json(), excpected_description)


@pytest.mark.asyncio
async def test_delete_product_with_existing_product_successfully_deletes_product(
    client: AsyncClient,
):
    new_created_product = await new_product()

    expected_status_code = status.HTTP_200_OK

    response = await client.delete(
        f"/product/{new_created_product.id}",
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )

    assert response.status_code == expected_status_code
    assert response.json() == {"message": "Product deleted successfully"}


@pytest.mark.asyncio
async def test_delete_product_with_not_existing_product_returns_error(
    client: AsyncClient,
):
    product_id: UUID = generate_id()

    expected_status_code = status.HTTP_404_NOT_FOUND
    excpected_description = "Product not found"

    response = await client.delete(
        f"/product/{product_id}", headers={"Authorization": f"Bearer {ADMIN_JWT}"}
    )

    assert response.status_code == expected_status_code
    assert_api_error(response.json(), excpected_description)
