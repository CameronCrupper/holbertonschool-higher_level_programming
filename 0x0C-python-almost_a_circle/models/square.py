#!/usr/bin/python3

"""
module of Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    creating class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializing class Square
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        creating getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        creating setter for size that returns type and value Errors
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def to_dictionary(self):
        """
        returns dictionary representation of Rectangle
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        """
        return string for a square
        """
        sq = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return sq.format(self.id, self.x, self.y, self.width)

