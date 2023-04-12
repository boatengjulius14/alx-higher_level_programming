#!/usr/bin/python3
"""Defines the function write_file"""


def write_file(filename="", text=""):
    """read and prints text files
    This function reads text file(UTF8) and prints it to
    stdout
    Args:
        filename(str): name of text file to be written into.
        text(str): text to write.
    Returns:
        int: the number of characters written
    """

    with open(filename, "w", encoding="UTF8") as file:
        return file.write(text)
