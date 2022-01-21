#!/usr/bin/python3

"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


from hashlib import new


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

    def to_json(self, attrs=None):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        """
        if attrs is None:
            return self.__dict__
        new = {}
        for j in attrs:
            try:
                new[j] = self.__dict__[j]
            except Exception:
                pass
        return new
