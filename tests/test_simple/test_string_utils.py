import pytest
from src.simple.string_utils import StringUtils

def test_reverse():
    assert StringUtils.reverse("hello") == "olleh"
    assert StringUtils.reverse("python") == "nohtyp"
    assert StringUtils.reverse("") == ""

def test_capitalize_words():
    assert StringUtils.capitalize_words("hello world") == "Hello World"
    assert StringUtils.capitalize_words("python test") == "Python Test"
    assert StringUtils.capitalize_words("") == ""

def test_remove_spaces():
    assert StringUtils.remove_spaces("hello world") == "helloworld"
    assert StringUtils.remove_spaces("  python  test  ") == "pythontest"
    assert StringUtils.remove_spaces("") == ""