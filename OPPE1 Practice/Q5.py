def is_positive_odd_or_negative_even(n: int) -> bool:
    '''
    Return True if integer n is either a positive odd number OR a negative even number;
    return False otherwise (note: 0 is neither positive nor negative).
    Examples:
    >>> is_positive_odd_or_negative_even(3)
    True
    >>> is_positive_odd_or_negative_even(-4)
    True
    >>> is_positive_odd_or_negative_even(0)
    False
    '''
    positive_odd = []
    negative_even = []
    if n > 0 and abs(n) % 2 ==1:
        positive_odd.append(n)
    if n<0 and abs(n)%2==0:
        negative_even.append(n)

    if (positive_odd) or (negative_even):
        return  True
    else:
        return False

print(is_positive_odd_or_negative_even(-3))
