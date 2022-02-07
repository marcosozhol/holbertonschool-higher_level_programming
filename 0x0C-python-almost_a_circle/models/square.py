#!/usr/bin/python3
""" Module Class Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Initialize class Square """
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        """ Call the super class with id """
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """ Getter size of width """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ Instance for overriding the str method """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """ Istance for assigns an argument """
        if args:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    self.size = value
                elif index == 2:
                    self.x = value
                elif index == 3:
                    self.y == value
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Instance returns dictionary representation of a Square """
        sq_dict = {}
        sq_dict["id"] = self.id
        sq_dict["size"] = self.size
        sq_dict["x"] = self.x
        sq_dict["y"] = self.y
        return sq_dict
