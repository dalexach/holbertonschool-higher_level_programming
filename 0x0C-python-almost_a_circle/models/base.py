#!/usr/bin/python3
"""
Module for Base class
"""


import json


class Base:
    """
    Base - class defining another classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor of Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list
        Arguments:
        @list_dictionaries: is a list of dictionaries
        Returns:
        The JSON string representation of list_dictionaries, otherwise "[]"
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        Arguments:
        @cls: class
        @list_objs: is a list of instances who inherits of Base
        Returns:
        Only writes the JSON string in the file
        """
        with open('{}.json'.format(cls.__name__), 'w') as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                jlist = []
                for i in list_objs:
                    i = i.to_dictionary()
                    jlist.append(i)
                f.write(cls.to_json_string(jlist))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a dictionary to a JSON string representation
        Arguments:
        @json_string: is a string representing a list of dictionaries
        Returns:
        list of JSON string representation, otherwise a empty list
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        Arguments:
        @cls: current class
        @dictionary: can be thought of as a double pointer to a dictionary
        Returns:
        An instance with all attributes already set
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            new = Rectangle(1, 1, 0, 0)
        elif cls.__name__ == "Square":
            new = Square(1, 0, 0)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances
        Arguments:
        @cls: current class
        Returns:
        An empty list if the file does not exist, otherwise,
        return a list of instances, the type of these instances depends on cls
        """
        try:
            with open('{}.json'.format(cls.__name__), 'r') as f:
                jtext = f.read()
                new_object = cls.from_json_string(jtext)
                new_list = []
                for i in new_object:
                    new_list.append(cls.create(**i))
                return new_list
        except FileNotFoundError as e:
            return []
        return new_list
