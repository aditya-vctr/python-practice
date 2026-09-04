def is_dot_com_or_dot_in(domain):
    """
    Checks whether a given domain ends with '.com' or '.in'.

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain ends with '.com' or '.in', False otherwise.

    Examples:
        >>> is_dot_com_or_dot_in('example.com')
        True
        >>> is_dot_com_or_dot_in('example.in')
        True
        >>> is_dot_com_or_dot_in('example.org')
        False
        >>> is_dot_com_or_dot_in('mywebsitein')
        False
    """
    if domain.endswith('.com') or domain.endswith('.in'):
        return True
    else:
        return False
print(is_dot_com_or_dot_in('abcd@gmail.com'))  #True
print(is_dot_com_or_dot_in('mywebsite.in'))    #True
print(is_dot_com_or_dot_in('example.org'))     #False