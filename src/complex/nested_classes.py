class Outer:
    """Outer class containing nested classes."""
    
    def outer_method(self):
        return "outer"
    
    class Inner:
        """Inner class nested within Outer."""
        
        def inner_method(self):
            return "inner"
        
        class DeepInner:
            """Deeply nested class within Inner."""
            
            def deep_method(self):
                return "deep"
            
            def untested_deep(self):
                return "untested"

class Sibling:
    """Sibling class at the same level as Outer."""
    
    def sibling_method(self):
        return "sibling"