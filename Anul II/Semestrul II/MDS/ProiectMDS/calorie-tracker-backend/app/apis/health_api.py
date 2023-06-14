from fastapi import APIRouter, Depends, status
from fastapi.responses import PlainTextResponse

from app.services.health_srv import HealthSrv

router: APIRouter = APIRouter(tags=["healthcheck"])

HEALTHY_RESPONSE: str = "Application is healthy"
UNHEALTHY_RESPONSE: str = "Application is unhealthy"


@router.get("/health", summary="Health check", status_code=status.HTTP_200_OK)
async def health(
    health_srv: HealthSrv = Depends(HealthSrv),
    response: PlainTextResponse = PlainTextResponse(),
) -> PlainTextResponse:
    if await health_srv.is_healthy():
        response.status_code = status.HTTP_200_OK
        response: str = HEALTHY_RESPONSE
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        response: str = UNHEALTHY_RESPONSE
    return response
