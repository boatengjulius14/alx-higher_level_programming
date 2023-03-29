#!/usr/bin/python3
"""Defines a square"""


class Square:
    """constructor with private attribute __size"""
    def __init__(self, size):
        """Initialize private attribute with size
        Args:
            size (int): size of a square.
        """
        self.__size = size
