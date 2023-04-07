#!/usr/bin/python3
"""This module defines the function say_my_name"""


def say_my_name(first_name, last_name=""):
    """Adds and print arguments as part of a string
        prints 'My name is <first_name> <last_name>
    Args:
        first_name (str): first argument
        last_name (str): second argument
    Raises:
        TypeError: first_name must be a string or last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
