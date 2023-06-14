from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.apis.schemas.meal_schema import (
    MealBase,
    MealCreate,
    MealUpdate,
    ProductMealBase,
)
from app.apis.utils.utils import generate_api_error_response, generate_error_responses
from app.auth.auth_bearer import auth_required
from app.models import Meal
from app.services.errors import MealNotFound, ProductNotFound
from app.services.meal_srv import MealSrv
from app.services.product_srv import ProductSrv

router = APIRouter(tags=["meal"])


def generate_response(meal: Meal) -> MealBase:
    return MealBase(
        id=meal.id,
        name=meal.name,
        total_calories=meal.total_calories,
        total_fat=meal.total_fat,
        total_carbs=meal.total_carbs,
        total_protein=meal.total_protein,
        products=[
            ProductMealBase(
                id=meal_product.product.id,
                name=meal_product.product.name,
                calories=meal_product.calories,
                fat=meal_product.fat,
                carbs=meal_product.carbs,
                protein=meal_product.protein,
                upvotes=meal_product.product.upvotes,
                downvotes=meal_product.product.downvotes,
                quantity_grams=meal_product.quantity_grams,
            )
            for meal_product in meal.meal_products
        ],
    )


@router.post(
    "/meal",
    summary="Create new meal",
    status_code=status.HTTP_201_CREATED,
    response_model=MealBase,
    response_description="Meal created successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN
    ),
)
async def create_meal(
    meal: MealCreate,
    user_id: UUID = Depends(auth_required),
    meal_srv: MealSrv = Depends(MealSrv),
    product_srv: ProductSrv = Depends(ProductSrv),
) -> MealBase | JSONResponse:
    products = []
    quantities = []
    name = meal.name
    for _product in meal.products:
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
    meal = await meal_srv.new_meal(user_id, name, list(zip(products, quantities)))
    return MealBase(
        id=meal.id,
        name=meal.name,
        total_calories=meal.total_calories,
        total_fat=meal.total_fat,
        total_carbs=meal.total_carbs,
        total_protein=meal.total_protein,
        products=[
            ProductMealBase(
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
    "/meals",
    summary="Get all meals",
    status_code=status.HTTP_200_OK,
    response_model=List[MealBase],
    response_description="Meals fetched successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN
    ),
)
async def list_meals(
    user_id: UUID = Depends(auth_required), meal_srv: MealSrv = Depends(MealSrv)
) -> List[MealBase] | JSONResponse:
    meals = await meal_srv.list_meals(user_id)
    return [generate_response(meal) for meal in meals]


@router.get(
    "/meal/{meal_id}",
    summary="Get meal",
    status_code=status.HTTP_200_OK,
    response_model=MealBase,
    response_description="Meal fetched successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN
    ),
)
async def get_meal(
    meal_id: UUID,
    user_id: UUID = Depends(auth_required),
    meal_srv: MealSrv = Depends(MealSrv),
) -> MealBase | JSONResponse:
    try:
        meal = await meal_srv.get_meal(user_id, meal_id)
    except MealNotFound:
        return generate_api_error_response(status.HTTP_404_NOT_FOUND, "Meal not found")
    return generate_response(meal)


@router.delete(
    "/meal/{meal_id}",
    summary="Delete meal",
    status_code=status.HTTP_200_OK,
    response_description="Meal deleted successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN
    ),
)
async def delete_meal(
    meal_id: UUID,
    user_id: UUID = Depends(auth_required),
    meal_srv: MealSrv = Depends(MealSrv),
) -> JSONResponse:
    try:
        await meal_srv.delete_meal(user_id, meal_id)
    except MealNotFound:
        return generate_api_error_response(status.HTTP_404_NOT_FOUND, "Meal not found")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Meal deleted successfully"},
    )


@router.put(
    "/meal/{meal_id}",
    summary="Update meal",
    status_code=status.HTTP_200_OK,
    response_model=MealBase,
    response_description="Meal updated successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN
    ),
)
async def update_meal(
    meal_id: UUID,
    meal: MealUpdate,
    user_id: UUID = Depends(auth_required),
    meal_srv: MealSrv = Depends(MealSrv),
    product_srv: ProductSrv = Depends(ProductSrv),
) -> MealBase | JSONResponse:
    try:
        if meal.product is None:
            product_id = None
            quantity = None
        else:
            product_id = meal.product.product_id
            quantity = meal.product.quantity_grams
            product = await product_srv.get_product(product_id)
        meal = await meal_srv.update_meal(
            user_id, meal_id, meal.name, product_id, quantity, product
        )
    except ProductNotFound:
        return generate_api_error_response(
            status.HTTP_404_NOT_FOUND, "Product not found"
        )
    except MealNotFound:
        return generate_api_error_response(status.HTTP_404_NOT_FOUND, "Meal not found")
    return generate_response(meal)
