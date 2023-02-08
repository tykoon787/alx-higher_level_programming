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
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(value))
        elif(value < 0):
            raise ValueError("{} must be > 0".format(value))
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(value))
        elif(value < 0):
            raise ValueError("{} must be >= 0".format(value))
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(value))
        elif(value < 0):
            raise ValueError("{} must be >= 0".format(value))
        self.__x = value
