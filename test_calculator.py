# skipping test method level docsrting requirement (test methods are self-documenting in most cases)
# pylint: disable=C0116

"""Unit tests for the `Calculator` class."""
from unittest import TestCase

import pytest
from pytest import approx

from calculator import Calculator, demo


class TestCalculator(TestCase):
    """Basic tests of `Calculator` arithmetic operations."""

    def test_calculator_subtract(self):
        calc = Calculator(5, 1.7)
        self.assertAlmostEqual(calc.subtract(), 3.3, places=7)

    def test_calculator_multiply(self):
        calc = Calculator(5.2, 3.0)
        self.assertAlmostEqual(calc.multiply(), 15.6)

    def test_calculator_divide(self):
        calc = Calculator(5, 3)
        self.assertAlmostEqual(calc.divide(), 1.666666667, places=7)

    def test_calculator_divide_by_zero(self):
        """Calculator.divide should return None when dividing by zero."""
        calc = Calculator(5, 0)
        self.assertIsNone(calc.divide())


class TestCalculatorForNumbers:
    """tests via `Calculator.for_numbers` that takes care about type casting to float"""

    def test_init(self):
        calc = Calculator.for_numbers(5.0, 3.0)
        assert isinstance(calc, Calculator)

    def test_init_with_not_numbers(self):
        calc = Calculator.for_numbers("wrong-parameter", 3)
        assert calc is None

    @pytest.mark.parametrize(
        "op1, op2, expected",
        [
            (5, 3.2, 8.2),
            (5.2, 3.0, 8.2),
            ("5.2", "3.0", 8.2),
        ],
    )
    def test_sum(self, op1, op2, expected):
        calc = Calculator.for_numbers(op1, op2)
        assert calc.sum() == approx(expected)

    @pytest.mark.parametrize(
        "op1, op2, expected",
        [
            (5, 3.2, 1.8),
            (5.2, 3.0, 2.2),
            ("5.2", "3.0", 2.2),
        ],
    )
    def test_subtract(self, op1, op2, expected):
        calc = Calculator.for_numbers(op1, op2)
        assert calc.subtract() == approx(expected)

    @pytest.mark.parametrize(
        "op1, op2, expected",
        [
            (5, 3.2, 16.0),
            (5.2, 3.0, 15.6),
            ("5.2", "3.0", 15.6),
        ],
    )
    def test_multiply(self, op1, op2, expected):
        calc = Calculator.for_numbers(op1, op2)
        assert calc.multiply() == approx(expected)

    @pytest.mark.parametrize(
        "op1, op2, expected",
        [
            (5, 3.0, 5 / 3.0),
            (5.2, 3.0, 5.2 / 3.0),
            ("5.2", "3.0", 5.2 / 3.0),
        ],
    )
    def test_divide(self, op1, op2, expected):
        calc = Calculator.for_numbers(op1, op2)
        assert calc.divide() == approx(expected)

    @pytest.mark.parametrize(
        "op1, op2",
        [
            (5, 0),
            ("5.2", 0),
            (0, 0),
        ],
    )
    def test_divide_by_zero(self, op1, op2):
        calc = Calculator.for_numbers(op1, op2)
        assert calc.divide() is None


class TestDemo(TestCase):
    """Test suite for verifying main function."""

    def test_demo(self):
        """Test main with valid arguments."""
        result = demo(15.2, 3.0)
        assert result == approx(18.2)

