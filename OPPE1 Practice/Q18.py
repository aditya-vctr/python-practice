def swap_even_and_odd_indices(lst: list) -> None:
    '''
    Swap adjacent elements at even and odd indices (0 with 1, 2 with 3, ...)
    IN-PLACE. Modify the list directly and return None.
    Example:
    >>> lst = [1, 2, 3, 4, 5, 6]; swap_even_and_odd_indices(lst); lst
    [2, 1, 4, 3, 6, 5]
    '''
    
    for i in range(0, len(lst), 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]

lst = [1, 2, 3, 4, 5, 6]
swap_even_and_odd_indices(lst)
print(lst)
