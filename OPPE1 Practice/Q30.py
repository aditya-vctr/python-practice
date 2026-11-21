def remove_keys_not_in_list(d: dict, l: list) -> None:
    '''
    Remove all keys from dictionary d that are NOT present in list l IN-PLACE.
    Do not return anything.
    Example:
    >>> d = {'a': 1, 'b': 2, 'c': 3}; remove_keys_not_in_list(d, ['a', 'c']); d
    {'a': 1, 'c': 3}
    '''
    remove_keys = []

    for key in d:
        if key not in l:
            remove_keys.append(key)

    for key in remove_keys:
        d.pop(key)

    