#!/usr/bin/python3
"""Define a empty class"""


class Rectangle:
    """Create class Rectangle"""

    def __init__(self, width=0, height=0):
        """Private instance attribute: width"""

        self.__height = height
        self.__width = width

    @property
    def height(self):
        """property def heigth(self): to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """heigth must be an integer and > 0"""
        if(type(value) != int):
            raise TypeError("height must be an integer")

        elif(value < 0):
            raise ValueError("height must be >= 0")

        else:
            self.__height = value

    @property
    def width(self):
        """property def width(self): to retrieve it """
        return self.__width

    @width.setter
    def width(self, value):
        """width must be an integer and > 0"""
        if(type(value) != int):
            raise TypeError("width must be an integer")

        elif(value < 0):
            raise ValueError("width must be >= 0")

        else:
            self.__width = value
