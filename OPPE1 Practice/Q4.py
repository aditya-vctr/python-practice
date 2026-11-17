def is_right_triangle_with_even_sides(a: int, b: int, c: int) -> bool:
    '''
    Check if the given positive sides (a, b, c) where c is the hypotenuse
    form a right triangle (a^2 + b^2 == c^2) AND both perpendicular sides a and b are even.
    Examples:
    >>> is_right_triangle_with_even_sides(6, 8, 10)
    True
    >>> is_right_triangle_with_even_sides(3, 4, 5)
    False
    '''
    if (a**2 + b**2 == c**2) and a%2==0 and b%2==0:
        return True
    else:
        return False
print(is_right_triangle_with_even_sides(3,4,5))