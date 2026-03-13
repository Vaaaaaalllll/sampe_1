# WARNING: template code, may need edits
"""Calculator class for performing arithmetic operations."""

from typing import Union
from src.operations import (
    add,
    subtract,
    multiply,
    divide,
    power,
    modulo,
    DivisionByZeroError,
)

Number = Union[int, float]


class Calculator:
    """A simple calculator class for basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator with an empty history."""
        self.history = []

    def add(self, a: Number, b: Number) -> Number:
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        result = add(a, b)
        self._add_to_history(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: Number, b: Number) -> Number:
        """Subtract b from a.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
        """
        result = subtract(a, b)
        self._add_to_history(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: Number, b: Number) -> Number:
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        result = multiply(a, b)
        self._add_to_history(f"{a} * {b} = {result}")
        return result

    def divide(self, a: Number, b: Number) -> float:
        """Divide a by b.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            Quotient of a and b
            
        Raises:
            DivisionByZeroError: If b is zero
        """
        result = divide(a, b)
        self._add_to_history(f"{a} / {b} = {result}")
        return result

    def power(self, a: Number, b: Number) -> Number:
        """Raise a to the power of b.
        
        Args:
            a: Base
            b: Exponent
            
        Returns:
            a raised to the power of b
        """
        result = power(a, b)
        self._add_to_history(f"{a} ^ {b} = {result}")
        return result

    def modulo(self, a: Number, b: Number) -> Number:
        """Calculate a modulo b.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Remainder of a divided by b
            
        Raises:
            DivisionByZeroError: If b is zero
        """
        result = modulo(a, b)
        self._add_to_history(f"{a} % {b} = {result}")
        return result

    def get_history(self) -> list:
        """Get the calculation history.
        
        Returns:
            List of calculation strings
        """
        return self.history.copy()

    def clear_history(self) -> None:
        """Clear the calculation history."""
        self.history.clear()

    def _add_to_history(self, operation: str) -> None:
        """Add an operation to history.
        
        Args:
            operation: String representation of the operation
        """
        self.history.append(operation)
