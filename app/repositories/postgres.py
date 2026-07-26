from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database.models.product import ProductORM
from app.exceptions.pricing import ProductNotFoundError
from app.models.product import Product
from app.repositories.base import ProductRepository


class PostgresProductRepository(ProductRepository):
    """
    Repository implementation backed by PostgreSQL.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, product_id: str) -> Product:
        statement = select(ProductORM).where(
            ProductORM.product_id == product_id
        )

        product = self.db.execute(
            statement
        ).scalar_one_or_none()

        if product is None:
            raise ProductNotFoundError(product_id)

        return Product(
            product_id=product.product_id,
            base_price=product.base_price,
            inventory=product.inventory,
            demand_score=product.demand_score,
        )