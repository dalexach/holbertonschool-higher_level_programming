#!/usr/bin/python3
"""
Module class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle - class that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for rectangle
        Arguments:
        @width: width of the rectangle
        @height: height of the rectangle
        @x: 
        @y:
        @id: 
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        self.validator("y", value)
        self.__y = value

    # magic methods
    def __str__(self):
        """
        formats string representation of the Rectangle
        """
        return ("[{}] ({}) {}/{} - {}/{}".format(
                self.__class__.__name__, self.id,
                self.x, self.y, self.__width, self.__height))

    # public methods
    def validator(self, name, value):
        """ 
        validator - method that checks for legal values
        Arguments:
        @name: name of the attribute to check
        @value: value of the attribute to check
        Returns:
        A raise Type or Value error if is not an integer or
        if is not a positive number, respectly
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and (name is "height" or name is "width"):
            raise ValueError("{} must be > 0".format(name))
        if value < 0 and (name is "x" or name is "y"):
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """
        area - method that returns the area value
        Returns:
        The area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        display - method that prints in stdout the Rectangle instance
        with the character #
        """
        for posy in range(self.__y):
            print()
        for r in range(self.__height):
            for posx in range(self.__x):
                print(" ", end="")
            for c in range(self.__width):
                print('#', end="")
            print()
