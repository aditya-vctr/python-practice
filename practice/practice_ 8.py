# def percentage_increase(original, new):
#     '''Calculate the percentage increase from the original value to the new value.

#     Args:
#         original (float): The original value.
#         new (float): The new value.

#     Returns:
#         float: The percentage increase.

#     Examples:
#     >>> percentage_increase(50, 75)
#     50.0
#     >>> percentage_increase(80, 100)
#     25.0
#     '''
#     per_inc = ((new-original)/original)*100
#     return float(per_inc)
# print(percentage_increase(50,75))



# def is_ten_digit_even(n):
#     '''Returns True if the number is a 10 digit even number, False otherwise.

#     Args: 
#         n (int): The given number. 

#     Returns: 
#         bool : result as True or False. 

#     >>> is_ten_digit_even(8769473839)
#     False
#     >>> is_ten_digit_even(9289479278)
#     True
#     '''

#     if len(str(n)) != 10 and n % 2 == 0:
#         return True
#     return False

# print(is_ten_digit_even(7319653851))

def find_indices_of_element(l, elem):
    '''Find all indices of an element in a list.

    Args:
        l (list): The input list.
        elem: The element to find.

    Returns:
        list: A list of indices where the element is found.

    Examples:
    >>> find_indices_of_element([1, 2, 3, 2, 4], 2)
    [1, 3]
    >>> find_indices_of_element(['a', 'b', 'a', 'c'], 'a')
    [0, 2]
    '''
    indices = []
    for index, x in enumerate(l):
        if x == elem:
            indices.append(index)
    return indices
print(find_indices_of_element([1,2,3,4,5,6,7,8,9,0],5))
