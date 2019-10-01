#!/usr/bin/python3
class Square:
    """
    Class Square for all the square needs.
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize Square class.
        Arguments:
        @size: Size of the square.
        @position: Starting point of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Set position as a property
        Return:
        The coordination of position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Setter of position
        Arguments:
        @value: coordination of position
        """
        if len(value) != 2 or type(value) != tuple or \
           type(value[0]) != int or value[0] < 0 or \
           type(value[1]) != int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Calculate the area of a square.
        Return:
        Power of square size
        """
        return (self.size ** 2)

    def my_print(self):
        """ Print a square with character # """
        if self.size == 0:
            print()
        else:
            for y in range(self.position[1]):
                print()
            for r in range(self.size):
                for x in range(self.position[0]):
                    print(" ", end="")
                for c in range(self.size):
                    print("#", end="")
                print()

    def __check_size__(self, size):
        """
        Size error checking
        Arguments:
        @size: value of size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
