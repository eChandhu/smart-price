from abc import ABC, abstractmethod
from decimal import Decimal

from app.schemas.pricing import PricingRequest


class PricingStrategy(ABC):
    """
    Abstract base class for all pricing strategies.
    """

    @abstractmethod
    def calculate_price(
        self,
        request: PricingRequest,
    ) -> Decimal:
        """
        Calculate the final price.
        """
        ...