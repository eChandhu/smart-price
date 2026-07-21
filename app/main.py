from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from app.config.logging import configure_logging
from app.config.settings import settings
from app.api.routes.pricing import router as pricing_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()

    logger.info("Starting SmartPrice API...")

    yield

    logger.info("Shutting down SmartPrice API...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

app.include_router(pricing_router)