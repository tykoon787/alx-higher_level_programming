#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
A rectangle class that inherits from the base geometry
class
"""


class Rectangle(BaseGeometry):
    """
    A rectangle
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.width = width
        self.height = height
