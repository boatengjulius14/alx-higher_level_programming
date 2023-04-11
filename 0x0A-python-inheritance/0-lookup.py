#!/usr/bin/python3
"""Defines function lookup"""


def lookup(obj):
    """returns the list of available
    attributes and methods of an object
    Args:
    obj: object
    Return:
    list: list of available attributes and methods
    of obj
    """
    return dir(obj)
