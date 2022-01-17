#!/usr/bin/python3


"""
text must be a string
no spaces at the beginning or end of printed line
no importing of modules
"""


def text_indentation(text):

    """
    print text w/ 2 new lines after each character . ? :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    j = [lines.strip(' ') for lines in text.split('\n')]
    i = "\n".join(j)
    print(i, end="")
