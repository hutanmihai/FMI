from test.api_test.utils.asserts import assert_api_error, assert_api_response, assert_api_validation_error
from test.api_test.utils.data_generation import (
    get_int_inside_of_range,
    get_negative_int,
    get_positive_int,
    get_random_image_base64,
    get_random_string,
)
from test.api_test.utils.payloads import get_object_removal_payload

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_remove_object_successfully(client: AsyncClient):
    image: str = get_random_image_base64()
    x0: int = 0
    y0: int = 0
    width: int = 0
    height: int = 0

    payload = await get_object_removal_payload(image, x0, y0, width, height)

    response = await client.post("/object-removal", json=payload)

    assert response.status_code == 200
    assert_api_response(response.json())


@pytest.mark.asyncio
async def test_remove_object_unsuccesfully_invalid_image(client: AsyncClient):
    image: str = get_random_string()
    x0: int = get_int_inside_of_range()
    y0: int = get_int_inside_of_range()
    width: int = get_positive_int()
    height: int = get_positive_int()

    payload = await get_object_removal_payload(image, x0, y0, width, height)

    response = await client.post("/object-removal", json=payload)

    assert response.status_code == 400
    assert_api_error(response.json(), "Invalid Image")


@pytest.mark.asyncio
async def test_remove_object_unsuccesfully_invalid_fields_except_image(client: AsyncClient):
    image: str = get_random_image_base64()
    x0: int = get_negative_int()
    y0: int = get_negative_int()
    width: int = get_negative_int()
    height: int = get_negative_int()

    payload = await get_object_removal_payload(image, x0, y0, width, height)

    expected_breaking_fields = ["x0", "y0", "width", "height"]

    response = await client.post("/object-removal", json=payload)

    assert response.status_code == 422
    assert_api_validation_error(response.json(), expected_breaking_fields)


@pytest.mark.asyncio
async def test_remove_object_unsuccesfully_missing_required_fields_except_image(client: AsyncClient):
    image: str = get_random_image_base64()

    payload = await get_object_removal_payload(image)

    expected_breaking_fields = ["x0", "y0", "width", "height"]

    response = await client.post("/object-removal", json=payload)

    assert response.status_code == 422
    assert_api_validation_error(response.json(), expected_breaking_fields)
