def surround_first_two_and_last_two_with_brackets(s: str) -> str:
    '''
    Given a string s of length at least 4, surround the first two characters
    and the last two characters with square brackets [].
    Examples:
    >>> surround_first_two_and_last_two_with_brackets("python")
    '[py]th[on]'
    >>> surround_first_two_and_last_two_with_brackets("four")
    '[fo][ur]'
    '''
    return ("[" + s[:2] + "]" + s[2:-2] + "["+ s[-2:] + "]")
print(surround_first_two_and_last_two_with_brackets("four"))
print(surround_first_two_and_last_two_with_brackets("python"))