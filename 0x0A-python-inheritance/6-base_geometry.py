#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """An empty class BaseGeometry"""

    def area(self):
        """raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
