def _calculate_luhn_sum(number: str) -> int:
    """Helper to reverse, double alternate digits, and calculate the Luhn sum."""
    digits = [int(d) for d in number]
    # Reverse to work right-to-left
    checksum = digits[::-1]

    # Double every second digit starting from index 1
    for i in range(1, len(checksum), 2):
        doubled = checksum[i] * 2
        checksum[i] = doubled - 9 if doubled > 9 else doubled
 
    return sum(checksum)

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
    luhn_sum = _calculate_luhn_sum(number+"0")
 
    # Calculate the digit needed to push the total sum to the next multiple of 10
    return str((10 - (luhn_sum % 10)) % 10)

