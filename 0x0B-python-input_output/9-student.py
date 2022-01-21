#!/usr/bin/python3

"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class Student:
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    def __init__(self, first_name, last_name, age):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        """
        return self.__dict__
