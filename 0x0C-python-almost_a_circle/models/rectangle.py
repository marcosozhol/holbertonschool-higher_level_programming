#!/usr/bin/python3
""" Module Class rectangle """

from models.base import Base


class Rectangle(Base):
    """ Initialize class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        """ Call the super class with id """
        Base.__init__(self, id)

    @property
    def width(self):
        """ Getter width """
        return self.__width

    @property
    def height(self):
        """ Getter height """
        return self.__height

    @property
    def x(self):
        """ Getter x """
        return self.__x

    @property
    def y(self):
        """ Getter y """
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Instance for area """
        return self.__width * self.__height

    def display(self):
        """ Instance for print a rectangle """
        print(("\n" * self.__y) +
                "\n".join(((" " * self.__x) +
                    ("#" * self.__width))for i in range(self.__height)))


    def __str__(self):
        """ Instance for overriding the str method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Instance for assigns an argument """
        if args:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    self.width = value
                elif index == 2:
                    self.height = value
                elif index == 3:
                    self.x = value
                elif index == 4:
                    self.y = value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
