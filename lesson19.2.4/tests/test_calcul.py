import pytest
from app.calculator import Calculator
class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self,2, 2) == 4

    def test_subtraction(self):
        assert self.calc.subtraction(self,9, 3) == 6

    def test_multiply(self):
        assert self.calc.multiply(self,3, 2) == 6

    def test_division(self):
        assert self.calc.division(self,9,3) == 3
