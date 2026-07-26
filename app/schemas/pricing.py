from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class PricingStrategy(str, Enum):
    SURGE = "surge"
    CLEARANCE = "clearance"


class PricingRequest(BaseModel):
    product_id: str = Field(
        ...,
        description="Unique identifier for the product",
        examples=["SKU-12345"],
    )

    strategy: PricingStrategy = Field(
        ...,
        description="Pricing strategy to apply",
    )


class PricingResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_id: str

    original_price: Decimal

    final_price: Decimal

    strategy_used: PricingStrategy

    message: str