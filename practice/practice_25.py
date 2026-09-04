#  Check If Even Two-Digit Number
def is_even_two_digit_number(num):
    """
    Determines whether a given number is an even two-digit number.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if `num` is an even two-digit number, False otherwise.

    Examples:
        >>> is_even_two_digit_number(42)
        True
        >>> is_even_two_digit_number(99)
        False
        >>> is_even_two_digit_number(-48)
        True
        >>> is_even_two_digit_number(5)
        False
    """
    is_two_digit =  10 <= abs(num) <= 99
    is_even = num % 2 == 0

    if is_two_digit and is_even:
        return True
    return False

print(is_even_two_digit_number(24)) # True
print(is_even_two_digit_number(85)) # False