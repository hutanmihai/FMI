from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.apis.schemas.product_schema import (
    ProductBase,
    ProductCreate,
    ProductsList,
    ProductUpdate,
)
from app.apis.utils.utils import generate_api_error_response, generate_error_responses
from app.auth.auth_bearer import admin_required, auth_required
from app.services.errors import ProductNotFound
from app.services.product_srv import ProductSrv

router = APIRouter(tags=["product"])


@router.get(
    "/product/{product_id}",
    summary="Get product",
    status_code=status.HTTP_200_OK,
    response_model=ProductBase,
    response_description="Product fetched successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN
    ),
    dependencies=[Depends(auth_required)],
)
async def get_product(
    product_id: UUID, product_srv: ProductSrv = Depends(ProductSrv)
) -> ProductBase | JSONResponse:
    try:
        product = await product_srv.get_product(product_id)
    except ProductNotFound:
        return generate_api_error_response(
            status.HTTP_404_NOT_FOUND, "Product not found"
        )
    return product


@router.get(
    "/products",
    summary="Get all products - ADMIN ONLY",
    status_code=status.HTTP_200_OK,
    response_model=ProductsList,
    response_description="Products fetched successfully",
    responses=generate_error_responses(
        status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN
    ),
    dependencies=[Depends(admin_required)],
)
async def list_products(product_srv: ProductSrv = Depends(ProductSrv)) -> ProductsList:
    products = await product_srv.list_products()
    return ProductsList(products=[product for product in products])


@router.post(
    "/product",
    summary="Create new product",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductBase,
    response_description="Product created successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN
    ),
    dependencies=[Depends(auth_required)],
)
async def new_product(
    product: ProductCreate, product_srv: ProductSrv = Depends(ProductSrv)
) -> ProductBase | JSONResponse:
    product = await product_srv.new_product(
        name=product.name,
        calories=product.calories,
        protein=product.protein,
        fat=product.fat,
        carbs=product.carbs,
    )
    return product


@router.put(
    "/product/{product_id}",
    summary="Update product",
    status_code=status.HTTP_200_OK,
    response_model=ProductBase,
    response_description="Product updated successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN
    ),
    dependencies=[Depends(auth_required)],
)
async def update_product(
    product_id: UUID,
    product: ProductUpdate,
    product_srv: ProductSrv = Depends(ProductSrv),
) -> ProductBase | JSONResponse:
    try:
        product = await product_srv.update_product(
            product_id=product_id,
            name=product.name,
            calories=product.calories,
            protein=product.protein,
            fat=product.fat,
            carbs=product.carbs,
            upvotes=product.upvotes,
            downvotes=product.downvotes,
        )
    except ProductNotFound:
        return generate_api_error_response(
            status.HTTP_404_NOT_FOUND, "Product not found"
        )
    return product


@router.delete(
    "/product/{product_id}",
    summary="Delete product - ADMIN ONLY",
    status_code=status.HTTP_200_OK,
    response_description="Product deleted successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND,
        status.HTTP_401_UNAUTHORIZED,
        status.HTTP_403_FORBIDDEN,
    ),
    dependencies=[Depends(admin_required)],
)
async def delete_product(
    product_id: UUID, product_srv: ProductSrv = Depends(ProductSrv)
) -> JSONResponse:
    try:
        await product_srv.delete_product(product_id)
    except ProductNotFound:
        return generate_api_error_response(
            status.HTTP_404_NOT_FOUND, "Product not found"
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Product deleted successfully"},
    )


@router.get(
    "/product/search/{product_string}",
    summary="Get product by string",
    status_code=status.HTTP_200_OK,
    response_model=ProductsList,
    response_description="Product updated successfully",
    responses=generate_error_responses(
        status.HTTP_404_NOT_FOUND, status.HTTP_403_FORBIDDEN
    ),
    dependencies=[Depends(auth_required)],
)
async def get_product_by_string(
    product_string: str, product_srv: ProductSrv = Depends(ProductSrv)
) -> ProductsList:
    products = await product_srv.search_product(product_string)
    return ProductsList(products=[product for product in products])
