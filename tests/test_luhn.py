from app.core.luhn import validate_luhn, generate_luhn

def test_valid_luhn() -> None:
    # A known valid Luhn number (e.g., standard test cases)
    assert validate_luhn("18") is True
    assert validate_luhn("79927398713") is True
    assert validate_luhn("49927398716") is True

def test_invalid_luhn() -> None:
    assert validate_luhn("79927398714") is False

def test_non_digits() -> None:
    assert validate_luhn("1234-abcd") is False

def test_generate_luhn() -> None:
    # A known valid Luhn number (e.g., standard test cases)
    assert generate_luhn("1") == "8"
    assert generate_luhn("7992739871") == "3"
    assert generate_luhn("4992739871") == "6"

