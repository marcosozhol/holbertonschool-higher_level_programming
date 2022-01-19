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
            print("size must be an integer", end="")
            raise TypeError

        if(size < 0):
            print("size must be >= 0", end="")
            raise ValueError

        self.__size = size
