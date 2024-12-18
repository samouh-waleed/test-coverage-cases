def format_string(text: str) -> str:
    """Format string helper"""
    return text.strip().lower()

def validate_input(value: int) -> bool:
    """Validate input helper"""
    return isinstance(value, int) and value > 0

def untested_helper(data: dict) -> list:
    """Untested helper function"""
    return list(data.keys())