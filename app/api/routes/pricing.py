from fastapi import APIRouter

from app.schemas.pricing import PricingRequest, PricingResponse
from app.services.pricing import PricingService

router = APIRouter(
    prefix="/pricing",
    tags=["Pricing"],
)

pricing_service = PricingService()


@router.post(
    "/calculate",
    response_model=PricingResponse,
    status_code=200,
)
def calculate_price(
    request: PricingRequest,
) -> PricingResponse:
    """
    Calculate the final selling price for a product.
    """

    return pricing_service.calculate_price(request)