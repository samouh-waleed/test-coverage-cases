import pytest
from src.simple.calculator import Calculator

def test_calculator_add():
    """Test calculator add method"""
    calc = Calculator()
    calc.add(5)
    assert calc.get_value() == 5

def test_calculator_subtract():
    """Test calculator subtract method"""
    calc = Calculator()
    calc.add(10)
    calc.subtract(3)
    assert calc.get_value() == 7

def test_calculator_get_value():
    """Test calculator get_value method"""
    calc = Calculator()
    assert calc.get_value() == 0
    calc.add(5)
    assert calc.get_value() == 5