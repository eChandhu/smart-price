from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.database.session import get_db

from app.repositories.base import ProductRepository
from app.repositories.postgres import PostgresProductRepository

from app.schemas.pricing import PricingRequest, PricingResponse
from app.services.pricing import PricingService

router = APIRouter(
    prefix="/pricing",
    tags=["Pricing"],
)


def get_product_repository(
    db: Session = Depends(get_db),
) -> ProductRepository:
    """
    Return the PostgreSQL-backed product repository.

    The router depends only on the ProductRepository interface,
    allowing the implementation to be swapped without affecting
    the service or API layer.
    """
    return PostgresProductRepository(db)


def get_pricing_service(
    repository: ProductRepository = Depends(get_product_repository),
) -> PricingService:
    """
    Create a PricingService with its required dependencies.
    """
    return PricingService(repository)


@router.post(
    "/calculate",
    response_model=PricingResponse,
    status_code=200,
)
def calculate_price(
    request: PricingRequest,
    pricing_service: PricingService = Depends(get_pricing_service),
) -> PricingResponse:
    """
    Calculate the final selling price for a product.
    """
    return pricing_service.calculate_price(request)