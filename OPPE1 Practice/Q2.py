def sum_squares_abs_diff_squares(a: int, b: int) -> tuple:
    '''
    Given two integers a and b, return a tuple containing:
    (sum of their squares, absolute difference of their squares).
    Examples:
    >>> sum_squares_abs_diff_squares(3, 4)
    (25, 7)
    >>> sum_squares_abs_diff_squares(2, 5)
    (29, 21)
    '''
    sum_sqr = a ** 2 + b** 2
    sqr_diff = abs(a**2 - b**2)
    return sum_sqr,sqr_diff
print(sum_squares_abs_diff_squares(3,4))