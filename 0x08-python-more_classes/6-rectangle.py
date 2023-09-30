#!/usr/bin/python3
"""
This module defines a class Rectangle.
"""

class Rectangle:
    """Class for printing or computation of dimensions of a rectangle.

    Attributes:
        number_of_instances (int): counter incrementing for every
            instantiation, and decrementing for every instance deletion.

    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Increments `number_of_instances` and calls setters for `__width`
        and `__height`.

        Args:
            width (int): horizontal dimension of rectangle, defaults to 0
            height (int): vertical dimension of rectangle, defaults to 0

        """

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            The value of __width (int): horizontal dimension of rectangle

        """

        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of rectangle

        Attributes:
            __width (int): horizontal dimension of rectangle

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter.

        Returns:
            The value of __height (int): vertical dimension of rectangle

        """

        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of rectangle

        Attributes:
            __height (int): vertical dimension of rectangle

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Computes the area of a rectangle of a given `width` and `height`.

        Returns:
            The area of rectangle: __width * __height

        """

        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of a rectangle of given `width` and `height`

        Returns:
            0 if either attribute is 0, or the perimeter: (__width * 2) +
            (__height * 2).

        """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """Formats a string of '#' and '\n' chars to print the rectangle
        represented by the current instance.

        Returns:
            str (str): string suitable for printing rectangle (final newline
            omitted)

        """

        str = ""
        for row in range(self.__height):
            for _ in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """Allows direct printing of instances.

        Returns:
            The output of _draw_rectangle, which creates a string
        representation of the rectangle suitable for printing.

        """

        return self._draw_rectangle()

    def __repr__(self):
        """Allows use of eval().

        Returns:
            A string of the code needed to create the instance.

        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Decrements `number_of_instances`, then prints message upon
        deletion of instance.

        """

        type(self).number_of_instances -= 1
        print('Bye rectangle...')