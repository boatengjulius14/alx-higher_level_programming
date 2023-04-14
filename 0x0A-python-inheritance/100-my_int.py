#!/usr/bin/python3
"""Defines the class MyInt"""


class MyInt(int):
    """MyInt class definition"""
    def __eq__(self, value):
        """equal to magic method"""
        return False

    def __ne__(self, other):
        """not equal magic method"""
        return True
