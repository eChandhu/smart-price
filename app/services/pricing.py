from decimal import Decimal

from fastapi import HTTPException

from app.factories.strategy_factory import StrategyFactory
from app.schemas.pricing import PricingRequest, PricingResponse


class PricingService:
    """
    Service responsible for orchestrating the pricing workflow.
    """

    def __init__(self) -> None:
        self.strategy_factory = StrategyFactory

    def calculate_price(
        self,
        request: PricingRequest,
    ) -> PricingResponse:
        """
        Calculate the final price using the selected pricing strategy.
        """

        try:
            strategy = self.strategy_factory.get_strategy(
                request.strategy
            )
        except ValueError as exc:
            raise HTTPException(
                status_code=400,
                detail=str(exc),
            ) from exc

        final_price = strategy.calculate_price(request)

        return PricingResponse(
            product_id=request.product_id,
            original_price=request.base_price,
            final_price=final_price.quantize(Decimal("0.01")),
            strategy_used=request.strategy,
            message="Price calculated successfully.",
        )