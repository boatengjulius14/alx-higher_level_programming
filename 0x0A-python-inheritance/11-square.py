#!/usr/bin/python3
"""Defines the class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of class Square,
    subclass of Rectangle
    """

    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns area"""
        return self.__size ** 2

    def __str__(self):
        """returns string representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
