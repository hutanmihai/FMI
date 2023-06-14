from sqlalchemy.sql.expression import select

from app.models import User
from app.repositories.errors import EntityNotFound
from app.repositories.sqlalchemy_repo import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    """User repository"""

    async def get_by_email(self, email):
        """Get user by email"""
        user = await self.db_session.scalar(select(User).where(User.email == email))
        if not user:
            raise EntityNotFound()
        return user
