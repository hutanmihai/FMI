from fastapi import status
from fastapi.responses import JSONResponse

from app.apis.schemas.errors_schema import ApiError


# Function that wraps the error response into predefined schema
def generate_api_error_response(status_code: int, detail: str) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content=ApiError(detail=detail).dict(),
    )


# Function that generates error responses for the OpenAPI documentation
def generate_error_responses(*args) -> dict[int, dict[str, str]]:
    error_responses = {}
    for arg in args:
        if arg == status.HTTP_400_BAD_REQUEST:
            description = "Bad Request Error"
        elif arg == status.HTTP_404_NOT_FOUND:
            description = "Not Found Error"
        elif arg == status.HTTP_403_FORBIDDEN:
            description = "Forbidden Error"
        elif arg == status.HTTP_401_UNAUTHORIZED:
            description = "Unauthorized Error"
        error_responses[arg] = {
            "description": description,
            "model": ApiError,
        }

    return error_responses
