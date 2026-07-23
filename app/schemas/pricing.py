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

    base_price: Decimal = Field(
        ...,
        gt=0,
        description="Original selling price of the product",
        examples=[999.99],
    )

    inventory: int = Field(
        ...,
        ge=0,
        description="Current inventory level",
        examples=[120],
    )

    demand_score: float = Field(
        ...,
        ge=0,
        le=1,
        description="Normalized demand score between 0 and 1",
        examples=[0.82],
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