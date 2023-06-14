from sqlalchemy.exc import IntegrityError

from app.database import async_session
from app.models import User
from app.settings import settings


async def get_admin_data():
    """
    Get admin data from app secrets

    Returns:
        Dictionary for <User>
    """
    admin = {
        "id": settings.admin_id,
        "g_id": settings.admin_g_id,
        "email": settings.admin_email,
        "name": settings.admin_name,
    }
    return admin


async def fill_db_with_admin_data():
    """
    Save object into database

    # get admin data
    # save admin
    """
    admin = await get_admin_data()

    async with async_session() as session:
        async with session.begin():
            # Check if admin exists
            found = await session.get(User, admin["id"])
            if not found:
                # If admin does not exist, create it
                user = User(**admin)
                session.add(user)

                try:
                    await session.commit()
                except IntegrityError:
                    await session.rollback()
                    raise IntegrityError


async def insert_admin():
    """
    Insert admin into database
    """
    try:
        await fill_db_with_admin_data()
    except IntegrityError:
        pass
