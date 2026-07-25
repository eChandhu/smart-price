from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Product:
    """
    Domain model representing a product in the pricing system.

    This model is independent of HTTP, databases, and external APIs.
    It captures the core business entity used by the application.
    """

    product_id: int
    name: str
    base_price: Decimal
    inventory: int
    demand_score: float
    category: str
    cost_price: Decimal
    is_active: bool = True