# skipping test method level docsrting requirement (test methods are self-documenting in most cases)
# pylint: disable=C0116

"""Unit tests for the `Calculator` class."""
from unittest import TestCase
from calculator import Calculator


class TestCalculator(TestCase):
    """Test suite for verifying `Calculator` arithmetic operations."""

    def test_calculator_sum(self):
        calc = Calculator(5, 3)
        assert calc.sum() == 8

    def test_calculator_subtract(self):
        calc = Calculator(5, 3)
        assert calc.subtract() == 2

    def test_calculator_multiply(self):
        calc = Calculator(5, 3)
        assert calc.multiply() == 15

    def test_calculator_divide(self):
        calc = Calculator(5, 3)
        assert calc.divide() == 1.6666666666666667

    def test_calculator_divide_by_zero(self):
        """Calculator.divide should return None when dividing by zero."""
        calc = Calculator(5, 0)
        self.assertIsNone(calc.divide())
