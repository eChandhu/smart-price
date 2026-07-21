import logging

from app.config.settings import settings


def configure_logging() -> None:
    """
    Configure the application's logging system.

    This function should be called only once during application startup.
    """

    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )