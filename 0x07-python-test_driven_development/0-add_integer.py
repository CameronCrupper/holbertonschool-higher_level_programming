#!/usr/bin/python3


"""
A function that adds two integers
both integers must be not float
python3 -c 'print(__import__("my_module").__doc__)'
"""


def add_integer(a, b=98):

    """
if a or b are float change and return int
"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
