#!/usr/bin/python3
"""
    function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix

    Args:
        matrix: matrix to divide
        div: value what divide the matrix

    Return:
        new_matrix (list): list of list with all elements of matrix divide
        by div number.
    """
    msgError = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not len(matrix):
        raise TypeError(msgError)
    for row in matrix:
        if not isinstance(row, list) or not len(row):
            raise TypeError(msgError)
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(msgError)
    lenRow = len(matrix[0])
    for a in range(len(matrix) - 1):
        if lenRow != len(matrix[a + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(i/div, 2) for i in row] for row in matrix]
    return new_matrix
