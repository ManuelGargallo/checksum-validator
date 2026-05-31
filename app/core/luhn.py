def validate_luhn(number: str) -> bool:
    """Verifies a string of numbers using the Luhn Algorithm."""
    if not number.isdigit():
        return False
        
    digits = [int(d) for d in number]
    # Reverse the digits to work from right to left
    checksum = digits[::-1]
    
    # Double every second digit starting from the second to last
    for i in range(1, len(checksum), 2):
        checksum[i] *= 2
        if checksum[i] > 9:
            checksum[i] -= 9
            
    return sum(checksum) % 10 == 0
