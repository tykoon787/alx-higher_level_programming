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
        self.__size = size
        self.__x = x
        self.__y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        print("Value Received: {}".format(value))
        if type(value) != int:
            raise TypeError("Size must be an integer")
        if value <= 0:
            raise ValueError("Size must be > 0")
        self.__size = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        print("Value Received: {}".format(value))
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        print("Value Received: {}".format(value))
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """
        Return Official Representation of the class
        """
        return ("[{}] ({}) {}/{} - {}".format(
            __class__.__name__,
            self.id,
            self.__x,
            self.__y,
            self.__size))
