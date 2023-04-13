#!/usr/bin/python3
"""Defines the function from_json_string"""


def from_json_string(my_str):
    """returns an object(Python data structure)
    represented by JSON string
    Args:
        my_str: JSON string
    Return:
        string: python string
    """

    import json
    return json.loads(my_str)
