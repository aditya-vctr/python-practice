def repeat(t: tuple) -> tuple:
    '''
    Given a 2-element tuple (a, b) of non-negative integers, return a tuple
    with a repeated b times followed by b repeated a times.
    Example:
    >>> repeat((2, 3))
    (2, 2, 2, 3, 3)
    '''
    a = t[0]
    b = t[1]
    return (a,) * b + (b,) * a
t = (2,3)
print(repeat(t))