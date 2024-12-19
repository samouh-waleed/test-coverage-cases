import pytest
from src.simple.math_operations import MathOperations

def test_sum_list():
    assert MathOperations.sum_list([1, 2, 3]) == 6
    assert MathOperations.sum_list([]) == 0
    assert MathOperations.sum_list([1.5, 2.5]) == 4.0

def test_average():
    assert MathOperations.average([1, 2, 3]) == 2.0
    assert MathOperations.average([1, 2, 3, 4]) == 2.5
    with pytest.raises(ValueError):
        MathOperations.average([])

def test_factorial():
    assert MathOperations.factorial(0) == 1
    assert MathOperations.factorial(1) == 1
    assert MathOperations.factorial(5) == 120
    with pytest.raises(ValueError):
        MathOperations.factorial(-1)