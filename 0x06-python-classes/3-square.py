#!/usr/bin/python3
"""Defines a square"""


class Square:
    """constructor with private attribute __size"""
    def __init__(self, size=0):
        """Initialize private attribute with size
        Args:
            size (int): size of a square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size
