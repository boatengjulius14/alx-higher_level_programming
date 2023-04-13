#!/usr/bin/python3
"""Defines the function load_from_json_file"""


def load_from_json_file(filename):
    """creates an object from a "JSON file"
    Args:
        filename(file obj): JSON file
    Return:
        object
    """

    import json
    with open(filename) as file:
        return json.load(file)
