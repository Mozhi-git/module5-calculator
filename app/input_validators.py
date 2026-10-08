from app.exceptions import InvalidNumberError

def validate_number(value):
    try:
        return float(value)
    except ValueError:
        raise InvalidNumberError("Invalid number")

