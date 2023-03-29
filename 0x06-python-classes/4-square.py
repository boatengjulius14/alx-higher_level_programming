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

    @property
    def size(self):
        """grants access to the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size
