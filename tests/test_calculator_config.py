import pytest
from app.calculator_config import HISTORY_FILE, validate_history_file
from app.exceptions import ConfigurationError

def test_history_file():
    assert HISTORY_FILE == "history.csv"

def test_empty_history_file():
    with pytest.raises(ConfigurationError):
        validate_history_file("")