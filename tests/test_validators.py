import pytest
from src.validators import validate_title, validate_status


def test_valid_title():
    assert validate_title("Task") == "Task"


def test_invalid_title():
    with pytest.raises(Exception):
        validate_title("aa")


def test_valid_status():
    assert validate_status(True) is True


def test_invalid_status():
    with pytest.raises(Exception):
        validate_status("yes")