#!/usr/bin/python3
"""
Module class Square that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square - class for a square, this class inherit form Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for square
        Arguments:
        @size: size of the rectangle
        @x: position in x
        @y: position in y
        @id: amount of instances created
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for width of square """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for width of square """
        super().validator("width", value)
        Rectangle.__width = value
        Rectangle.__height = value


    # magic methods
    def __str__(self):
        """
        formats string representation of the Square
        """
        return ("[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__, self.id,
                self.x, self.y, self.width))
