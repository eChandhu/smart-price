from decimal import Decimal

from app.models.product import Product
from app.strategies.base import PricingStrategy


class ClearancePricingStrategy(PricingStrategy):
    """
    Applies inventory-based clearance discounts.
    """

    def calculate_price(
        self,
        product: Product,
    ) -> Decimal:
        if product.inventory > 80:
            discount = Decimal("0.30")
        elif product.inventory > 50:
            discount = Decimal("0.15")
        else:
            discount = Decimal("0.05")

        return product.base_price * (
            Decimal("1") - discount
        )