import pytest
from fastapi import status
from httpx import AsyncClient

HEALTH_URL = "/health"

EXPECTED_HEALTHY_RESPONSE = "Application is healthy"


@pytest.mark.asyncio
async def test_health(client: AsyncClient):
    expected_status_code = status.HTTP_200_OK
    expected_response = EXPECTED_HEALTHY_RESPONSE

    response = await client.get(HEALTH_URL)

    assert response.status_code == expected_status_code
    assert response.json() == expected_response
