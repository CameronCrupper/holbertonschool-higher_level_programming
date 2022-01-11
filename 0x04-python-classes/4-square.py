#!/usr/bin/python3
"""This defines a square class"""


class Square:
    """This class is instantiated size with no value verifi or type"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        sq_area = self.__size * self.__size
        return(sq_area)

    def my_print(self):
        if self.__size == 0:
            print(" ")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
