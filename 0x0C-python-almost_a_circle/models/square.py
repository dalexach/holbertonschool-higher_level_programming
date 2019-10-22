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
        Rectangle.width = value
        Rectangle.height = value

    # magic methods

    def __str__(self):
        """
        formats string representation of the Square
        """
        return ("[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__, self.id,
                self.x, self.y, self.width))

    # public methods

    def update(self, *args, **kwargs):
        """
        update - assign the arguments to each attribute
        @args: list of arguments
        @kargs: dictionary of arguments, key represents
        an attribute to the instance
        """
        if isinstance(args, tuple):
            if len(args) > 1:
                temp = list(args)
                temp.insert(1, args[1])
                temp = tuple(temp)
                super().update(*temp)
            else:
                super().update(*args)
        if not args:
            super().update(**kwargs)
            for key, value in kwargs.items():
                if key == 'size':
                    self.width = value
                    self.height = value

    def to_dictionary(self):
        """
        to_dictionary - returns a dictionary representation of a Square
        """
        temp = {}
        for key in self.__dict__.keys():
            if key in ["_Rectangle__height", "_Rectangle__width"]:
                temp["size"] = self.__dict__[key]
                continue
            temp[key.split('-')[-1]] = self.__dict__[key]
        return temp
