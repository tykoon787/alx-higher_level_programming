#!/usr/bin/python3
"""
Base Class

    Methods:
        area(self): Calculates Area
"""


class BaseGeometry():
    """
    Class Base Geometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
