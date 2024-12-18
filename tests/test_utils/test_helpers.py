from src.utils.helpers import format_string, validate_input

def test_format_string():
    """Test string formatting helper"""
    assert format_string("  Hello  ") == "hello"
    assert format_string("WORLD") == "world"

def test_validate_input():
    """Test input validation helper"""
    assert validate_input(5) is True
    assert validate_input(0) is False
    assert validate_input(-1) is False