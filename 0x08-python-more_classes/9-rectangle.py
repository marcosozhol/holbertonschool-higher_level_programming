#!/usr/bin/python3
"""Define a empty class"""


class Rectangle:
    """Create class Rectangle
    Public class attribute number_of_instances:
    Initialized to 0
    Incremented during each new instance instantiation
    Decremented during each instance deletion
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Private instance attribute: width"""

        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

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
        """property def width(self): to retrieve it"""
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

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if(self.__width == 0 or self.__height == 0):
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """method str"""
        rect = ""

        if(self.__width == 0 or self.__height == 0):
            return rect

        for i in range(self.__height):
            for j in range(self.__width):
                rect += str(self.print_symbol)
            if(i != (self.__height - 1)):
                rect += "\n"
        return rect

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
        rect = Rectangle()
        repr(rect)

    def __del__(self):
        """deleted rectangle"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with width == height == size
        Args:
            size: size to set the new rectangle to
        Returns:
            The new Rectangle instance
        """
        return cls(size, size)
