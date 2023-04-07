#!/usr/bin/python3
"""This module defines the function matrix_divided"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix
        matrix_divided returns a new list by dividing all elements
        in the list of list, matrix
    Args:
        matrix (list): first argument
        div (float or int): second argument
    Return:
        list: lists of lists with the results of dividing all
        elements in matrix by div
    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeErrors: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    for i in matrix:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i/div, 2) for i in j] for j in matrix]
