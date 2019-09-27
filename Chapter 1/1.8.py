import numpy as np

# this is grossly inefficient
def zero_matrix(matrix):
    row_count = len(matrix)
    column_count = len(matrix[0])
    
    zeroed_matrix = [[0] * column_count for i in range(row_count)]
    indexes_to_zero = []

    # O(r)
    for r in range(row_count):
        # O(c)
        for c in range(column_count):
            if matrix[r][c] == 0:
                # O(r)
                for i in range(row_count):
                    indexes_to_zero.append((i, c))

                # O(c)
                for i in range(column_count):
                    indexes_to_zero.append((r, i))
            else:
                zeroed_matrix[r][c] = matrix[r][c]

    for index in indexes_to_zero:
        zeroed_matrix[index[0]][index[1]] = 0

    print(np.matrix(zeroed_matrix))

matrix = [[1, 2, 3, 4], [4, 0, 6, 6], [7, 8, 9, 0]]
zero_matrix(matrix)
