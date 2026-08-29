def average_of_numbers(lst: list) -> float:
    '''
    Given a list containing integers, floats, and strings, return the average 
    of the integers and floats, rounded to two decimal points. If neither 
    integers nor floats are present, return -1.

    Arguments:
    lst: list - a list containing integers, floats, and strings

    Return:
    float - the average of the integers and floats rounded to two decimal points,
            or -1 if no integers or floats are present

    Example:
    >>> average_of_numbers([1, 2.5, 'a', 3, 'b'])
    2.17
    >>> average_of_numbers(['a', 'b', 'c'])
    -1
    '''
    # 1. Setup Trackers: Create variables for the running total and the number count
    total = 0
    valid_number = 0
    # 2. Loop Through the List: Look at each item one by one
    for item in lst:
        # 3. Check the Data Type: We only want integers and floats
        # type(item) is safer here than isinstance() because it ignores booleans
        if type(item) in (int, float):
            total = total + item
            valid_number =  valid_number + 1
    # 5. Handle the "No Numbers" Case: If the count is still 0, return -1
    if valid_number == 0:
        return -1

    # 6. Calculate and Round: Divide total by count, and round to 2 decimal places
    average = total / valid_number
    return round(average, 2)

print(average_of_numbers(['a', 'b', 'c']))
print(average_of_numbers([1, 2.5, 'a', 3, 'b']))
