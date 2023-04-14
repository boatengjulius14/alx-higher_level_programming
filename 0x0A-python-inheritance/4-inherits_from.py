#!/usr/bin/python3
"""Defines is_kind of class"""


def inherits_from(obj, a_class):
    """checks if an object is an instance of a class that inherited
    from the the specific class
    """
    if type(obj) != a_class:
        return isinstance(obj, a_class)
    return False
