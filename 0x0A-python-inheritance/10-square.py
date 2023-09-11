#!/usr/bin/python3
"""
class square that inherits from Rectangle(9-rectangle.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class named Square
    """
    def __init__(self, size):
        """instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
