#!/usr/bin/python3

"""
This module represents a square. A square is a special rectangle
Where width, height = size
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class Representing a Square

    ...
    Attributes
    ----------
    width : int
        Width of the sqauare
    heiht : int
        Height of the square
    x : int
        x axis
    y : int
        y axis
    id : int
        id

    ....
    Methods
    --------
    All Methods are inherited from super(), in this case, Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return Official Representation of the class
        """
        return ("[{}] ({}) {}/{} - {}".format(
            __class__.__name__,
            self.id,
            self.x,
            self.y,
            self.size))

    def update(self, *args, **kwargs):
        """
        Function that updates the square

            Parameters:
                args (string) : Arguments
                kwargs (dict) : Key=Value paired dict
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            print()
