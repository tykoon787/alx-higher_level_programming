#!/usr/bin/python3
"""
A square inheriting from the rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square inheriting
    from Rectangle
    """
    def __init__(self, size):
        super().integer_validator(size)
        self.__size = size

    def area(self):
        """
        Returns the area of a square
        """
        return (self.__size * self.__size)
