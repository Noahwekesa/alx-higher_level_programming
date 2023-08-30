#!/usr/bin/python3
"""a class Square program that defines a square by: (based on 4-square.py)
"""


class Square:
    """Private instance attribute: 
        size
    """

    def __init__(self, size=0):
        """Initialization of, attribute size """
        self.__size = size

    def area(self):
        """Calculation of the area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Setter,"""
        return self.__size

    @size.setter
    def size(self, value):
        """initialization of attribute(size)"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
        if self.size <= 0:
            print()
