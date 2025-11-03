from unittest import TestCase
from calculator import Calculator


class TestCalculator(TestCase):

    def test_calculator_sum(self):
        calc = Calculator(5, 3)
        assert calc.sum() == 8

    def test_calculator_substract(self):
        calc = Calculator(5, 3)
        assert calc.substract() == 2

    def test_calculator_multiply(self):
        calc = Calculator(5, 3)
        assert calc.multiply() == 15

    def test_calculator_divide(self):
        calc = Calculator(5, 3)
        assert calc.divide() == 1.6666666666666667

    def test_calculator_divide_by_zero(self):
        calc = Calculator(5, 0)
        self.assertIsNone(calc.divide())

