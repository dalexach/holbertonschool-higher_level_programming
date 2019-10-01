#!/usr/bin/python3
class Square:
    """
    Create a class Square, includes setters and getters for size
    """

    def __init__(self, size=0):
        """ Initialize Square class.
        Arguments:
        @size: Size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Set size as a property.
        Return:
        Value of size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Setter of size.
        Arguments:
        @value: value of size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculate the area of a square.
        Return:
        Power of square size
        """
        return ((self.__size) ** 2)
