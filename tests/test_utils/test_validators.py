import pytest
from src.utils.validators import Validators

def test_is_valid_email():
    assert Validators.is_valid_email("test@example.com")
    assert Validators.is_valid_email("user.name@domain.co.uk")
    assert not Validators.is_valid_email("invalid.email")
    assert not Validators.is_valid_email("@domain.com")

def test_is_valid_phone():
    assert Validators.is_valid_phone("1234567890")
    assert Validators.is_valid_phone("+11234567890")
    assert not Validators.is_valid_phone("123")
    assert not Validators.is_valid_phone("abcdefghijk")

def test_is_within_range():
    assert Validators.is_within_range(5, 0, 10)
    assert Validators.is_within_range(0, 0, 10)
    assert Validators.is_within_range(10, 0, 10)
    assert not Validators.is_within_range(-1, 0, 10)
    assert not Validators.is_within_range(11, 0, 10)