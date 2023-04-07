#!/usr/bin/python3
"""This module adds two integers"""


def matrix_divided(matrix, div):
    """Returns the addition of integers a + b
    Args:
        a (int or float): first argument
        b (int or float): second argument
    Return:
        int: the addition of a and b
    Raises:
        TypeError: a must be an integer or b must be an integer
    """
    for i in matrix:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i/div, 2) for i in j] for j in matrix]
        
        

matrix = [
    [1, 2],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
