from __future__ import annotations

from abc import ABC, abstractmethod
from decimal import Decimal


class BaseGuard(ABC):
    """
    Base class for all pricing guardrails.

    Each guard validates or modifies the calculated price
    before passing it to the next guard in the chain.
    """

    def __init__(self) -> None:
        self._next_guard: BaseGuard | None = None

    def set_next(self, guard: BaseGuard) -> BaseGuard:
        """
        Link the next guard in the chain.
        """

        self._next_guard = guard
        return guard

    def handle(
        self,
        price: Decimal,
    ) -> Decimal:
        """
        Execute the current guard and pass the result
        to the next guard.
        """

        updated_price = self.apply(price)

        if self._next_guard is not None:
            return self._next_guard.handle(updated_price)

        return updated_price

    @abstractmethod
    def apply(
        self,
        price: Decimal,
    ) -> Decimal:
        """
        Apply this guard's business rule.
        """
        ...