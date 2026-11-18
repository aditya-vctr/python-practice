def lowercase_first_half_and_uppercase_second_half(s: str) -> str:
    '''
    Given an even-length string s, return a new string with the first half
    converted to lowercase and the second half converted to uppercase.
    Examples:
    >>> lowercase_first_half_and_uppercase_second_half("HELLOworld")
    'helloWORLD'
    >>> lowercase_first_half_and_uppercase_second_half("Pytho
    nCODE")
    'pythONCODE'
    '''
    n = len(s)
    mid = n//2

    first_half = s[:mid].lower()
    second_half = s[mid:].upper()
    return first_half + second_half

print(lowercase_first_half_and_uppercase_second_half("HELLOworld"))
print(lowercase_first_half_and_uppercase_second_half("PythonCODE"))