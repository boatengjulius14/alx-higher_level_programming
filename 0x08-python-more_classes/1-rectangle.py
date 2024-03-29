#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Rectangle Class
    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
     """

    def __init__(self, width=0, height=0):
        """Constructor
        Magic method for instantiation
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for width
        Return:
           The private instance attribute, width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method
        Gives access to change the value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for height
        Return:
           The private instance attribute, height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method
        Gives access to change the value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
