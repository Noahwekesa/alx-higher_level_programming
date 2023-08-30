#!/usr/bin/python3
"""a class program that square that defines a square by:(based on 3-square)"""


class Square:
    """create a class called class"""

    def __init__(self, size=0):
        '''Initializes the size attribute'''
        self.size = size

    @property
    def size(self):
        """setter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size attribute initialization"""
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """area of the square"""
        return self.__size * self.__size
