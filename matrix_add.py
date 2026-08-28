#matrix addition
# import numpy as np
# a = np.array([
#     [2,4,7,5,9,2],
#     [5,9,6,1,2,3],
#     [5,5,6,5,5,4]
# ])

# b = np.array([
#     [7,6,5,1,7,0],
#     [5,1,2,4,5,7],
#     [1,2,3,4,5,6]
# ])

# print(a+b)

# Find the index of the row with maximum number of zeros in a matrix
matrix = [
    [1, 1, 1, 1],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0]
]
def row_index_with_most_numbers_of_zeros(matrix:list) -> int:
    max_zero = -1
    index = 0

    for i in range(len(matrix)):
        zeros= matrix[i].count(0)

        if zeros > max_zero:
            max_zero = zeros
            index = i
    return index
answer = row_index_with_most_numbers_of_zeros(matrix)
print(answer)
      