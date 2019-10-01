#!/usr/bin/python3
class Square:
    """
    Class Square that defines a square with
    setters and getters fot the size
    """
    def __init__(self, size=0):
        """
        Initialize the class with a size
        Arguments:
        @size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Size getter
        Return:
        The private size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the value of the size of the square
        Arguments:
        @value: size of the square
        """
        self.__check_size__(value)
        self.__size = value

    """
    functions to compare two objects
    eq: for equal
    ne: for not equal
    lt: for the second is greater
    gt: for the first is greater
    le: if the second is greater or equal
    ge: if the first is grater or equal
    """

    def __eq__(self, other):
        return (self.size == other.size)

    def __ne__(self, other):
        return (self.size != other.size)

    def __lt__(self, other):
        return (self.size < other.size)

    def __gt__(self, other):
        return (self.size > other.size)

    def __le__(self, other):
        return (self.size <= other.size)

    def __ge__(self, other):
        return (self.size >= other.size)

    def area(self):
        """
        Calculates the area of the square
        Return:
        The area of square
        """
        return (self.__size ** 2)

    def __check_size__(self, size):
        """
        Checks the type of size on the square
        """
        if type(size) != int and type(size) != float:
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
