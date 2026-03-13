# WARNING: template code, may need edits
"""Unit tests for the operations module."""

import pytest
from src.operations import (
    add,
    subtract,
    multiply,
    divide,
    power,
    modulo,
    DivisionByZeroError,
)


class TestAddition:
    """Test cases for addition operation."""

    def test_add_positive_numbers(self):
        assert add(5, 3) == 8

    def test_add_negative_numbers(self):
        assert add(-5, -3) == -8

    def test_add_mixed_numbers(self):
        assert add(5, -3) == 2

    def test_add_floats(self):
        assert add(2.5, 3.7) == pytest.approx(6.2)

    def test_add_zero(self):
        assert add(5, 0) == 5


class TestSubtraction:
    """Test cases for subtraction operation."""

    def test_subtract_positive_numbers(self):
        assert subtract(10, 3) == 7

    def test_subtract_negative_numbers(self):
        assert subtract(-5, -3) == -2

    def test_subtract_mixed_numbers(self):
        assert subtract(5, -3) == 8

    def test_subtract_floats(self):
        assert subtract(5.5, 2.2) == pytest.approx(3.3)

    def test_subtract_zero(self):
        assert subtract(5, 0) == 5


class TestMultiplication:
    """Test cases for multiplication operation."""

    def test_multiply_positive_numbers(self):
        assert multiply(5, 3) == 15

    def test_multiply_negative_numbers(self):
        assert multiply(-5, -3) == 15

    def test_multiply_mixed_numbers(self):
        assert multiply(5, -3) == -15

    def test_multiply_floats(self):
        assert multiply(2.5, 4) == pytest.approx(10.0)

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0


class TestDivision:
    """Test cases for division operation."""

    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5.0

    def test_divide_negative_numbers(self):
        assert divide(-10, -2) == 5.0

    def test_divide_mixed_numbers(self):
        assert divide(10, -2) == -5.0

    def test_divide_floats(self):
        assert divide(7.5, 2.5) == pytest.approx(3.0)

    def test_divide_by_zero(self):
        with pytest.raises(DivisionByZeroError):
            divide(5, 0)

    def test_divide_zero_by_number(self):
        assert divide(0, 5) == 0.0


class TestPower:
    """Test cases for power operation."""

    def test_power_positive_exponent(self):
        assert power(2, 3) == 8

    def test_power_zero_exponent(self):
        assert power(5, 0) == 1

    def test_power_negative_exponent(self):
        assert power(2, -2) == pytest.approx(0.25)

    def test_power_float_base(self):
        assert power(2.5, 2) == pytest.approx(6.25)

    def test_power_float_exponent(self):
        assert power(4, 0.5) == pytest.approx(2.0)


class TestModulo:
    """Test cases for modulo operation."""

    def test_modulo_positive_numbers(self):
        assert modulo(10, 3) == 1

    def test_modulo_negative_dividend(self):
        assert modulo(-10, 3) == 2

    def test_modulo_negative_divisor(self):
        assert modulo(10, -3) == -2

    def test_modulo_floats(self):
        assert modulo(7.5, 2.5) == pytest.approx(0.0)

    def test_modulo_by_zero(self):
        with pytest.raises(DivisionByZeroError):
            modulo(5, 0)

    def test_modulo_zero(self):
        assert modulo(0, 5) == 0
