#!/usr/bin/python3
"""class Square"""


class Square:
    """
    Create a Square class
    """
    def __init__(self, size=0):
        """
        Private instance attribute: size.
        Instantiation with size (no type/value verification).
        """
        if(type(size) != int):
            raise TypeError("size must be an integer", end="")

        if(size < 0):
            raise ValueError("size must be >= 0", end="")

        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size * self.__size
