#!/usr/bin/python3
""" Module """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Create class Square """

    def __init__(self, size):
        """ Atributes """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        self.area()
