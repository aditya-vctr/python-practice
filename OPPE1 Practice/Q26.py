def has_more_than_5_unique_digits(num: int) -> bool:
    '''
    Return True if integer num has strictly more than 5 unique digits
    (ignoring any negative sign), and False otherwise.
    Examples:
    >>> has_more_than_5_unique_digits(123456)
    True
    >>> has_more_than_5_unique_digits(112233)
    False
    '''

    num = abs(num)
    digit = []
    for i in range(len(str(num))):
        if str(num)[i] not in digit:
            digit.append(str(num)[i])

    if len(digit)>5:
            return True
    else:
        return False
print(has_more_than_5_unique_digits(123456789))