#!/usr/bin/python3


"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class BaseGeometry:
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    def area(self):
        """
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    def __init__(self, width, height):
        """
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return self.__width * self.__height

    def __str__(self):
        """
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    def __init__(self, size):
        """
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return self.__size ** 2

    def __str__(self):
        """
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
