#!/usr/bin/python3

"""
function that divides all elements of a matrix
must be int or float
each matrix row must be equivalent
"""

def matrix_divided(matrix, div):

    """
    divide all elements of a matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size = len(matrix[0])
    for lists in matrix:
        if len(lists) != size:
            raise TypeError("Each row of the matrix must have the same size")
        nl = []
        for i in lists:
            nl.append(round(i / div, 2))
        new_matrix.append(nl)
    return new_matrix
