from decimal import Decimal

from app.factories.strategy_factory import StrategyFactory
from app.guardrails.base_guard import BaseGuard
from app.guardrails.price_floor_guard import PriceFloorGuard
from app.guardrails.volatility_guard import VolatilityGuard
from app.repositories.base import ProductRepository
from app.schemas.pricing import (
    PricingRequest,
    PricingResponse,
)


class PricingService:
    """
    Service responsible for orchestrating the pricing workflow.
    """

    def __init__(
        self,
        repository: ProductRepository,
    ) -> None:
        self.strategy_factory = StrategyFactory
        self._repository = repository

    def _build_guard_chain(
        self,
        base_price: Decimal,
    ) -> BaseGuard:
        """
        Build and return the pricing guard chain.
        """

        floor_guard = PriceFloorGuard()
        volatility_guard = VolatilityGuard(base_price)

        floor_guard.set_next(volatility_guard)

        return floor_guard

    def calculate_price(
        self,
        request: PricingRequest,
    ) -> PricingResponse:
        """
        Calculate the final price using the selected strategy
        and apply all pricing guardrails.
        """

        product = self._repository.get_by_id(
            request.product_id
        )

        strategy = self.strategy_factory.get_strategy(
            request.strategy
        )

        raw_price = strategy.calculate_price(
            product
        )

        guard_chain = self._build_guard_chain(
            product.base_price
        )

        final_price = guard_chain.handle(raw_price)

        return PricingResponse(
            product_id=product.product_id,
            original_price=product.base_price,
            final_price=final_price.quantize(
                Decimal("0.01")
            ),
            strategy_used=request.strategy,
            message="Price calculated successfully.",
        )