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

    def area(self):
        """area method
        Return:
            the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """perimeter method
        Return:
            the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """Return a printable string represention
        of an instance
        """
        _str = ""
        if self.__width == 0 or self.__height == 0:
            return _str

        for i in range(self.__height):
            _str += "#" * self.__width
            if i != (self.__height - 1):
                _str += "\n"
        return _str
