#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Rectangle Class
    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
     """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Constructor
        Magic method for instantiation
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            _str += str(self.print_symbol) * self.__width
            if i != (self.__height - 1):
                _str += "\n"
        return _str

    def __repr__(self):
        """Return an official string representation
        of an instance"""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """prints 'Bye rectangle...' when an instance of
        Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the instance with the biggest area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
