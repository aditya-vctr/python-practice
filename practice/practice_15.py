def create_count_dict(lst1: list, lst2: list) -> dict:
    '''
    Given two lists, lst1 and lst2, return a dictionary where each item 
    of lst1 is the key and the corresponding value is the count of that 
    item in lst2.

    Arguments:
    lst1: list - the first list of items to be used as keys
    lst2: list - the second list of items from which to count occurrences

    Return:
    dict - a dictionary with items from lst1 as keys and their counts in lst2 as values

    Example:
    >>> create_count_dict(['a', 'b', 'c'], ['a', 'b', 'a', 'a', 'c', 'c', 'c'])
    {'a': 3, 'b': 1, 'c': 3}
    '''
    result = {}
    for item in lst1:
        result[item] = lst2.count(item)
    return result
print(create_count_dict(['a', 'b', 'c'], ['a', 'b', 'a', 'a', 'c', 'c', 'c']))