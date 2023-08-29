#!/usr/bin/python3
"""
A class Square that defines a square by: (based on 1-square.py)
"""


class Square:
    """
    Attributes:
        size (private instance)
    """

    def __init__(self, size=0):
        """
        Initialize a square instance.
        Args:
            size (int): The size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
