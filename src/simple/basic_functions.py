def add(a: int, b: int) -> int:
    """Simple addition function"""
    return a + b

def subtract(a: int, b: int) -> int:
    """Simple subtraction function"""
    return a - b

def multiply(a: int, b: int) -> int:
    """Simple multiplication function - untested"""
    return a * b

def divide(a: int, b: int) -> float:
    """Simple division function - partially tested"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b