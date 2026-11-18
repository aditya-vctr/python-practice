def is_dot_com_or_dot_in(domain: str) -> bool:
    '''
    Return True if the string domain ends with '.com' or '.in';
    return False otherwise.
    Examples:
    >>> is_dot_com_or_dot_in('example.com')
    True
    >>> is_dot_com_or_dot_in('study.iitm.ac.in')
    True
    >>> is_dot_com_or_dot_in('mywebsitein')
    False
    '''
    if domain.endswith(".com") or domain.endswith(".in"):
        return True
    else:
        return False
print(is_dot_com_or_dot_in('mywebsitein'))