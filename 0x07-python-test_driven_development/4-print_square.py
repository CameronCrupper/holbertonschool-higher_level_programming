#!/usr/bin/python3


"""
size is the length of the square
size must be an integer
size must be more than 0
"""


def print_square(size):

    """
    function that prints a square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if size == 0:
        print("", end="")
    else:
        print("\n".join(["#" * size for rows in range(size)]))
