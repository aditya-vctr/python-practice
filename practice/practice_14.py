def modify_string_1(s: str) -> str:
    '''
    Given a string, Seperate the characters present in odd and even indices
    and return the merged string with even indices first and odd indices second in reverse order.

    Arguments:
    s: str - the input string

    Return:
    str - modified string

    Example:
    >>> modify_string_1('abcde')
    'acedb'
    >>> modify_string_1('python')
    'ptonhy'
    '''
    even = s[::2] # Grab all the even indices
    odd = s[1::2] # Grab all the odd indices
    reversed_odd = odd[::-1]
    return even + reversed_odd
print(modify_string_1('python'))
