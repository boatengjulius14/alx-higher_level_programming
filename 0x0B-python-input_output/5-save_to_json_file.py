#!/usr/bin/python3
"""Defines the function save_to_json_file"""


def save_to_json_file(my_obj, filename):
    """writes an object to a text file,
    using JSON representation
    Args:
        my_obj: object data to serialize
        filename: file for storing serialize data
    """

    import json
    with open(filename, "w") as file:
        json.dump(my_obj, file)
