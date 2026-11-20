def unique_chars_present_in_first_not_in_second(s1: str, s2: str) -> set:
    '''
    Return a set of unique characters present in s1 but NOT in s2.
    Example:
    >>> unique_chars_present_in_first_not_in_second("water", "watch")
    {'e', 'r'}
    '''
    result = set()
    for i in range(len(s1)):
        if s1[i] not in s2:
            result.add(s1[i])

    return result
print(unique_chars_present_in_first_not_in_second("water", "watch"))