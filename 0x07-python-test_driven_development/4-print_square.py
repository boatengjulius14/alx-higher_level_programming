#!/usr/bin/python3
"""This module defines the function print_square"""


def print_square(size):
    """prints a square with the character '#'
        Prints a square with length 'size', make up
        of '#'
    Args:
        size (int): length of the square
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print(''.join(['#' for _ in range(size)]))
