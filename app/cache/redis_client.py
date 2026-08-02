from functools import lru_cache

import redis

from app.config.settings import settings


@lru_cache
def get_redis_client() -> redis.Redis:
    """
    Create and cache a Redis client instance.

    The Redis client is thread-safe and can be shared across the application,
    so we create it once and reuse it.
    """
    return redis.Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        decode_responses=True,
    )