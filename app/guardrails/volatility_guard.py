from decimal import Decimal

from app.guardrails.base_guard import BaseGuard


class VolatilityGuard(BaseGuard):
    """
    Limit excessive price increases.
    """

    MAX_MULTIPLIER = Decimal("1.40")

    def __init__(
        self,
        base_price: Decimal,
    ) -> None:
        super().__init__()
        self.base_price = base_price

    def apply(
        self,
        price: Decimal,
    ) -> Decimal:

        maximum_allowed = (
            self.base_price * self.MAX_MULTIPLIER
        )

        return min(price, maximum_allowed)