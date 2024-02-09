from typing import AsyncGenerator
from unittest.mock import patch

import pytest
import pytest_asyncio
from app import app
from httpx import AsyncClient


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        yield client


@pytest.fixture
def mock_dependencies():
    with patch("apis.image_editing.convert_base64_to_numpy_image") as convert_to_numpy_mock, patch(
        "apis.image_editing.convert_numpy_image_to_base64"
    ) as convert_to_b64_mock, patch("apis.image_editing.blur_image") as blur_mock, patch(
        "apis.image_editing.remove_object"
    ) as remove_object_mock, patch(
        "apis.image_editing.remove_background"
    ) as remove_background_mock, patch(
        "apis.image_editing.validate_image_base64"
    ) as validate_image_mock, patch(
        "apis.image_editing.image_response"
    ) as image_response_mock, patch(
        "apis.image_editing.process_prefix"
    ) as process_prefix_mock:
        yield {
            "convert_to_numpy_mock": convert_to_numpy_mock,
            "convert_to_b64_mock": convert_to_b64_mock,
            "blur_mock": blur_mock,
            "remove_object_mock": remove_object_mock,
            "remove_background_mock": remove_background_mock,
            "validate_image_mock": validate_image_mock,
            "image_response_mock": image_response_mock,
            "process_prefix_mock": process_prefix_mock,
        }
