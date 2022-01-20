#!/usr/bin/python3

class BaseGeometry:

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.value = value
        self.name = name

        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
