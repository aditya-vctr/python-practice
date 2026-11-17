# Q8 [Sep Set 2]
def sum_of_floored_to_tens(a: int, b: int) -> int:
    '''
    Given two non-negative integers a and b, return the sum of the two numbers
    after flooring each to the nearest lower multiple of 10.
    Examples:
    >>> sum_of_floored_to_tens(35, 46)
    70
    >>> sum_of_floored_to_tens(0, 105)
    100
    '''
    lower_a = a//10 *10
    lower_b = b//10 *10
    sum_floored = lower_a +lower_b
    return sum_floored
print(sum_of_floored_to_tens(0,105))