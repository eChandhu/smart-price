from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    APP_NAME: str
    APP_VERSION: str

    DEBUG: bool

    HOST: str
    PORT: int

    LOG_LEVEL: str

    database_url: str

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int = 0

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """
    Return a cached Settings instance.

    The configuration is loaded only once during the application's lifetime.
    """
    return Settings()


settings = get_settings()