from functools import wraps

def debug_decorator(func):
    """Debug decorator that prints function entry and exit."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

@debug_decorator
def sample_function():
    """Sample function using the debug decorator."""
    return "sample"