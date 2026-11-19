def add_the_middle_element_to_both_ends(l: list) -> None:
    '''
    Given an odd-length list l, insert the middle element at both the start
    and the end of l IN-PLACE. Do not return a new list.
    Example:
    >>> lst = [1, 2, 3, 4, 5]; add_the_middle_element_to_both_ends(lst); lst
    [3, 1, 2, 3, 4, 5, 3]
    '''
    mid = l[len(l)//2]
    l.insert(0,mid)
    l.append(mid)
    return  l

print(add_the_middle_element_to_both_ends([1, 2, 3, 4, 5]))