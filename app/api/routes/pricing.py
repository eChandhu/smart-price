from fastapi import APIRouter, Depends

from app.api.dependencies import get_pricing_service
from app.schemas.pricing import (
    PricingRequest,
    PricingResponse,
)
from app.services.pricing import PricingService

router = APIRouter(
    prefix="/pricing",
    tags=["Pricing"],
)


@router.post(
    "/calculate",
    response_model=PricingResponse,
)
def calculate_price(
    request: PricingRequest,
    service: PricingService = Depends(get_pricing_service),
) -> PricingResponse:
    """
    Calculate the final product price.
    """
    return service.calculate_price(request)