'''Part B: String, Case Conversion & Format Validation'''

def swap_except_middle_three(s: str) -> str:
    '''
    Given an odd-length string s (length >= 3), swap the substring before
    the middle three characters with the substring after the middle three characters,
    keeping the middle three characters in place.
    Examples:
    >>> swap_except_middle_three("abcdefghi")
    'ghidefabc'
    >>> swap_except_middle_three("firstabclast1")
    'last1abcfirst'
    '''
    mid = len(s)//2
    left = s[:mid-1]
    middle = s[mid-1:mid+2]
    right = s[mid+2:]

    return right + middle + left
print(swap_except_middle_three("firstabclast1"))