from typing import Final

from app.schemas.pricing import PricingStrategy
from app.strategies.base import PricingStrategy as BasePricingStrategy
from app.strategies.clearance import ClearancePricingStrategy
from app.strategies.surge import SurgePricingStrategy


class StrategyFactory:
    """
    Factory responsible for creating pricing strategy instances.
    """

    _STRATEGIES: Final = {
        PricingStrategy.SURGE: SurgePricingStrategy,
        PricingStrategy.CLEARANCE: ClearancePricingStrategy,
    }

    @classmethod
    def get_strategy(
        cls,
        strategy: PricingStrategy,
    ) -> BasePricingStrategy:
        strategy_cls = cls._STRATEGIES.get(strategy)

        if strategy_cls is None:
            raise ValueError(
                f"Unsupported pricing strategy: {strategy}"
            )

        return strategy_cls()