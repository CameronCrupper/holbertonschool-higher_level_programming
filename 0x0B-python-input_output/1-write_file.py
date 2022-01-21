#!/usr/bin/python3

"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def write_file(filename="", text=""):
    """
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """
    with open(filename, mode="w", encoding="utf-8") as f:

        return f.write(text)
