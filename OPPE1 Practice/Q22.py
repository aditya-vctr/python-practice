def is_present_in_opposite_halves(elem, l1: list, l2: list) -> bool:
    '''
    Given two even-length lists l1 and l2, return True if elem is present
    in the first half of l1 AND the second half of l2, OR in the second half
    of l1 AND the first half of l2. Return False otherwise.
    Examples:
    >>> is_present_in_opposite_halves(6, [5, 6, 7, 8], [1, 2, 6, 4])
    True
    >>> is_present_in_opposite_halves(3, [1, 2, 3, 4], [5, 6, 3, 8])
    False
    '''
    n = len(l1)
    mid_l1 = n // 2
    m = len(l2)
    mid_l2 = m //2 
    l1_first_half = l1[:mid_l1]
    l1_second_half = l1[mid_l1:]
    l2_first_half  = l2[:mid_l2]
    l2_second_half = l2[mid_l2:]

    if elem  in l1_first_half and elem in l2_second_half:
        return True
    if elem in l1_second_half and elem in l2_first_half:
        return True
    return False

print(is_present_in_opposite_halves(3, [1, 2, 3, 4], [5, 6, 3, 8]))