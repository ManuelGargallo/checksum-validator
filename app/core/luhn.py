# Pre-computed values for (digit * 2) - 9 if product > 9 else (digit * 2)
# Index:          0  1  2  3  4  5  6  7  8  9
_LUHN_DOUBLED = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)


def _calculate_luhn_sum(number: str) -> int:
    """Luhn sum using a look-up table and zero array allocations."""
    total = 0
    is_alternate = False
    for i in range(len(number) - 1, -1, -1):
        digit = int(number[i])
        total += _LUHN_DOUBLED[digit] if is_alternate else digit
        is_alternate = not is_alternate
    return total


def validate_luhn(number: str) -> bool:
    """Verifies a string of numbers using the Luhn Algorithm."""
    if not number.isdigit() or not number:
        return False
    return _calculate_luhn_sum(number) % 10 == 0


def generate_luhn(number: str) -> str:
    """Generates the missing check digit for a base number using the Luhn Algorithm."""
    if not number.isdigit() or not number:
        raise ValueError("Input must be a non-empty string of digits.")

    # Append a placeholder 0 where the check digit will live
    luhn_sum = _calculate_luhn_sum(number + "0")

    # Calculate the digit needed to push the total sum to the next multiple of 10
    return str((10 - (luhn_sum % 10)) % 10)
