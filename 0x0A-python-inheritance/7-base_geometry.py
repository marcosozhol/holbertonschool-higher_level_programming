#!/usr/bin/python3
""" Geometry module """


class BaseGeometry:
    """ Create class """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ function that validation """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
