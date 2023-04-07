#!/usr/bin/python3
"""This module adds two integers
This module has only one function 'add_integer' which receives
two int or float values. One parameter is mandatory the other
is non-mandatory with an int value of 98 being passed automatically
"""


def add_integer(a, b=98):
    """adds two arguments(int or float)
    Return: the addition of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
