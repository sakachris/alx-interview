#!/usr/bin/python3
''' 0-rotate_2d_matrix.py '''


def rotate_2d_matrix(matrix):
    ''' rotates 2d matrix 90 degrees clockwise '''
    n = len(matrix)

    # Transposing the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reversing each row
    for row in matrix:
        row.reverse()
