def number_of_unique_common_digits(n1: int, n2: int) -> int:
    '''
    Return the count of unique digits that appear in both integers n1 and n2
    (ignoring any negative signs).
    Example:
    >>> number_of_unique_common_digits(287498, 295424)
    3
    '''
    n1  = abs(n1)
    n2 = abs(n2)

    digit1 = []
    digit2 = []

    for i in range(len(str(n1))):
        if str(n1)[i] not in digit1:
            digit1.append(str(n1)[i])

    for i in range(len(str(n2))):
        if str(n2)[i] not in digit2:
            digit2.append(str(n2)[i])

    count = 0

    for i in range(len(digit1)):
        if digit1[i] in digit2:
            count += 1

    return count

print(number_of_unique_common_digits(287498, 295424))
