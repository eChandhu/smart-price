import json
import logging
from dataclasses import asdict
from decimal import Decimal
from typing import Optional

from redis import Redis

from app.models.product import Product

logger = logging.getLogger(__name__)


class ProductCache:
    """
    Handles all Redis operations for Product objects.

    Responsibilities:
    - Build Redis keys
    - Read Product objects from Redis
    - Write Product objects to Redis
    - Delete Product objects from Redis
    """

    CACHE_PREFIX = "product"
    TTL_SECONDS = 300  # Cache expires after 5 minutes

    def __init__(self, redis_client: Redis) -> None:
        self._redis = redis_client

    def _build_key(self, product_id: str) -> str:
        """
        Build a consistent Redis key for a product.

        Example:
            product:SKU-12345
        """
        return f"{self.CACHE_PREFIX}:{product_id}"

    def get_product(
        self,
        product_id: str,
    ) -> Optional[Product]:
        """
        Retrieve a product from Redis.

        Returns:
            Product if found, otherwise None.
        """
        key = self._build_key(product_id)

        try:
            cached_data = self._redis.get(key)

            if cached_data is None:
                return None

            data = json.loads(cached_data)

            # Convert JSON string back to Decimal
            data["base_price"] = Decimal(data["base_price"])

            return Product(**data)

        except Exception:
            logger.exception(
                "Failed to retrieve product '%s' from Redis.",
                product_id,
            )
            return None

    def cache_product(
        self,
        product: Product,
    ) -> bool:
        """
        Store a Product in Redis.

        Returns:
            True if caching succeeds, otherwise False.
        """
        key = self._build_key(product.product_id)

        try:
            self._redis.set(
                key,
                json.dumps(
                    asdict(product),
                    default=str,
                ),
                ex=self.TTL_SECONDS,
            )

            return True

        except Exception:
            logger.exception(
                "Failed to cache product '%s' in Redis.",
                product.product_id,
            )
            return False

    def invalidate_product(
        self,
        product_id: str,
    ) -> None:
        """
        Remove a Product from Redis.
        """
        key = self._build_key(product_id)

        try:
            self._redis.delete(key)

        except Exception:
            logger.exception(
                "Failed to invalidate product '%s' from Redis.",
                product_id,
            )