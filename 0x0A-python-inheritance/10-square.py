#!/usr/bin/python3
"""
class square inherits class rectangle
python3 -c 'print(__import__("my_module").__doc__)'
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class rectangle from 9
    python3 -c 'print(__import__("my_module").my_function.__doc__)'"""
    def __init__(self, size):
        """initiates size
        python3 -c 'print(__import__("my_module").
        MyClass.my_function.__doc__)'"""
        if self.integer_validator("size", size):
            self.__width = size
            self.__height = size
            self.__size = size

    def __str__(self):
        """method that print size
        python3 -c 'print(__import__("my_module").
        MyClass.my_function.__doc__)'"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """returns area with size
        python3 -c 'print(__import__("my_module").
        MyClass.my_function.__doc__)'"""
        return self.__size * self.__size
