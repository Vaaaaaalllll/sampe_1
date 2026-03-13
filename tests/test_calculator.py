# WARNING: template code, may need edits
"""Unit tests for the Calculator class."""

import pytest
from src.calculator import Calculator
from src.operations import DivisionByZeroError


class TestCalculator:
    """Test cases for Calculator class."""

    @pytest.fixture
    def calc(self):
        """Fixture to create a fresh Calculator instance for each test."""
        return Calculator()

    def test_calculator_initialization(self, calc):
        """Test that calculator initializes with empty history."""
        assert calc.get_history() == []

    def test_add_operation(self, calc):
        """Test addition operation."""
        result = calc.add(5, 3)
        assert result == 8
        assert "5 + 3 = 8" in calc.get_history()

    def test_subtract_operation(self, calc):
        """Test subtraction operation."""
        result = calc.subtract(10, 3)
        assert result == 7
        assert "10 - 3 = 7" in calc.get_history()

    def test_multiply_operation(self, calc):
        """Test multiplication operation."""
        result = calc.multiply(5, 3)
        assert result == 15
        assert "5 * 3 = 15" in calc.get_history()

    def test_divide_operation(self, calc):
        """Test division operation."""
        result = calc.divide(10, 2)
        assert result == 5.0
        assert "10 / 2 = 5.0" in calc.get_history()

    def test_divide_by_zero(self, calc):
        """Test division by zero raises error."""
        with pytest.raises(DivisionByZeroError):
            calc.divide(5, 0)

    def test_power_operation(self, calc):
        """Test power operation."""
        result = calc.power(2, 3)
        assert result == 8
        assert "2 ^ 3 = 8" in calc.get_history()

    def test_modulo_operation(self, calc):
        """Test modulo operation."""
        result = calc.modulo(10, 3)
        assert result == 1
        assert "10 % 3 = 1" in calc.get_history()

    def test_modulo_by_zero(self, calc):
        """Test modulo by zero raises error."""
        with pytest.raises(DivisionByZeroError):
            calc.modulo(5, 0)

    def test_history_tracking(self, calc):
        """Test that history tracks multiple operations."""
        calc.add(5, 3)
        calc.subtract(10, 2)
        calc.multiply(4, 5)
        
        history = calc.get_history()
        assert len(history) == 3
        assert "5 + 3 = 8" in history
        assert "10 - 2 = 8" in history
        assert "4 * 5 = 20" in history

    def test_clear_history(self, calc):
        """Test clearing history."""
        calc.add(5, 3)
        calc.subtract(10, 2)
        assert len(calc.get_history()) == 2
        
        calc.clear_history()
        assert calc.get_history() == []

    def test_history_immutability(self, calc):
        """Test that returned history is a copy."""
        calc.add(5, 3)
        history = calc.get_history()
        history.append("fake entry")
        
        # Original history should not be modified
        assert "fake entry" not in calc.get_history()

    def test_float_operations(self, calc):
        """Test operations with float numbers."""
        result = calc.add(2.5, 3.7)
        assert result == pytest.approx(6.2)
        
        result = calc.multiply(2.5, 4)
        assert result == pytest.approx(10.0)

    def test_negative_numbers(self, calc):
        """Test operations with negative numbers."""
        result = calc.add(-5, -3)
        assert result == -8
        
        result = calc.multiply(-5, 3)
        assert result == -15
