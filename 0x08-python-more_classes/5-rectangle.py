#!/usr/bin/python3
"""
a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
"""


class Rectangle:
    """Defines a Rectangle class.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Methods:
        area(): Returns the area of the rectangle.
        perimeter(): Returns the perimeter of the rectangle.
        __str__(): Returns a string representation of the rectangle.
        __repr__(): Returns a string representation of the rectangle.
        __del__(): Prints a message when an instance of the class is deleted.

    """
    def __init__(self, width=0, height=0):
        """Initializes an instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width of the rectangle.

        Returns:
            The width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter method for the height of the rectangle.

        Returns:
            The height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            The area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle.

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """Draws a rectangle using the '#' character.

        Returns:
            A string representation of the rectangle.

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            A string representation of the rectangle.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """Returns a string representation of the rectangle.

        Returns:
            A string representation of the rectangle.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when an instance of the class is deleted.

        """
        print('Bye rectangle...')
