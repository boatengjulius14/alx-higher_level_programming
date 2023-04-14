#!/usr/bin/python3
"""Defines is_kind of class"""


def is_kind_of_class(obj, a_class):
    """Checks if and object is an instance of a class
    Returns True or False to verify"""
    if isinstance(obj, a_class):
        return True
    return False
