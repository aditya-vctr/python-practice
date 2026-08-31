
def sort_tuples_by_second_then_third(input_list):
    """
    Args:
        input_list (list): The list of tuples to sort.
    Returns:
        list: The sorted list of tuples.
    """
    return sorted(input_list, key=lambda x: (x[1], x[2], x[0]))
print(sort_tuples_by_second_then_third([(0,2,0),(1,2,1),(-6,2,1),(0,2,1),(-9,1,0),(5,2,-1)]))