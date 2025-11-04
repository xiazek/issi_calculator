# skipping test method level docsrting requirement (test methods are self-documenting in most cases)
# pylint: disable=C0116

"""Unit tests for the `Calculator` class."""
from unittest import TestCase
from unittest.mock import patch

from calculator import Calculator, main


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


class TestMain(TestCase):
    """Test suite for verifying main function."""

    def test_main(self):
        """Test main function with valid arguments."""
        result = main(['5', '3'])
        assert result == 0

    @patch('sys.argv', ['calculator.py', '5', '3'])
    def test_main_with_none_argv(self):
        """Test main function with None argv (should read from sys.argv)."""
        result = main(None)
        assert result == 0

    def test_main_with_invalid_arguments(self):
        """Test main function with non-numeric arguments."""
        result = main(['abc', 'def'])
        assert result == 1

    def test_main_with_no_arguments(self):
        """Test main function with no arguments."""
        result = main([])
        assert result == 1

    def test_main_with_one_argument(self):
        """Test main function with only one argument."""
        result = main(['5'])
        assert result == 1

    def test_main_with_too_many_arguments(self):
        """Test main function with more than two arguments."""
        result = main(['5', '3', '2'])
        assert result == 1
