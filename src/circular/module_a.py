from .module_b import function_b

def function_a():
    """Function A that calls function B."""
    return function_b() + " from A"