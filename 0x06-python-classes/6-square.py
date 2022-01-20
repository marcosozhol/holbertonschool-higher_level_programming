#!/usr/bin/python3
"""class Square"""


class Square:
    """
    Create a Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Private instance attribute: size.
        Instantiation with size (no type/value verification).
        """
        self.__size = size
        self.__position = position

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
        if(self.__size == 0):
            print()
        else:
            for i in range(self.__position[1]):
                print()

        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")

            print("#" * self.__size)

        if(self.__size == 0):
            print("")

    @property
    def position(self):
        """"retrieve it"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if(type(position) != tuple or len(position != 2)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if((type(position[0]) != int) or (type(position[1]) != int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if((type(position[0]) < 0) or (type(position[1]) < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
