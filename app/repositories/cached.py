import logging

from app.cache.product_cache import ProductCache
from app.models.product import Product
from app.repositories.base import ProductRepository

logger = logging.getLogger(__name__)


class CachedProductRepository(ProductRepository):
    """
    Decorates a ProductRepository by adding Redis caching.

    Implements the Cache-Aside pattern:
    1. Check Redis.
    2. If found, return the cached product.
    3. Otherwise, fetch from the wrapped repository.
    4. Store the product in Redis.
    5. Return the product.
    """

    def __init__(
        self,
        cache: ProductCache,
        repository: ProductRepository,
    ) -> None:
        self._cache = cache
        self._repository = repository

    def get_by_id(
        self,
        product_id: str,
    ) -> Product:
        """
        Retrieve a product using the Cache-Aside pattern.
        """

        # Attempt to retrieve from Redis
        product = self._cache.get_product(product_id)

        if product is not None:
            logger.info(
                "Cache HIT for product '%s'",
                product_id,
            )
            return product

        logger.info(
            "Cache MISS for product '%s'",
            product_id,
        )

        # Fallback to PostgreSQL
        product = self._repository.get_by_id(product_id)

        # Cache the product for future requests
        if self._cache.cache_product(product):
            logger.info(
                "Product '%s' cached successfully",
                product_id,
            )

        return product