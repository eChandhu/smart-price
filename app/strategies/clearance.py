from decimal import Decimal

from app.schemas.pricing import PricingRequest
from app.strategies.base import PricingStrategy


class ClearancePricingStrategy(PricingStrategy):
    """
    Applies inventory-based clearance discounts.
    """

    def calculate_price(self, request: PricingRequest) -> Decimal:
        if request.inventory > 80:
            discount = Decimal("0.30")
        elif request.inventory > 50:
            discount = Decimal("0.15")
        else:
            discount = Decimal("0.05")

        return request.base_price * (Decimal("1") - discount)