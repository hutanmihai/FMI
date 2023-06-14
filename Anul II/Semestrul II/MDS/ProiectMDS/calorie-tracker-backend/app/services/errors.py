class BaseServiceError(Exception):
    """Base class for all exceptions raised by this module."""


class BaseUserServiceError(BaseServiceError):
    """Base class for all exceptions raise by User services"""


class UserAlreadyExists(BaseUserServiceError):
    """Raised when a user already exists."""


class UserNotFound(BaseUserServiceError):
    """Raised when a user doesn't exist."""


class BaseProductServiceError(BaseServiceError):
    """Base class for all exceptions raise by Product services"""


class ProductNotFound(BaseProductServiceError):
    """Raised when a product doesn't exist."""


class BaseMealServiceError(BaseServiceError):
    """Base class for all exceptions raise by Meal services"""


class MealNotFound(BaseMealServiceError):
    """Raised when a meal doesn't exist."""


class BaseDiaryServiceError(BaseServiceError):
    """Base class for all exceptions raise by Diary services"""


class DiaryNotFound(BaseDiaryServiceError):
    """Raised when a diary doesn't exist."""


class DiaryAlreadyExists(BaseDiaryServiceError):
    """Raised when a diary already exists."""
