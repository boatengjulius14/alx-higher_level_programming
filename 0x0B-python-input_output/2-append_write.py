#!/usr/bin/python3
"""Defines the function append_write"""


def append_write(filename="", text=""):
    """appends a string to the end of a file
    This function appends a  string at the end of a text file (UTF8)
    and returns the number of characters added.
    Args:
        filename(str): name of text file to be written into.
        text(str): text to write.
    Returns:
        int: the number of characters added
    """

    with open(filename, "a", encoding="UTF8") as file:
        return file.write(text)
