def most_frequent_element(lst: list) -> int:
    '''
    Arguments:
    lst: list - a list of integers

    Return:
    int - the integer that occurs most frequently, or the largest one
          if there are multiple with the same frequency

    Example:
    >>> most_frequent_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    4
    
    '''
    # create an empty dictionary to track frequencies
    counts = {}
    # loop through the list to count every number
    for num in lst:
        if num in counts:
            counts[num] = counts[num]+1
        else:
            counts[num] = 1
    # setup variable to track the current winner
    max_count = 0
    best_num = 0

    # loop through our dictionary (keys and values at the same time)
    for num, count in counts.items():
        if count > max_count:
            max_count= count
            best_num = num
        elif count == max_count:
            if num>best_num:
                best_num =  num
    return best_num
print(most_frequent_element([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))