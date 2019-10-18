#!/usr/bin/python3
"""
Module for Base class
"""

class Base:
    """
    Base - class defining another classes
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        Constructor of Base
        """
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
