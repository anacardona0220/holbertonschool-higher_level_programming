#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = list()
    for i in range(0, len(matrix)):
        new_list.append(list(map(lambda x: x**2, matrix[i])))
    return new_list
