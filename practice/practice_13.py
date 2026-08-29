def not_present_in_both(lst1: list, lst2: list) -> list:
    '''
    Given two lists, return a list containing the items 
    that are present in either list 1 or list 2 but not in both.

    Arguments:
    lst1: list - the first list 
    lst2: list - the second list 

    Return:
    set - a set containing the items present in either list 1 or list 2 but not in both

    Example:
    >>> symmetric_difference([1, 2, 3], [3, 4, 5])
    {1, 2, 4, 5}
    '''
    set1 = set(lst1)
    set2 = set(lst2)
    result = set1 ^ set2
    return result

print(not_present_in_both([1, 2, 3], [3, 4, 5]))