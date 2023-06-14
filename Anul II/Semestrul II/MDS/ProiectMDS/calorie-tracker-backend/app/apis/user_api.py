from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.apis.schemas.user_schema import UserBase, UsersList, UserUpdate
from app.apis.utils.utils import generate_api_error_response, generate_error_responses
from app.auth.auth_bearer import admin_required, auth_required
from app.services.errors import UserNotFound
from app.services.user_srv import UserSrv
from app.settings import settings

router = APIRouter(tags=["user"])


@router.get(
    "/user/me",
    summary="Get current user",
    status_code=status.HTTP_200_OK,
    response_model=UserBase,
    response_description="User fetched successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN
    ),
)
async def get_current_user(
    user_id: UUID = Depends(auth_required), user_srv: UserSrv = Depends(UserSrv)
) -> UserBase | JSONResponse:
    try:
        user = await user_srv.get_user(user_id)
    except UserNotFound:
        return generate_api_error_response(status.HTTP_404_NOT_FOUND, "User not found")
    return user


@router.get(
    "/users",
    summary="Get all users - ADMIN ONLY",
    status_code=status.HTTP_200_OK,
    response_model=UsersList,
    response_description="Users fetched successfully",
    responses=generate_error_responses(
        status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN
    ),
    dependencies=[Depends(admin_required)],
)
async def get_all_users(
    user_srv: UserSrv = Depends(UserSrv),
) -> UsersList | JSONResponse:
    users = await user_srv.get_all_users()
    return UsersList(users=[user for user in users])


@router.put(
    "/user/me",
    summary="Update current user",
    status_code=status.HTTP_200_OK,
    response_model=UserBase,
    response_description="User updated successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND,
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_403_FORBIDDEN,
    ),
)
async def update_user(
    user_update: UserUpdate,
    user_id: UUID = Depends(auth_required),
    user_srv: UserSrv = Depends(UserSrv),
) -> UserBase | JSONResponse:
    try:
        user = await user_srv.update_user(
            user_id=user_id,
            name=user_update.name,
            pref_height_metric=user_update.pref_height_metric,
            pref_weight_metric=user_update.pref_weight_metric,
            height=user_update.height,
            weight=user_update.weight,
            target_weight=user_update.target_weight,
            target_calories=user_update.target_calories,
        )
    except UserNotFound:
        return generate_api_error_response(status.HTTP_404_NOT_FOUND, "User not found")
    return user


@router.delete(
    "/user/{user_id}",
    summary="Delete user - ADMIN ONLY",
    status_code=status.HTTP_200_OK,
    response_description="User deleted successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND,
        status.HTTP_401_UNAUTHORIZED,
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_403_FORBIDDEN,
    ),
    dependencies=[Depends(admin_required)],
)
async def delete_user(
    user_id: UUID,
    user_srv: UserSrv = Depends(UserSrv),
) -> JSONResponse:
    if user_id == settings.admin_id:
        return generate_api_error_response(
            status.HTTP_400_BAD_REQUEST, "Cannot delete admin user"
        )
    try:
        await user_srv.delete_user(user_id)
    except UserNotFound:
        return generate_api_error_response(status.HTTP_404_NOT_FOUND, "User not found")
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "User deleted successfully"}
    )
