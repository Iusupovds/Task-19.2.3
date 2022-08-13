import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_addition_calculate_correctly(self):
        assert self.calc.addition(self, 1, 2) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 3, 1) == 2

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 5) == 10

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 3) == 2
