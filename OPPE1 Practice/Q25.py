def manhattan_distance_via_b(a: tuple, b: tuple, c: tuple) -> int:
    '''
    Given three 2D points a, b, and c, return the total Manhattan distance
    to travel from a to b and then from b to c.
    Example:
    >>> manhattan_distance_via_b((0, 0), (3, 4), (6, 8))
    14
    '''
    distance_ab = abs(b[0]-a[0]) + abs(b[1]-a[1])
    distance_bc = abs(c[0]-b[0]) + abs(c[1]-b[1])
    return distance_ab + distance_bc
print(manhattan_distance_via_b((0, 0), (3, 4), (6, 8)))