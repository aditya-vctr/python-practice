def count_positive_ignore_none(nums: list) -> int:
    '''
    Given a list nums containing integers and possibly None values,
    return the count of strictly positive integers (> 0) while safely
    ignoring None and 0.
    Examples:
    >>> count_positive_ignore_none([1, -2, 3, 0, None, 4])
    3
    >>> count_positive_ignore_none([None, 0, -5])
    0
    '''
    count = 0
    for i in range(len(nums)):
        if nums[i] is not None and nums[i]>0:
            count = count + 1
    return count
print(count_positive_ignore_none([1, -2, 3, 0, None, 4]))