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
        self.__check_size__(size)
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
        self.__check_size__(value)
        self.__size = value

    def area(self):
        """ Calculate the area of a square.
        Return:
        Power of square size
        """
        return ((self.__size) ** 2)

    def my_print(self):
        """ Print a square with character # """
        if self.size == 0:
            print()
        else:
            for r in range(self.size):
                for c in range(self.size):
                    print("#", end="")
                print()

    def __check_size__(self, size):
        """
        Size error checking
        Arguments:
        @size: value of size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
