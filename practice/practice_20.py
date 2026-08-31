def rotate_list(lst: list, k: int) -> list:
    '''
    Given a list of items and an integer k, rotate the list to the right by k steps.

    Arguments:
    lst: list - a list of items
    k: int - the number of steps to rotate the list to the right

    Return:
    list - the rotated list
    '''
    if not lst :
        return []
    # find the real number of moves
    effective_k = k % len(lst)

    if effective_k == 0:
        return lst

    right_part = lst[-effective_k:]
    left_part = lst[:-effective_k]

    return right_part + left_part

print(rotate_list([10,20,30,40,50], 2))