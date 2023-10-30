#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """This Method divide all the elements of matrix by value div

    Args:
        matrix : list of lists and all elements are floats or ints
        div :  number (integer or float) to divide matrix by
    Returns:
        div_matrix : matrix divided by div
    Raises:
        TypeError : If div is not an int or float.
        ZeroDivisionError: If div is zero.
        TypeError : If matrix is not a list of lists and all elements are ints or floats.
        TypeError : If The lists do not have the same length.

    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    div_matrix = []
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(element / div, 2))
        div_matrix.append(new_row)

    return div_matrix
