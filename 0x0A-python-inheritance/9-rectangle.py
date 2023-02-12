#!/usr/bin/python3
"""
A rectangle class that inherits from the base geometry
class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A rectangle
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return ("[{}] {}/{}".format(
            self.__class__.__name__,
            self.width, self.height))
