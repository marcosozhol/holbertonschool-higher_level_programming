#!/usr/bin/python3
"""class Square"""


class Square:
    """
    Create a Square class
    """
    def __init__(self, size=None):
        """
        Private instance attribute: size.
        Instantiation with size (no type/value verification).
        """
        self.__size = size
