def swap_adjacent_elements(t: tuple) -> tuple:
    '''
    Given an even-length tuple t, return a new tuple with every pair
    of adjacent elements swapped.
    Example:
    >>> swap_adjacent_elements((1, 2, 3, 4, 5, 6))
    (2, 1, 4, 3, 6, 5)
    '''
    result = []
    for i in range(0,len(t),2):
        result.append(t[i+1])
        result.append(t[i])
    return tuple(result)

print(swap_adjacent_elements((1, 2, 3, 4, 5, 6)))
