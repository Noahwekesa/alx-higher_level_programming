#!/usr/bin/python3
"""
a class bassed on 6-base_geometry.py
"""
class BaseGeometry:
    """
    a class called basegeometry
    """
    def area(self):
        """function that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
