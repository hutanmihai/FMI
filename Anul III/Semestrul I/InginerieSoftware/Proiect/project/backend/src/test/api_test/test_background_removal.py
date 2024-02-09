from test.api_test.utils.asserts import assert_api_error, assert_api_response
from test.api_test.utils.data_generation import get_random_image_base64, get_random_string
from test.api_test.utils.payloads import get_background_removal_payload

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_remove_background_successfully(client: AsyncClient):
    image: str = get_random_image_base64()

    payload = await get_background_removal_payload(image)

    response = await client.post("/background-removal", json=payload)

    assert response.status_code == 200
    assert_api_response(response.json())


@pytest.mark.asyncio
async def test_remove_background_unsuccesfully_invalid_image(client: AsyncClient):
    image: str = get_random_string()

    payload = await get_background_removal_payload(image)

    response = await client.post("/background-removal", json=payload)

    assert response.status_code == 400
    assert_api_error(response.json(), "Invalid Image")
