def arithmetic_operations(t: tuple) -> tuple:
    '''
    Given a tuple of two integers (a, b), return a tuple containing the 
    sum, difference, product, and quotient (integer division) of the two numbers.

    Arguments:
    t: tuple - a tuple of two integers (a, b)

    Return:
    tuple - a tuple containing the sum, difference, product, and quotient

    Example:
    >>> arithmetic_operations((1, 2))
    (3, -1, 2, 0)
    '''
    lst = list(t)
    result = []

    addition = lst[0] + lst[1]
    result.append(addition)

    subtraction = lst[0] - lst[1]
    result.append(subtraction)

    product = lst[0] * lst[1]
    result.append(product)

    quotient = lst[0] // lst[1]
    result.append(quotient)

    return tuple(result)

print(arithmetic_operations((1,2)))