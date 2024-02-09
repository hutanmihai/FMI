from test.api_test.utils.asserts import assert_api_error, assert_api_response, assert_api_validation_error
from test.api_test.utils.data_generation import (
    get_int_inside_of_range,
    get_negative_int,
    get_random_accepted_blur_type,
    get_random_image_base64,
    get_random_string,
)
from test.api_test.utils.payloads import get_blur_image_payload

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_blur_image_successfully(client: AsyncClient):
    image: str = get_random_image_base64()
    value: int = get_int_inside_of_range()
    type: str = get_random_accepted_blur_type()

    payload = await get_blur_image_payload(image, value, type)

    response = await client.post("/blur", json=payload)

    assert response.status_code == 200
    assert_api_response(response.json())


@pytest.mark.asyncio
async def test_blur_image_unsuccesfully_invalid_image(client: AsyncClient):
    image: str = get_random_string()
    value: int = get_int_inside_of_range()
    type: str = get_random_accepted_blur_type()

    payload = await get_blur_image_payload(image, value, type)

    response = await client.post("/blur", json=payload)

    assert response.status_code == 400
    assert_api_error(response.json(), "Invalid Image")


@pytest.mark.asyncio
async def test_blur_image_unsuccesfully_invalid_fields_except_image(client: AsyncClient):
    image: str = get_random_image_base64()
    value: int = get_negative_int()
    type: str = get_random_string()

    payload = await get_blur_image_payload(image, value, type)

    expected_breaking_fields = ["value", "type"]

    response = await client.post("/blur", json=payload)

    assert response.status_code == 422
    assert_api_validation_error(response.json(), expected_breaking_fields)


@pytest.mark.asyncio
async def test_blur_image_unsuccesfully_missing_required_fields_except_image(client: AsyncClient):
    image: str = get_random_image_base64()

    payload = await get_blur_image_payload(image)

    expected_breaking_fields = ["value", "type"]

    response = await client.post("/blur", json=payload)

    assert response.status_code == 422
    assert_api_validation_error(response.json(), expected_breaking_fields)
