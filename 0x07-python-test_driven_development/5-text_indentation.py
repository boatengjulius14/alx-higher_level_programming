#!/usr/bin/python3
"""This module defines the function text_indentation"""


def text_indentation(text):
    """prints a text
        Prints a text with 2 new lines after each
        of these characters: . ? and :
    Args:
        text (str): length of the square
    Raises:
        TypeError: text must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = list(text)
    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            print("{}\n".format(text[i]))
            if (i != len(text) - 1 and text[i+1] == " "):
                text[i+1] = ""
            continue
        print(text[i], end="")
