def abs_diff_between_sum_and_sum_of_squares(a: int, b: int) -> int:
    '''
    Given two integers a and b, return the absolute difference between
    their sum and the sum of their squares.
    Examples:
    >>> abs_diff_between_sum_and_sum_of_squares(2, 3)
    8
    >>> abs_diff_between_sum_and_sum_of_squares(-2, 3)
    12
    '''

    sum = a + b
    squares = a ** 2 + b ** 2
    absolute_diff = abs(sum - squares)
    return absolute_diff

abs_diff_between_sum_and_sum_of_squares(2,3)