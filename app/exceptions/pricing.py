class PricingException(Exception):
    """
    Base exception for all pricing-related errors.
    """


class ProductNotFoundError(PricingException):
    """
    Raised when a product cannot be found.
    """

    def __init__(self, product_id: str) -> None:
        self.product_id = product_id
        super().__init__(
            f"Product with ID {product_id} was not found."
        )


class InvalidPricingStrategyError(PricingException):
    """
    Raised when an unsupported pricing strategy is requested.
    """

    def __init__(self, strategy: str) -> None:
        self.strategy = strategy
        super().__init__(
            f"Unsupported pricing strategy: '{strategy}'."
        )