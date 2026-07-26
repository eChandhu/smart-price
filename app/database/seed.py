from decimal import Decimal

from app.database.session import SessionLocal
from app.database.models.product import ProductORM


PRODUCTS = [
    ProductORM(
        product_id="SKU-12345",
        base_price=Decimal("999.99"),
        inventory=100,
        demand_score=0.80,
    ),
    ProductORM(
        product_id="SKU-67890",
        base_price=Decimal("499.99"),
        inventory=35,
        demand_score=0.45,
    ),
    ProductORM(
        product_id="SKU-11111",
        base_price=Decimal("1499.99"),
        inventory=15,
        demand_score=0.95,
    ),
]


def seed_products() -> None:
    db = SessionLocal()

    try:
        if db.query(ProductORM).count() > 0:
            print("Products already exist.")
            return

        db.add_all(PRODUCTS)
        db.commit()

        print("Database seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_products()