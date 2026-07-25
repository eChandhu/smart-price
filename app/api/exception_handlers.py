from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.pricing import (
    InvalidPricingStrategyError,
    ProductNotFoundError,
)


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register global exception handlers.
    """

    @app.exception_handler(ProductNotFoundError)
    async def product_not_found_handler(
        request: Request,
        exc: ProductNotFoundError,
    ):
        return JSONResponse(
            status_code=404,
            content={
                "detail": str(exc),
            },
        )

    @app.exception_handler(
        InvalidPricingStrategyError
    )
    async def invalid_strategy_handler(
        request: Request,
        exc: InvalidPricingStrategyError,
    ):
        return JSONResponse(
            status_code=400,
            content={
                "detail": str(exc),
            },
        )