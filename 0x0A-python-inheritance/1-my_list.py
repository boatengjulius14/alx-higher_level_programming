#!/usr/bin/python3
"""Defines the class Mylist"""


class MyList(list):
    """subclass of list

    Attributes
    print_sorted: prints the list in ascending sort
    """
    def print_sorted(self):
        """prints a list in ascending sort"""
        print(sorted(self))
