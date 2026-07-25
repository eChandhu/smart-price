from abc import ABC, abstractmethod

from app.models.product import Product


class ProductRepository(ABC):
    """
    Abstract repository defining how product data is accessed.

    The business layer depends on this abstraction instead of
    any concrete storage technology.
    """

    @abstractmethod
    def get_by_id(self, product_id: int) -> Product:
        """
        Retrieve a product by its unique identifier.

        Raises:
            ProductNotFoundError: If the product does not exist.
        """
        raise NotImplementedError