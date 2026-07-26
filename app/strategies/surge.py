from decimal import Decimal

from app.models.product import Product
from app.strategies.base import PricingStrategy


class SurgePricingStrategy(PricingStrategy):
    """
    Applies demand-based surge pricing.
    """

    def calculate_price(
        self,
        product: Product,
    ) -> Decimal:
        multiplier = Decimal("1") + (
            Decimal(str(product.demand_score))
            * Decimal("0.5")
        )

        return product.base_price * multiplier