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

    @property
    def size(self):
        """retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """must be an integer and > 0"""
        if(type(value) != int):
            raise TypeError("size must be an integer")

        if(value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if(self.__size > 0):

            for i in range(self.__size):
                print("#" * self.__size)

        else:
            print("")
