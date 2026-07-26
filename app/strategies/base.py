from abc import ABC, abstractmethod
from decimal import Decimal

from app.models.product import Product


class PricingStrategy(ABC):
    """
    Abstract base class for all pricing strategies.
    """

    @abstractmethod
    def calculate_price(
        self,
        product: Product,
    ) -> Decimal:
        """
        Calculate the final price.
        """
        ...