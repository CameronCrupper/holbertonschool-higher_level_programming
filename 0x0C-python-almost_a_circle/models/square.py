#!/usr/bin/python3

"""

"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """

    """
    def __init__(self, size, x=0, y=0, id=None):
        """

        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def to_dictionary(self):
        """

        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
