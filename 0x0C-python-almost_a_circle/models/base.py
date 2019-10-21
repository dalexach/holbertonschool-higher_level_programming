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
