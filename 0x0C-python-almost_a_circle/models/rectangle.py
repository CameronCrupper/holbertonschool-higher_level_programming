#!/usr/bin/python3
"""
Module for Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    define class for rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        creating getter of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        creating setter for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        creating getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        creating setter for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        creating getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        creating setter for x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        creating getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        creating setter for y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returning the area of a rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        return a string for Rectangle
        """
        k = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return k.format(self.id, self.__x, self.__y,
        self.__width, self.__height)

    def display(self):
        """
        print in stdout a rectangle with '#'
        """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def update(self, *args, **kwargs):
        """
        assigning key/value arguments to each attribute
        """
        if args:
            item = ['id', 'width', 'height', 'x', 'y']
            for l, arg in enumerate(args):
                setattr(self, item[l], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        return dictionary representation of Rectangle
        """
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}
