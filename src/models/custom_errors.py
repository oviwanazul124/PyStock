# Custom error classes for the Pystock system.

class ProductNotFoundError(Exception):
    """Raised when a product is not found in the inventory."""
    pass