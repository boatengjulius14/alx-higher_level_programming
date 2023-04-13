#!/usr/bin/python3
"""Defines the function to_json_string"""


def to_json_string(my_obj):
    """returns the JSON representation
    of an object(string)
    Args:
        my_obj: the object
    Return:
        string: JSON representation of an object(string)
    """

    import json
    return json.dumps(my_obj)
