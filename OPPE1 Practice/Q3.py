def square_and_clip(x: int, threshold: int) -> int:
    '''
    Square the given integer x and clip the result to threshold
    (if x squared exceeds threshold, return threshold; otherwise return x squared).
    Examples:
    >>> square_and_clip(5, 20)
    20
    >>> square_and_clip(3, 20)
    9
    '''
    x_sqr = x**2
    if x_sqr > threshold:
        return threshold
    else:
        return x_sqr
print(square_and_clip(5,20))
