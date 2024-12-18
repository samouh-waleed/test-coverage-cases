import pytest
from src.simple.basic_functions import add, subtract, divide

def test_add():
    """Test addition function"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    """Test subtraction function"""
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0

def test_divide():
    """Test division function"""
    assert divide(6, 2) == 3.0
    with pytest.raises(ValueError):
        divide(1, 0)