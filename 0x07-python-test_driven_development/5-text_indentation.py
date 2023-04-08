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

    _str = []
    text = list(text)
    for i in range(len(text)):
        if text[i] in ['.', '?', ':']:
            _str[len(_str):] += [text[i], '\n', '\n']
            if (i != len(text) - 1 and text[i+1] == " "):
                while text[i+1] == " ":
                    text[i+1] = ""
                    i += 1
            continue
        _str += text[i]

    _str1 = ""
    for i in _str:
        _str1 += i

    print(_str1.strip(" "), end="")
