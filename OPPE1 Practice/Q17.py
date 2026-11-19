def interleave_lists(list1: list, list2: list, list3: list) -> list:
    '''
    Given three lists of the same length, interleave their elements
    [list1[0], list2[0], list3[0], list1[1], ...] and return the new list.
    Example:
    >>> interleave_lists([1, 2], ['a', 'b'], [10, 20])
    [1, 'a', 10, 2, 'b', 20]
    '''
    result = []

    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])

    return result

print(interleave_lists([1, 2], ['a', 'b'], [10, 20]))
