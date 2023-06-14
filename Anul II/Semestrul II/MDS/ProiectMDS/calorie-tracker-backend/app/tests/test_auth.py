from datetime import datetime, timedelta

import pytest
from fastapi import status
from httpx import AsyncClient
from jwt import encode

from app.settings import settings
from app.tests.utils.data_generation_tools import generate_id
from app.tests.utils.entity_instance import new_user


@pytest.mark.asyncio
async def test_valid_jwt_return_works(client: AsyncClient):
    new_created_user, jwt = await new_user()

    expected_status_code = status.HTTP_200_OK
    expected_response = {
        "message": f"Hello {new_created_user.name} from a protected endpoint!"
    }

    response = await client.get(
        "/protected",
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == expected_status_code
    assert response.json() == expected_response


@pytest.mark.asyncio
async def test_valid_jwt_admin_works(client: AsyncClient):
    jwt = settings.admin_token

    expected_status_code = status.HTTP_200_OK
    expected_response = {"message": "Hello ADMIN from a protected endpoint!"}

    response = await client.get(
        "/protected-admin",
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == expected_status_code
    assert response.json() == expected_response


@pytest.mark.asyncio
async def test_valid_jwt_admin_on_user_endpoint_works(client: AsyncClient):
    jwt = settings.admin_token
    name = settings.admin_name

    expected_status_code = status.HTTP_200_OK
    expected_response = {"message": f"Hello {name} from a protected endpoint!"}

    response = await client.get(
        "/protected",
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == expected_status_code
    assert response.json() == expected_response


@pytest.mark.asyncio
async def test_user_jwt_cant_access_admin_protected_endpoints(client: AsyncClient):
    new_created_user, jwt = await new_user()

    expected_status_code = status.HTTP_401_UNAUTHORIZED
    expected_response = {"detail": "Not an admin user"}

    response = await client.get(
        "/protected-admin",
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == expected_status_code
    assert response.json() == expected_response


@pytest.mark.asyncio
async def test_bad_scheme_for_jwt_header_returns_error(client: AsyncClient):
    new_created_user, jwt = await new_user()

    expected_status_code = status.HTTP_403_FORBIDDEN
    expected_response = {"detail": "Invalid authentication credentials"}

    response = await client.get(
        "/protected",
        headers={"Authorization": f"Here should be only Bearer {jwt}"},
    )

    assert response.status_code == expected_status_code
    assert response.json() == expected_response


@pytest.mark.asyncio
async def test_invalid_jwt_returns_error(client: AsyncClient):
    new_created_user, jwt = await new_user()

    expected_status_code = status.HTTP_403_FORBIDDEN
    expected_response = {"detail": "Invalid token"}

    response = await client.get(
        "/protected",
        headers={"Authorization": f"Bearer {jwt}123"},
    )

    assert response.status_code == expected_status_code
    assert response.json() == expected_response


@pytest.mark.asyncio
async def test_missing_sub_field_in_jwt_returns_error(client: AsyncClient):
    jwt = encode(
        {"not_a_sub_field": "123", "exp": datetime.utcnow() + timedelta(10)},
        settings.secret_key,
        algorithm=settings.algorithm,
    )

    expected_status_code = status.HTTP_403_FORBIDDEN
    expected_response = {"detail": "Missing user_id in token"}

    response = await client.get(
        "/protected",
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == expected_status_code
    assert response.json() == expected_response


@pytest.mark.asyncio
async def test_missing_exp_field_in_jwt_returns_error(client: AsyncClient):
    payload = {"sub": "123"}
    jwt = encode(payload, settings.secret_key, algorithm=settings.algorithm)

    expected_status_code = status.HTTP_403_FORBIDDEN
    expected_response = {"detail": "Invalid token"}

    response = await client.get(
        "/protected",
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == expected_status_code
    assert response.json() == expected_response


@pytest.mark.asyncio
async def test_invalid_sub_in_jwt_returns_error(client: AsyncClient):
    payload = {"sub": "123", "exp": datetime.utcnow() + timedelta(10)}
    jwt = encode(payload, settings.secret_key, algorithm=settings.algorithm)

    expected_status_code = status.HTTP_403_FORBIDDEN
    expected_response = {"detail": "Invalid user_id in token"}

    response = await client.get(
        "/protected",
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == expected_status_code
    assert response.json() == expected_response


@pytest.mark.asyncio
async def test_invalid_jwt_no_user_found_error(client: AsyncClient):
    payload = {"sub": generate_id(), "exp": datetime.utcnow() + timedelta(10)}
    jwt = encode(payload, settings.secret_key, algorithm=settings.algorithm)

    expected_status_code = status.HTTP_404_NOT_FOUND
    expected_response = {"detail": "User not found, invalid token"}

    response = await client.get(
        "/protected",
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == expected_status_code
    assert response.json() == expected_response


@pytest.mark.asyncio
async def test_expired_jwt_returns_error(client: AsyncClient):
    new_created_user, jwt = await new_user()
    jwt = {"sub": new_created_user.id, "exp": datetime.utcnow() - timedelta(minutes=10)}

    expected_status_code = status.HTTP_403_FORBIDDEN
    expected_response = {"detail": "Invalid token"}

    response = await client.get(
        "/protected",
        headers={"Authorization": f"Bearer {jwt}"},
    )

    assert response.status_code == expected_status_code
    assert response.json() == expected_response
