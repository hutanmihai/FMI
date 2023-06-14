from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.apis.schemas.diary_schema import (
    DiaryBase,
    DiaryCreate,
    DiaryUpdate,
    ProductDiaryBase,
)
from app.apis.utils.utils import generate_api_error_response, generate_error_responses
from app.auth.auth_bearer import auth_required
from app.models import Diary
from app.services.diary_srv import DiarySrv
from app.services.errors import DiaryAlreadyExists, DiaryNotFound, ProductNotFound
from app.services.product_srv import ProductSrv

router = APIRouter(tags=["diary"])


def generate_response(diary: Diary) -> DiaryBase:
    return DiaryBase(
        id=diary.id,
        date=diary.date,
        total_calories=diary.total_calories,
        total_fat=diary.total_fat,
        total_carbs=diary.total_carbs,
        total_protein=diary.total_protein,
        products=[
            ProductDiaryBase(
                id=diary_product.product.id,
                name=diary_product.product.name,
                calories=diary_product.calories,
                fat=diary_product.fat,
                carbs=diary_product.carbs,
                protein=diary_product.protein,
                upvotes=diary_product.product.upvotes,
                downvotes=diary_product.product.downvotes,
                quantity_grams=diary_product.quantity_grams,
            )
            for diary_product in diary.diary_products
        ],
    )


@router.post(
    "/diary",
    summary="Create new diary",
    status_code=status.HTTP_201_CREATED,
    response_model=DiaryBase,
    response_description="diary created successfully",
    responses=generate_error_responses(
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_404_NOT_FOUND,
        status.HTTP_403_FORBIDDEN,
    ),
)
async def create_diary(
    diary: DiaryCreate,
    user_id: UUID = Depends(auth_required),
    diary_srv: DiarySrv = Depends(DiarySrv),
    product_srv: ProductSrv = Depends(ProductSrv),
) -> DiaryBase | JSONResponse:
    products = []
    quantities = []
    date = diary.date
    for _product in diary.products:
        try:
            product = await product_srv.get_product(_product.product_id)
        except ProductNotFound:
            return generate_api_error_response(
                status.HTTP_404_NOT_FOUND, "Product not found"
            )
        # sum up the quantities for the same product
        if product in products:
            index = products.index(product)
            quantities[index] += _product.quantity_grams
        else:
            products.append(product)
            quantities.append(_product.quantity_grams)
    try:
        diary = await diary_srv.new_diary(
            user_id, date, list(zip(products, quantities))
        )
    except DiaryAlreadyExists:
        return generate_api_error_response(
            status.HTTP_400_BAD_REQUEST, "Diary already exists"
        )
    return DiaryBase(
        id=diary.id,
        date=diary.date,
        total_calories=diary.total_calories,
        total_fat=diary.total_fat,
        total_carbs=diary.total_carbs,
        total_protein=diary.total_protein,
        products=[
            ProductDiaryBase(
                id=product.id,
                name=product.name,
                calories=round(product.calories * quantity / 100, 2),
                fat=round(product.fat * quantity / 100, 2),
                carbs=round(product.carbs * quantity / 100, 2),
                protein=round(product.protein * quantity / 100, 2),
                upvotes=product.upvotes,
                downvotes=product.downvotes,
                quantity_grams=quantity,
            )
            for product, quantity in zip(products, quantities)
        ],
    )


@router.get(
    "/diaries",
    summary="Get all diaries",
    status_code=status.HTTP_200_OK,
    response_model=List[DiaryBase],
    response_description="Diaries fetched successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN
    ),
)
async def list_diaries(
    user_id: UUID = Depends(auth_required), diary_srv: DiarySrv = Depends(DiarySrv)
) -> List[DiaryBase] | JSONResponse:
    diaries = await diary_srv.list_diaries(user_id)
    return [generate_response(diary) for diary in diaries]


@router.get(
    "/diary/{diary_id}",
    summary="Get diary",
    status_code=status.HTTP_200_OK,
    response_model=DiaryBase,
    response_description="Diary fetched successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN
    ),
)
async def get_diary(
    diary_id: UUID,
    user_id: UUID = Depends(auth_required),
    diary_srv: DiarySrv = Depends(DiarySrv),
) -> DiaryBase | JSONResponse:
    try:
        diary = await diary_srv.get_diary(user_id, diary_id)
    except DiaryNotFound:
        return generate_api_error_response(status.HTTP_404_NOT_FOUND, "Diary not found")
    return generate_response(diary)


@router.delete(
    "/diary/{diary_id}",
    summary="Delete diary",
    status_code=status.HTTP_200_OK,
    response_description="Diary deleted successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN
    ),
)
async def delete_diary(
    diary_id: UUID,
    user_id: UUID = Depends(auth_required),
    diary_srv: DiarySrv = Depends(DiarySrv),
) -> JSONResponse:
    try:
        await diary_srv.delete_diary(user_id, diary_id)
    except DiaryNotFound:
        return generate_api_error_response(status.HTTP_404_NOT_FOUND, "Diary not found")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Diary deleted successfully"},
    )


@router.put(
    "/diary/{diary_id}",
    summary="Update diary",
    status_code=status.HTTP_200_OK,
    response_model=DiaryBase,
    response_description="Diary updated successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN
    ),
)
async def update_diary(
    diary_id: UUID,
    diary: DiaryUpdate,
    user_id: UUID = Depends(auth_required),
    diary_srv: DiarySrv = Depends(DiarySrv),
    product_srv: ProductSrv = Depends(ProductSrv),
) -> DiaryBase | JSONResponse:
    try:
        try:
            product = await product_srv.get_product(diary.product.product_id)
            product_id = product.id
            quantity = diary.product.quantity_grams
        except ProductNotFound:
            return generate_api_error_response(
                status.HTTP_404_NOT_FOUND, "Product not found"
            )
        diary = await diary_srv.update_diary(
            user_id, diary_id, product_id, quantity, product
        )
    except DiaryNotFound:
        return generate_api_error_response(status.HTTP_404_NOT_FOUND, "Diary not found")
    return generate_response(diary)
