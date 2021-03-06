#!/usr/bin/python3


"""
set a class for rectangle
"""


class Rectangle:

    """
    set private insantces for height and width
    raise TypeError if not int
    raise ValueError if less than 0
    """

    def __init__(self, width=0, height=0):
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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        string = self.__width * "#"
        return (string + "\n") * (self.__height - 1) + string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
