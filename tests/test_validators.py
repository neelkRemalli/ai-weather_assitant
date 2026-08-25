import pytest

from src.utils.validators import validate_location


def test_validate_location():
    assert validate_location(" London ") == "London"


def test_empty_location():
    with pytest.raises(ValueError):
        validate_location("")