#!/usr/bin/python3
"""Module"""


class Student:
    """A class named Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of student"""
        if type(attrs) != list:
            return self.__dict__

        new_dict = {}

        for i in attrs:
            if type(i) != str:
                return self.__dict__
            if i in self.__dict__:
                new_dict[i] = self.__dict__[i]

        return new_dict
