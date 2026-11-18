def within_and_has_double_quotes(s: str) -> bool:
    '''
    Return True if string s starts and ends with double quotes (") AND contains
    at least one double quote strictly inside the string (excluding the first
    and last characters); return False otherwise.
    Examples:
    >>> within_and_has_double_quotes('"abcd"efgh"')
    True
    >>> within_and_has_double_quotes('"abcdefgh"')
    False
    >>> within_and_has_double_quotes('\'abcd"efgh"\'')
    False
    '''
    

    if s.startswith('"') and s.endswith('"') and '"' in s[1:-1]:
        return True
    else:
        return False
print(within_and_has_double_quotes('"abcd"efgh"'))
print(within_and_has_double_quotes('"abcdefgh"'))
print(within_and_has_double_quotes("'abcd\"efgh\"'"))