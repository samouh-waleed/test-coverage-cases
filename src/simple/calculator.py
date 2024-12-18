class Calculator:
    """A simple calculator class with basic operations."""
    
    def __init__(self):
        self.value = 0
    
    def add(self, x: int) -> None:
        """Add to current value"""
        self.value += x
    
    def subtract(self, x: int) -> None:
        """Subtract from current value"""
        self.value -= x
    
    def get_value(self) -> int:
        """Get current value"""
        return self.value
    
    def reset(self) -> None:
        """Reset calculator - untested"""
        self.value = 0