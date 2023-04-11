#!/usr/bin/python3
"""Defines the function is_same_class"""


def is_same_class(obj, a_class):
    """Checks the class of an object
    Returns True if an object is an instance
    of class, False if not

    Args:
        obj: object of a class
        a_class: the class
    Return:
        bool: returns True if the object is exactly an instance
        of the specified class; False if otherwise
    """

    if type(obj) == a_class:
        return True
    return False
