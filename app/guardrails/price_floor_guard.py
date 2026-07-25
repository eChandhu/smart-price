from decimal import Decimal

from app.guardrails.base_guard import BaseGuard


class PriceFloorGuard(BaseGuard):
    """
    Prevent prices from dropping below the configured floor.
    """

    MIN_PRICE = Decimal("100.00")

    def apply(
        self,
        price: Decimal,
    ) -> Decimal:

        return max(price, self.MIN_PRICE)