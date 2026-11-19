def remove_elements_at_two_indices(l: list, i1: int, i2: int) -> None:
    '''
    Remove the elements at two distinct non-negative indices i1 and i2
    from list l IN-PLACE. Do not return a new list.
    Example:
    >>> lst = [1, 2, 3, 4, 5, 6, 7]; remove_elements_at_two_indices(lst, 5, 1); lst
    [1, 3, 4, 5, 7]
    '''
    l.pop(max(i1,  i2))
    l.pop(min(i1, i2))

    return l
lst = [1, 2, 3, 4, 5, 6, 7]
print(remove_elements_at_two_indices(lst, 5, 1))