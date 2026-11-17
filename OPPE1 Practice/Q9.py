def percentage_increase(original: float, new: float) -> float:
    '''
    Calculate and return the percentage increase from original to new.
    Examples:
    >>> percentage_increase(50, 75)
    50.0
    >>> percentage_increase(80, 100)
    25.0
    '''
    incr = float(new - original)
    percentage_increase = float((incr*100)/original)
    return percentage_increase
print(percentage_increase(80,158))