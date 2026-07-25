from decimal import Decimal

from app.models.product import Product
from app.repositories.base import ProductRepository
from app.exceptions.pricing import ProductNotFoundError


class MockProductRepository(ProductRepository):
    """
    In-memory implementation of ProductRepository.

    Used during development before integrating PostgreSQL.
    """

    def __init__(self) -> None:
        self._products = {
            "SKU-12345": Product(
                product_id="SKU-12345",
                name="Gaming Laptop",
                base_price=Decimal("1200.00"),
                inventory=15,
                demand_score=0.90,
                category="Electronics",
                cost_price=Decimal("900.00"),
            ),
            "SKU-67890": Product(
                product_id="SKU-67890",
                name="Wireless Mouse",
                base_price=Decimal("35.00"),
                inventory=250,
                demand_score=0.35,
                category="Accessories",
                cost_price=Decimal("18.00"),
            ),
            "SKU-11111": Product(
                product_id="SKU-11111",
                name="Mechanical Keyboard",
                base_price=Decimal("120.00"),
                inventory=80,
                demand_score=0.75,
                category="Accessories",
                cost_price=Decimal("70.00"),
            ),
        }

    def get_by_id(self, product_id: int) -> Product:
        """
        Retrieve a product by its ID.

        Raises:
            ProductNotFoundError if the product does not exist.
        """
        product = self._products.get(product_id)

        if product is None:
            raise ProductNotFoundError(product_id)

        return product