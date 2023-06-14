from csv import DictReader

from sqlalchemy.exc import IntegrityError

from app.database import async_session
from app.models import Product

PRODUCTS_PATH = "../../data/food.csv"


async def get_products_data():
    """
    Get products data from CSV file

    Returns:
        List of dictionaries for <Product>
    """
    with open(PRODUCTS_PATH, "r", encoding="utf-8") as csv_file:
        reader = DictReader(csv_file, delimiter=",")

        products = []

        for row in reader:
            product = {
                "name": row["Food"],
                "calories": float(row["Calories"]),
                "fat": float(row["Fat"]),
                "carbs": float(row["Carbs"]),
                "protein": float(row["Protein"]),
                "upvotes": 0,
                "downvotes": 0,
            }
            product["name"] = product["name"].strip().lower()
            products.append(product)

    return products


async def fill_db_with_products():
    """
    Save object into database

    # get all products' data
    # save each product
    """
    products = await get_products_data()

    async with async_session() as session:
        async with session.begin():
            for product in products:
                prod = Product(**product)
                session.add(prod)

            try:
                await session.commit()
            except IntegrityError:
                await session.rollback()


async def fill_db():
    await fill_db_with_products()


if __name__ == "__main__":
    import asyncio

    asyncio.run(fill_db())
