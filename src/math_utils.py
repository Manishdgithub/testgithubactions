"""Basic utility functions for arithmetic and validation."""

def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def divide(dividend: float, divisor: float) -> float:
    """Divide dividend by divisor.
    
    Raises:
        ZeroDivisionError: If divisor is zero.
    """
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return dividend / divisor