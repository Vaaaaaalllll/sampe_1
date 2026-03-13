# WARNING: template code, may need edits
"""Mathematical operations for the calculator."""

from typing import Union

Number = Union[int, float]


class DivisionByZeroError(Exception):
    """Raised when attempting to divide by zero."""
    pass


def add(a: Number, b: Number) -> Number:
    """Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Subtract b from a.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
    """
    return a * b


def divide(a: Number, b: Number) -> float:
    """Divide a by b.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Quotient of a and b
        
    Raises:
        DivisionByZeroError: If b is zero
    """
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero")
    return a / b


def power(a: Number, b: Number) -> Number:
    """Raise a to the power of b.
    
    Args:
        a: Base
        b: Exponent
        
    Returns:
        a raised to the power of b
    """
    return a ** b


def modulo(a: Number, b: Number) -> Number:
    """Calculate a modulo b.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Remainder of a divided by b
        
    Raises:
        DivisionByZeroError: If b is zero
    """
    if b == 0:
        raise DivisionByZeroError("Cannot perform modulo with zero")
    return a % b
