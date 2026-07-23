from decimal import Decimal

from app.schemas.pricing import PricingRequest
from app.strategies.base import PricingStrategy


class SurgePricingStrategy(PricingStrategy):
    """
    Applies demand-based surge pricing.
    """

    def calculate_price(self, request: PricingRequest) -> Decimal:
        multiplier = Decimal("1") + (
            Decimal(str(request.demand_score)) * Decimal("0.5")
        )

        return request.base_price * multiplier