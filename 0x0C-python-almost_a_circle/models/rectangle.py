#!/usr/bin/python3
"""
Rectangle Class

Classes:
    Rectangle(Base)

"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle that Inherits from base

    ...

    Attributes
    ----------
    width : int
        Width of the Rectangle
    height: int
        Height of the Rectangle
    x : int
        Variable x
    y : int
        Variable y

    Methods
    -------
    area:
        Returns the area of a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
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
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Function that returns the area of a  rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Displays the rectangle instance
        """
        height_counter = 0
        while height_counter < self.__height:
            print("#" * self.__width)
            height_counter += 1

    def __str__(self):
        """
        Returns formatted information to display
        """
        return ("[{}] ({}) <{}>/<{}> - <{}>/<{}>".format(__class__.__name__, self.id, 
                                                        self.__x, self.__y, self.__width, self.__height)) 

    def update(self, *args):
        """
        Assigns an argument to each attribue
        """
        args = list(args)
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.__width = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        elif len(args) == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
