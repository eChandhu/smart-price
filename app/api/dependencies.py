from fastapi import Depends
from redis import Redis
from sqlalchemy.orm import Session

from app.cache.product_cache import ProductCache
from app.cache.redis_client import get_redis_client
from app.database.session import get_db
from app.repositories.base import ProductRepository
from app.repositories.cached import CachedProductRepository
from app.repositories.postgres import PostgresProductRepository
from app.services.pricing import PricingService


def get_postgres_repository(
    db: Session = Depends(get_db),
) -> ProductRepository:
    """
    Provide the PostgreSQL-backed repository.
    """
    return PostgresProductRepository(db)


def get_product_cache() -> ProductCache:
    """
    Provide the Redis-backed product cache.
    """
    redis_client: Redis = get_redis_client()
    return ProductCache(redis_client)


def get_product_repository(
    cache: ProductCache = Depends(get_product_cache),
    repository: ProductRepository = Depends(get_postgres_repository),
) -> ProductRepository:
    """
    Wrap the PostgreSQL repository with Redis caching.
    """
    return CachedProductRepository(
        cache=cache,
        repository=repository,
    )


def get_pricing_service(
    repository: ProductRepository = Depends(get_product_repository),
) -> PricingService:
    """
    Provide the PricingService with the configured repository.
    """
    return PricingService(repository)