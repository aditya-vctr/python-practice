def is_ten_digit_even(n: int) -> bool:
    '''
    Return True if n is a 10-digit even number (ignoring any negative sign),
    and False otherwise.
    Examples:
    >>> is_ten_digit_even(8769473839)
    False
    >>> is_ten_digit_even(9289479278)
    True
    '''
    if 1000000000<=abs(n) and n%2==0:
        return True
    else:
        return False
print(is_ten_digit_even(9289479278))