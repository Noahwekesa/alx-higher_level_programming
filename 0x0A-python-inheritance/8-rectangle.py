#!/usr/bin/python3
"""
a class function that inherits from BaseGeometry(7-base_geometry.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    """
    a class rectangle
    """

    def __init__(self, width, height):
        """
        function instantiation with w and h"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height