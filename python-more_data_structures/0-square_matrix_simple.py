#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2 = []
    for row in matrix:
        row_2 = []
        for element in row:
            square = element ** 2
            row_2.append(square)
        matrix_2.append(row_2)
    return matrix_2
