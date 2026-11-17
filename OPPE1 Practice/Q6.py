def is_even_two_digit_number(num: int) -> bool:
    '''
    Return True if num is an even two-digit number (ignoring any negative sign),
    and False otherwise.
    Examples:
    >>> is_even_two_digit_number(42)
    True
    >>> is_even_two_digit_number(-48)
    True
    >>> is_even_two_digit_number(99)
    False
    >>> is_even_two_digit_number(5)
    False
    '''
    if 10<=abs(num) and num% 2==0:
        return True
    else:
        return False
print(is_even_two_digit_number(-48))