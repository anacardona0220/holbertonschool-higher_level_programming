#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ Check if matrix is a list of lists of integers or floats"""
    
    
    if not all(isinstance(row, list) for row in matrix) or not all(
            isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    """ Check if each row of the matrix has the same size """
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    """Validate div value"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    """Validate div input"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
