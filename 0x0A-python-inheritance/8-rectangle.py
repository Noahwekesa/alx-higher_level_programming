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
        self._width = width
        self._height = height
        self.integer_validator(self._width)
        self.integer_validator(self._height)
        