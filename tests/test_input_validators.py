import pytest
from app.input_validators import validate_number
from app.exceptions import InvalidNumberError


def test_validate_number():
    assert validate_number("5") == 5.0

def test_invalid_number():
    with pytest.raises(InvalidNumberError):
        validate_number("hello")