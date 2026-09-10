'''
Write a recursive function named non_decreasing that accepts 
a non-empty list L of integers as argument and returns True 
if the elements are sorted in non-decreasing order from left 
to right, and False otherwise.
'''

def non_decreasing (L):
    """
    A recursive function that determines if L is sorted in non-decreasing
    order.
    Parameters:
    L: list of integers
    Return:
        result : bool 
    """
        # 1. THE BASE CASE
    # If the list has shrunk down to 1 item, it survived all checks!
    if len(L) <= 1:
        return True
        
    # 2. THE FAIL CONDITION
    # If the first number is bigger than the next, it's not non-decreasing.
    if L[0] > L[1]:
        return False
        
    # 3. THE RECURSIVE STEP
    # If they are in the right order, chop off the first item and check the rest
    else:
        return non_decreasing(L[1:])


print(non_decreasing([10,54,64,62,78,23])) #false