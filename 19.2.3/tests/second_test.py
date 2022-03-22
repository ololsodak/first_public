import pytest
import sys
sys.path.append('..')
print(sys.path)
from calculator import Calculator
class TestCalc:
    def setup(self):
        self.calc = Calculator #подключаем тестируемый объект класс Calculator

    def test_calc_multiply_correctly(self):  #  тест на корректность умножения
        assert self.calc.multiply(self, 4, 5) == 20

    def test_calc_division_correctly(self):  # тест на корректность деления
        assert self.calc.division(self, 15, 3) == 5.0

    def test_calc_subtraction_correctly(self):  # тест на корректность вычитания
        assert self.calc.subtraction(self, 6, 5) == 1

    def test_calc_adding_correctly(self): # тест на корректность  сложения
        assert self.calc.adding(self, 4, 5) == 9

