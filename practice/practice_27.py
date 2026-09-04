# Check if the given element is present in opposite halves

def is_present_in_opposite_halves(elem, l1: list, l2: list):
    """
    Determines whether an element is present in the first half of one list 
    and the second half of the other list, or vice versa.

    Args:
        elem (Any): The element to check for.
        l1 (list): The first list to search.
        l2 (list): The second list to search.

    Returns:
        bool: True if `elem` is present in opposite halves of `l1` and `l2`, 
        False otherwise.
    """

    # Find the exact middle index 
    mid_l1 = len(l1) // 2
    mid_l2 = len(l2) // 2

    # cutting list into halves
    first_halve_l1 = l1[:mid_l1]
    second_halve_l1 = l1[mid_l1:]

    first_halve_l2 = l2[:mid_l2]
    second_halve_l2 = l2[mid_l2:]

    if elem in first_halve_l1 and elem in second_halve_l2:
        return True
    if elem in second_halve_l1 and elem in first_halve_l2:
        return True
    else:
        return False

print(is_present_in_opposite_halves(3, [1, 2, 3, 4], [5, 6, 3, 8]))  #False
print(is_present_in_opposite_halves(6, [5, 6, 7, 8], [1, 2, 6, 4]))  #True
print(is_present_in_opposite_halves(6, [5, 7, 6, 8], [1, 6, 2, 4]))  #True
