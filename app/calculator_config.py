import os
from dotenv import load_dotenv
from app.exceptions import ConfigurationError

load_dotenv()


def validate_history_file(value):
    if not value:
        raise ConfigurationError("HISTORY_FILE cannot be empty")
    return value

HISTORY_FILE = validate_history_file(os.getenv("HISTORY_FILE", "history.csv"))