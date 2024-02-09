import numpy as np
import pytest

from schemas.image_editing import BlurImagePayload
from test.unit_test.constants import ACCEPTED_IMAGE_VALUES
from apis.image_editing import blur


@pytest.mark.asyncio
async def test_blur_endpoint(mock_dependencies):
    # Mocking the payload
    mock_blur_type = "gaussian"
    mock_blur_value = 50
    mock_prefix = "data:image/png;base64"
    mock_image_type = "png"
    mock_base64_image = ACCEPTED_IMAGE_VALUES[0]
    mock_numpy_image = np.ones((10, 10, 3), dtype=np.uint8)
    mock_payload = BlurImagePayload(image=mock_base64_image, type=mock_blur_type, value=mock_blur_value)

    # Setting up mocks and expected behavior
    mock_dependencies["validate_image_mock"].return_value = True
    mock_dependencies["process_prefix_mock"].return_value = (mock_base64_image, mock_image_type, mock_prefix)
    mock_dependencies["convert_to_numpy_mock"].return_value = mock_numpy_image
    mock_dependencies["blur_mock"].return_value = mock_numpy_image
    mock_dependencies["convert_to_b64_mock"].return_value = mock_base64_image
    mock_dependencies["image_response_mock"].return_value = mock_base64_image

    # Calling the endpoint
    result = await blur(mock_payload)

    # Assertions
    assert result == mock_base64_image
    mock_dependencies["validate_image_mock"].assert_called_once_with(mock_payload.image)
    mock_dependencies["process_prefix_mock"].assert_called_once_with(mock_payload.image)
    mock_dependencies["convert_to_numpy_mock"].assert_called_once_with(mock_base64_image)
    assert np.array_equal(mock_dependencies["blur_mock"].call_args[0][0], mock_numpy_image)
    assert mock_dependencies["blur_mock"].call_args[0][1] == mock_blur_type
    assert mock_dependencies["blur_mock"].call_args[0][2] == mock_blur_value

    assert np.array_equal(
        mock_dependencies["convert_to_b64_mock"].call_args[0][0], mock_dependencies["blur_mock"].return_value
    )
    mock_dependencies["image_response_mock"].assert_called_once_with(mock_base64_image, mock_prefix)
