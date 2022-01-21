#!/usr/bin/python3


"""
Class rectangle and subclass base geometry
python3 -c 'print(__import__("my_module").__doc__)'
"""


class BaseGeometry:

    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """

    def area(self):
        raise Exception("area() is not implemented")

    """
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    def integer_validator(self, name, value):
        self.value = value
        self.name = name

        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """instatiate rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
