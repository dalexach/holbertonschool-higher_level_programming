#!/usr/bin/python3
"""
Class Rectangle
"""


class Rectangle:
    """ This is Rectangle Class """
    def __init__(self, width=0, height=0):
        """
        Initialzie Rectangle Class
        Arguments:
        @width: width of the rectangle
        @height: height of the rectangle
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
            if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getter width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Setter of width
        Arguments:
        @value: value to set the width of the rectangle
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Setter of height
        Arguments:
        @value: value to set the height of the rectangle
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
