from fastapi import APIRouter
from schemas.health import HealthResponse
from starlette import status

router: APIRouter = APIRouter(tags=["healthcheck"])


@router.get(path="/health", summary="Health Check", status_code=status.HTTP_200_OK, response_model=HealthResponse)
async def health():
    """Health check."""
    return HealthResponse(status_code=status.HTTP_200_OK, message="Application is healthy!")
