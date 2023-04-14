#!/usr/bin/python3
"""Defines add_attribute"""


def add_attribute(obj, attr, value):
    """adds a new attribute to an object if it's possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr] = value
