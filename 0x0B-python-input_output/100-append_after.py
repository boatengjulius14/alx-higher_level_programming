#!/usr/bin/python3
"""Defines class Student"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after aech line
    containing a specific string
    """
    new_text = ""
    with open(filename, 'r') as file:
        for line in file:
            new_text += line
            if search_string in line:
                new_text += new_string

    with open(filename, "w") as file:
        file.write(new_text)
