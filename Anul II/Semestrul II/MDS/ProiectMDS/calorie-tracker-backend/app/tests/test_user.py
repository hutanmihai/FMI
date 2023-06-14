import pytest
from fastapi import status
from httpx import AsyncClient

from app.apis.utils.enums import HeightMetric, WeightMetric
from app.models import User
from app.settings import settings
from app.tests.utils.asserts import (
    assert_api_error,
    assert_api_path_param_validation_error,
    assert_api_validation_error,
    assert_base_user_response,
    assert_id_did_not_change,
    assert_list_all_users_response,
)
from app.tests.utils.data_generation_tools import generate_id
from app.tests.utils.entity_instance import new_user
from app.tests.utils.entity_list_instances import get_all_users
from app.tests.utils.payloads import get_update_user_payload

ADMIN_JWT = settings.admin_token


@pytest.mark.asyncio
async def test_get_current_user_successfuly_returns_user(client: AsyncClient):
    new_created_user, jwt = await new_user()

    expected_status_code = status.HTTP_200_OK
    expected_user = new_created_user

    response = await client.get(
        "/user/me",
        headers={"Authorization": f"Bearer {jwt}"},
    )
    actual_user = User(**response.json())

    assert response.status_code == expected_status_code
    assert_base_user_response(actual_user, expected_user)


@pytest.mark.asyncio
async def test_get_all_users_succesfully_returns_all_users(client: AsyncClient):
    await new_user()
    await new_user()
    await new_user()

    expected_status_code = status.HTTP_200_OK
    expected_users = await get_all_users()

    response = await client.get(
        "/users",
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )
    actual_users = [User(**user) for user in response.json()["users"]]

    assert response.status_code == expected_status_code
    assert_list_all_users_response(actual_users, expected_users)


@pytest.mark.asyncio
async def test_delete_user_succesfully_deletes_user(client: AsyncClient):
    new_created_user, jwt = await new_user()

    expected_status_code = status.HTTP_200_OK

    response = await client.delete(
        f"/user/{new_created_user.id}",
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )

    assert response.status_code == expected_status_code


@pytest.mark.asyncio
async def test_delete_user_with_invalid_id_returns_validation_error(
    client: AsyncClient,
):
    expected_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    expected_breaking_field = "user_id"

    response = await client.delete(
        f"/user/{generate_id()}123",
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )

    assert response.status_code == expected_status_code
    assert_api_path_param_validation_error(response.json(), [expected_breaking_field])


@pytest.mark.asyncio
async def test_delete_user_with_non_existing_id_returns_not_found_error(
    client: AsyncClient,
):
    expected_status_code = status.HTTP_404_NOT_FOUND
    expected_description = "User not found"

    response = await client.delete(
        f"/user/{generate_id()}",
        headers={"Authorization": f"Bearer {ADMIN_JWT}"},
    )

    assert response.status_code == expected_status_code
    assert_api_error(response.json(), expected_description)


@pytest.mark.asyncio
async def test_update_user_succesfully_updates_user(client: AsyncClient):
    new_created_user, jwt = await new_user()

    name: str = "new name"
    pref_height_metric: HeightMetric | None = HeightMetric.cm
    height: float | None = 180.0
    pref_weight_metric: WeightMetric | None = WeightMetric.kg
    weight: float | None = 80.0
    target_weight: float | None = 70.0
    target_calories: int | None = 2000

    expected_status_code = status.HTTP_200_OK
    expected_user = new_created_user
    expected_user.name = name
    expected_user.pref_height_metric = pref_height_metric
    expected_user.height = height
    expected_user.pref_weight_metric = pref_weight_metric
    expected_user.weight = weight
    expected_user.target_weight = target_weight
    expected_user.target_calories = target_calories

    request_payload = get_update_user_payload(
        name=name,
        pref_height_metric=pref_height_metric,
        height=height,
        pref_weight_metric=pref_weight_metric,
        weight=weight,
        target_weight=target_weight,
        target_calories=target_calories,
    )

    response = await client.put(
        "/user/me",
        headers={"Authorization": f"Bearer {jwt}"},
        json=request_payload,
    )
    actual_user = User(**response.json())

    assert response.status_code == expected_status_code
    assert_id_did_not_change(actual_user, expected_user)
    assert_base_user_response(actual_user, expected_user)


@pytest.mark.asyncio
async def test_update_user_with_some_fields_missing_succesfuly_updates_user(
    client: AsyncClient,
):
    new_created_user, jwt = await new_user()

    name: str = "new name"
    pref_height_metric: HeightMetric | None = HeightMetric.cm
    height: float | None = 180.0
    pref_weight_metric: WeightMetric | None = WeightMetric.kg
    weight: float | None = None
    target_weight: float | None = None
    target_calories: int | None = None

    expected_status_code = status.HTTP_200_OK
    expected_user = new_created_user
    expected_user.name = name
    expected_user.pref_height_metric = pref_height_metric
    expected_user.height = height
    expected_user.pref_weight_metric = pref_weight_metric

    request_payload = get_update_user_payload(
        name=name,
        pref_height_metric=pref_height_metric,
        height=height,
        pref_weight_metric=pref_weight_metric,
        weight=weight,
        target_weight=target_weight,
        target_calories=target_calories,
    )

    response = await client.put(
        "/user/me",
        headers={"Authorization": f"Bearer {jwt}"},
        json=request_payload,
    )
    actual_user = User(**response.json())

    assert response.status_code == expected_status_code
    assert_id_did_not_change(actual_user, expected_user)
    assert_base_user_response(actual_user, expected_user)


@pytest.mark.asyncio
async def test_update_user_with_bad_enum_value_returns_validation_error(
    client: AsyncClient,
):
    new_created_user, jwt = await new_user()

    name: str = "new name"
    pref_height_metric: HeightMetric | None = 25
    height: float | None = 180.0
    pref_weight_metric: WeightMetric | None = 25
    weight: float | None = None
    target_weight: float | None = None
    target_calories: int | None = None

    expected_status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    expected_breaking_fields = ["pref_height_metric", "pref_weight_metric"]

    request_payload = get_update_user_payload(
        name=name,
        pref_height_metric=pref_height_metric,
        height=height,
        pref_weight_metric=pref_weight_metric,
        weight=weight,
        target_weight=target_weight,
        target_calories=target_calories,
    )

    response = await client.put(
        "/user/me",
        headers={"Authorization": f"Bearer {jwt}"},
        json=request_payload,
    )

    assert response.status_code == expected_status_code
    assert_api_validation_error(response.json(), expected_breaking_fields)
