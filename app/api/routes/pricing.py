from fastapi import APIRouter, Depends

from app.repositories.base import ProductRepository
from app.repositories.mock import MockProductRepository
from app.schemas.pricing import PricingRequest, PricingResponse
from app.services.pricing import PricingService

router = APIRouter(
    prefix="/pricing",
    tags=["Pricing"],
)


def get_product_repository() -> ProductRepository:
    """
    Return the application's product repository.

    Currently uses an in-memory mock repository.
    This can later be replaced with a PostgreSQL implementation
    without changing the service or router.
    """
    return MockProductRepository()


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