from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Product:
    """
    Domain model representing a product.

    This model is independent of FastAPI, SQLAlchemy,
    and any external infrastructure.
    """

    product_id: str
    base_price: Decimal
    inventory: int
    demand_score: float 