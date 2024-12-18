class Base:
    """Base class for inheritance hierarchy."""
    
    def base_method(self):
        return "base"

class Child(Base):
    """Child class inheriting from Base."""
    
    def child_method(self):
        return "child"
    
    def untested_child(self):
        return "untested"

class GrandChild(Child):
    """Grandchild class inheriting from Child."""
    
    def grand_child_method(self):
        return "grandchild"