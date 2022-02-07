#!/usr/bin/python3
""" Module class Base """

import json


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize class Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Static method that returns the JSON string """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Class method that write the JSON string """
        filename = cls.__name__ + ".json"
        list_objs_tmp = []
        if list_objs is not None:
            for i in list_objs:
                list_objs_tmp.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_objs_tmp))

    @staticmethod
    def from_json_string(json_string):
        """ Return the list of the JSON string """
        empty_list = []
        if json_string is None or len(json_string) == 0:
            return empty_list
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Instance to return al attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
