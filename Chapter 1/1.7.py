import numpy as np

def rotate_matrix(matrix):
    # intialize n by n matrix with zeroes using a list comprehension
    rotated_matrix = [[0] * len(matrix) for i in range(len(matrix))]
    
    column = 0
    
    for row in matrix:
        for i in range(len(row)):
            rotated_matrix[i][column] = row[i]
        
        column += 1

    # using numpy to nicely print the rotated matrix
    print(np.matrix(rotated_matrix))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate_matrix(matrix)
