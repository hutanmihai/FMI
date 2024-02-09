from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Vision Canvas API"
    APP_DESCRIPTION: str = "Vision Canvas API"
    APP_VERSION: str = "v1"

    # ENV
    APP_HOST: str = "127.0.0.1"
    APP_PORT: int = 8080


settings = Settings(_env_file=".env")
