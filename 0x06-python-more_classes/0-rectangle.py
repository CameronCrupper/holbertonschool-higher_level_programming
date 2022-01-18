#!/usr/bin/python3


"""
set private insantces for height and width
raise TypeError if not int
raise ValueError if less than 0
"""

class Rectangle:

    """
    class to define a rectangle
    """

    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

@property
def width(self):
    return self.__width

@property
def height(self):
    return self.__height

@width.setter
def width(self, value):
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value

@height.setter
def height(self, value):
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value
