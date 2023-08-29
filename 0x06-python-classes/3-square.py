#!/usr/bin/python3

class Square:
    """
    A class representing a square based on 2-square.py
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance.
        private instance
        Args:
            size (int): The size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns: The area of the square.
        """
        return self.__size ** 2
