from app.core.luhn import validate_luhn

def test_valid_luhn():
    # A known valid Luhn number (e.g., standard test cases)
    assert validate_luhn("79927398713") is True

def test_invalid_luhn():
    assert validate_luhn("79927398714") is False

def test_non_digits():
    assert validate_luhn("1234-abcd") is False
