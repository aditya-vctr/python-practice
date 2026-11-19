def find_indices_of_element(l: list, elem) -> list:
    '''
    Return a list of all 0-based indices where elem occurs in list l.
    Examples:
    >>> find_indices_of_element([1, 2, 3, 2, 4], 2)
    [1, 3]
    >>> find_indices_of_element(['a', 'b', 'c'], 'z')
    []
    '''
    result = []
    for i in range(len(l)):
        if l[i]  == elem:
            result.append(i)

    return result

print(find_indices_of_element([1, 2, 3, 2, 4], 2))

