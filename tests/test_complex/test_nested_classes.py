from src.complex.nested_classes import Outer, Sibling

def test_outer():
    """Test outer class method"""
    outer = Outer()
    assert outer.outer_method() == "outer"

def test_inner():
    """Test inner class method"""
    inner = Outer.Inner()
    assert inner.inner_method() == "inner"

def test_deep_inner():
    """Test deeply nested class method"""
    deep = Outer.Inner.DeepInner()
    assert deep.deep_method() == "deep"

def test_sibling():
    """Test sibling class method"""
    sibling = Sibling()
    assert sibling.sibling_method() == "sibling"