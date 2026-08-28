# Accept a positive integer n as input and print the first n positive integers, one number on each line
n = int(input("enter an integer: "))
for i in range(1, n+1):
     print(i)

# Accept an integer as input. Print positive if it is greater than zero and negative if it is less than zero. You can assume that the input will be non-zero.
n = int(input('Enter an integer: '))
if n > 0:
    print("Positive")
else:
    print('Negative')

'''Write a function is_positive_odd_or_negative_even that
 checks if an integer is either a positive
 odd number or a negative even number. Return True if the number meets
one of these conditions; otherwise, return False'''

def is_positive_odd_or_negative_even(n: int) -> bool:
    if (n % 2 == 1) and (n>0):
        return True
    if (n % 2 == 0) and (n<0):
        return True

    return False
n=int(input())
print(is_positive_odd_or_negative_even(n))

#Problem 1 - Data Types
'''
    Given two integers, find the absolute difference between 
    their sum and the sum of their squares.
    Eg. 
    a, b = 2,3 
    sum is 5
    sum of squares is 13 
    absolute difference is 8

    Args:
        a - int : The first integer.
        b - int : The second integer.

    Returns:
        int: absolute difference between the sum and the sum of squares
    '''
def abs_diff_between_sum_and_sum_of_squares(a: int, b: int) -> int:
    return abs((a + b) - (a ** 2 + b ** 2))


a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

# Call the function and store the result
result = abs_diff_between_sum_and_sum_of_squares(a, b)
print(result)

#Problem 2 - Data Types
'''
    Given three lists of same length, 
    interleave them together and return the interleaved list.

    Example:
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c']
        list3 = [(1,1),(2,2),(3,3)]
        output = [1, 'a', (1,1), 2, 'b', (2,2), 3, 'c', (3,3)]

    Args:
        list1 (list): The first list.
        list2 (list): The second list.
        list3 (list): The third list.

    Returns:
        list: A list containing interleaved elements from all three lists.
    '''

def interleave_lists(list1, list2, list3):
    interleaved_list = []
    for i in range(len(list1)):
        interleaved_list.append(list1[i])
        interleaved_list.append(list2[i])
        interleaved_list.append(list3[i])
    return interleaved_list


'''
    Given an odd-length string, 
    swap the parts before and after the middle three characters,
    while keeping the middle three characters in place.

    Assume the string has at least 5 characters.

    Examples:
        "firstabclast1" -> "last1abcfirst"
        "abcdefghi" -> "ghidefabc"

    Args:
        s (str): The input string of odd length.

    Returns:
        str: The modified string with the parts swapped.
    '''
def swap_except_middle_three(s: str) -> str:
    mid = len(s) // 2

    left = s[:mid-1]
    middle = s[mid-1:mid+2]
    right = s[mid+2:]

    return right + middle + left


  