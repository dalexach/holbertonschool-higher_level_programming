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
