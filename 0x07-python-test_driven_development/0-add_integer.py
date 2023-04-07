#!/usr/bin/python3
""" Add Integer Module

This module has only one function 'add_integer' which receives
two int or float values
"""


def add_integer(a, b=98):
    """adds two arguments(int or float)
    Return: the addition of a and b
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
