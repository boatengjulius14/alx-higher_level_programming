#!/usr/bin/python3
"""Defines the function read_file"""


def read_file(filename=""):
    """read and prints text files
    This function reads text file(UTF8) and prints it to
    stdout
    Args:
        filename(str): name of text file to be read
    """

    with open(filename, "r", encoding="UTF8") as file:
        print(file.read())
