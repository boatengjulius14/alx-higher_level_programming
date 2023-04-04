#!/usr/bin/python3
"""This module adds two integers"""


def add_integer(a, b=98):
    """Returns the addition of integers a + b
    Args:
        a (int or float): first argument
        b (int or float): second argument
    Return:
        int: the addition of a and b
    Raises:
        TypeError: a must be an integer or b must be an integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
