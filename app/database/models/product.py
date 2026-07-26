from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base
from decimal import Decimal


class ProductORM(Base):
    """
    SQLAlchemy ORM model representing the products table.
    """

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    product_id: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    base_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    inventory: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    demand_score: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )