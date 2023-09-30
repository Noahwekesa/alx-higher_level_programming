#!/usr/bin/python3
"""

a class Rectangle that defines a rectangle by: (based on 3-rectangle.py

"""


class Rectangle:
    """
    A Rectangle class
    """

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):

        return self.__width

    @width.setter
    def width(self, value):

        self.__check_valid_width(value)
        self.__width = value

    @property
    def height(self):

        return self.__height

    @height.setter
    def height(self, value):

        self.__check_valid_height(value)
        self.__height = value

    def __check_valid_width(self, width):

        if self.__check_int_value(width) is False:
            raise TypeError('width must be an integer')

        if self.__check_positive_value(width) is False:
            raise ValueError('width must be >= 0')

    def __check_valid_height(self, height):

        if self.__check_int_value(height) is False:
            raise TypeError('height must be an integer')

        if self.__check_positive_value(height) is False:
            raise ValueError('height must be >= 0')

    def __check_int_value(self, value):

        if type(value) is int:
            return True

        return False

    def __check_positive_value(self, value):

        if value >= 0:
            return True

        return False

    def area(self):

        return self.__width * self.__height

    def perimeter(self):

        if self.__width == 0 or self.__height == 0:
            return 0

        return self.__width * 2 + self.__height * 2

    def __draw_rectangle(self):

        rect_str = ''
        new_width = self.__width
        new_height = self.__height

        if new_width == 0 or new_height == 0:
            return rect_str

        for i in range(new_height):
            for j in range(new_width):
                rect_str += '#'

            if i != new_height - 1:
                rect_str += '\n'

        return rect_str

    def __str__(self):

        return self.__draw_rectangle()

    def __repr__(self):
        new_width = str(eval('self.width'))
        new_height = str(eval('self.height'))

        return 'Rectangle(' + new_width + ', ' + new_height + ')'
