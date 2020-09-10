#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_mat = matrix[:]
    for i in range(len(square_mat)):
        square_mat[i] = list(map(square, square_mat[i]))
    return square_mat


def square(value):
    return value ** 2
