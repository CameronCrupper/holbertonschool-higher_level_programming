#!/usr/bin/python3
"""This defines a square class"""


class Square:
    """This class is instantiated size with no value verifi or type"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        sq_area = self.__size * self.__size
        return(sq_area)