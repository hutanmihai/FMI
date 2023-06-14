from pydantic import BaseSettings, Field, PostgresDsn, validator


class AppSettings(BaseSettings):
    algorithm: str = Field(..., env="ALGORITHM")
    secret_key: str = Field(..., env="SECRET_KEY")
    access_token_expires_minutes: int = Field(..., env="ACCESS_TOKEN_EXPIRE_MINUTES")

    admin_token: str = Field(..., env="ADMIN_TOKEN")
    admin_id: str = Field(..., env="ADMIN_ID")
    admin_g_id: str = Field(..., env="ADMIN_G_ID")
    admin_email: str = Field(..., env="ADMIN_EMAIL")
    admin_name: str = Field(..., env="ADMIN_NAME")

    google_client_id: str = Field(..., env="GOOGLE_CLIENT_ID")
    google_client_secret: str = Field(..., env="GOOGLE_CLIENT_SECRET")
    google_scopes: str = "openid email profile"
    google_conf_url: str = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )

    app_host: str = Field(..., env="APP_HOST")
    app_port: str = Field(..., env="APP_PORT")

    database_hostname: str = Field(..., env="DATABASE_HOSTNAME")
    database_user: str = Field(..., env="DATABASE_USER")
    database_password: str = Field(..., env="DATABASE_PASSWORD")
    database_port: str = Field(..., env="DATABASE_PORT")
    database_db: str = Field(..., env="DATABASE_DB")
    sqlalchemy_database_url: str = ""

    @validator("sqlalchemy_database_url")
    def _assemble_db_connection(cls, v: str, values: dict[str, str]) -> str:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values["database_user"],
            password=values["database_password"],
            host=values["database_hostname"],
            port=values["database_port"],
            path=f"/{values['database_db']}",
        )


settings: AppSettings = AppSettings()
