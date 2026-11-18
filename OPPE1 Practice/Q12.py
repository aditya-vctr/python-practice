def is_odd_length_palindrome(s: str) -> bool:
    '''
    Return True if string s is both a palindrome and has an odd length;
    return False otherwise.
    Examples:
    >>> is_odd_length_palindrome("racecar")
    True
    >>> is_odd_length_palindrome("noon")
    False
    >>> is_odd_length_palindrome("nun")
    True
    '''
    if len(s) % 2 ==1:
        if s==s[::-1]:
            return True
    else:
        return False
print(is_odd_length_palindrome("noon"))