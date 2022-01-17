#!/usr/bin/python3


"""
stuf
an
things
"""


def text_indentation(text):

    """
    stuff
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    j = [lines.strip(' ') for lines in text.split('\n')]
    i = "\n".join(j)
    print(i, end="")
