# Check if Either of Two Number is a Multiple of the other

def is_multiple(a: int, b: int) -> bool:
    '''
    Given two integers, check if either is a multiple of the other.

    Eg.
    is_multiple(10, 5) -> True
    is_multiple(6, 18) -> True
    is_multiple(7, 3) -> False
    is_multiple(8, 16) -> True

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        bool: True if either is a multiple of the other, else False.
    '''
    if a > b:
        if a % b ==0:
            return True
        return False
    if b > a:
        if b % a == 0:
            return True
        return False
print(is_multiple(10,5))
print(is_multiple(7,3))