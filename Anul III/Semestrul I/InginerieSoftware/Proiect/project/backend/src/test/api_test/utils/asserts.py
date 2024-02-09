from httpx import Response


def assert_api_validation_error(response: Response, expected_breaking_fields: list[str]):
    for i, _ in enumerate(expected_breaking_fields):
        assert response["detail"][i]["loc"][0] == "body"
        assert response["detail"][i]["loc"][1] == expected_breaking_fields[i]


def assert_api_error(response: Response, expected_detail: str):
    assert response["detail"] == expected_detail


def assert_api_response(response: dict, expected_response_keys: set[str] | None = None):
    if expected_response_keys is None:
        expected_response_keys = {"image"}
    assert response.keys() == expected_response_keys
