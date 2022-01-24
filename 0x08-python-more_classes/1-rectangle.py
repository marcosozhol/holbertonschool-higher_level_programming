#!/usr/bin/python
"""Define a empty class"""


class Rectangle:
    """Create class Rectangle"""

    def __init__(self, width=0, heigth=0):
        """Private instance attribute: width"""

    @property
    def width(self):
        """property def width(self): to retrieve it"""
        self.__width = width

    @width.setter
    def width(self, value):
        """width must be an integer and > 0"""
        if(type(value) != int):
            raise TypeError("width must be an integer")

        if(value < 0):
            raise ValueError("width must be >= 0")

    @property
    def heigth(self):
        """property def heigth(self): to retrieve it"""
        self.__heigth = heigth

    @heigth.setter
    def heigth(self, value):
        """heigth must be an integer and > 0"""
        if(type(value) != int):
            raise TypeError("height must be an integer")

        if(value < 0):
            raise ValueError("height must be >= 0")
