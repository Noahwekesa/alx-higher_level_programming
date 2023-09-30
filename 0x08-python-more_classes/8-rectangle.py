#!/usr/bin/python3
"""
A module that does nothing
"""


class Rectangle:
    """

    An empty Rectangle class

    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """

        Checks the parameters and initializes some values

        Args:
            width (:obj:`int`, optional): The width of the Rectangle.
            height (:obj:`int`, optional): The height of the Rectangle.

        """

        self.width = width
        self.height = height
        class Rectangle:
            """
            A class representing a rectangle.

            Attributes:
                number_of_instances (int): The number of Rectangle instances.
                print_symbol (any): The symbol used for string representation.

            """

            number_of_instances = 0
            print_symbol = '#'

            def __init__(self, width=0, height=0):
                """
                Initializes a Rectangle instance.

                Args:
                    width (int): The width of the Rectangle.
                    height (int): The height of the Rectangle.

                """

                self.width = width
                self.height = height
                Rectangle.number_of_instances += 1

            def __del__(self):
                """
                Deletes a Rectangle instance.

                """

                Rectangle.number_of_instances -= 1
                print('Bye rectangle...')

            @property
            def width(self):
                """
                Gets the width of the Rectangle.

                Returns:
                    int: The width of the Rectangle.

                """

                return self.__width

            @width.setter
            def width(self, value):
                """
                Sets the width of the Rectangle.

                Args:
                    value (int): The width of the Rectangle.

                Raises:
                    TypeError: If `value` type is not `int`.
                    ValueError: If `value` is less than `0`.

                """

                self.__check_valid_width(value)
                self.__width = value

            @property
            def height(self):
                """
                Gets the height of the Rectangle.

                Returns:
                    int: The height of the Rectangle.

                """

                return self.__height

            @height.setter
            def height(self, value):
                """
                Sets the height of the Rectangle.

                Args:
                    value (int): The height of the Rectangle.

                Raises:
                    TypeError: If `value` type is not `int`.
                    ValueError: If `value` is less than `0`.

                """

                self.__check_valid_height(value)
                self.__height = value

            def __check_valid_width(self, width):
                """
                Checks if the width is a valid integer.

                Args:
                    width (int): The width of the Rectangle.

                Raises:
                    TypeError: If `width` type is not `int`.
                    ValueError: If `width` is less than `0`.

                """

                if not isinstance(width, int):
                    raise TypeError('width must be an integer')

                if width < 0:
                    raise ValueError('width must be >= 0')

            def __check_valid_height(self, height):
                """
                Checks if the height is a valid integer.

                Args:
                    height (int): The height of the Rectangle.

                Raises:
                    TypeError: If `height` type is not `int`.
                    ValueError: If `height` is less than `0`.

                """

                if not isinstance(height, int):
                    raise TypeError('height must be an integer')

                if height < 0:
                    raise ValueError('height must be >= 0')

            def area(self):
                """
                Computes the area of a Rectangle.

                Returns:
                    int: The area of a Rectangle.

                """

                return self.__width * self.__height

            def perimeter(self):
                """
                Computes the perimeter of a Rectangle.

                Returns:
                    int: The perimeter of a Rectangle.

                """

                if self.__width == 0 or self.__height == 0:
                    return 0

                return self.__width * 2 + self.__height * 2

            def __draw_rectangle(self):
                """
                Draws the Rectangle with their size.

                Returns:
                    str: `Empty` If width or height is `0`,
                    otherwise returns a string with the Rectangle.

                """

                rect_str = ''
                w = self.__width
                h = self.__height

                if w == 0 or h == 0:
                    return rect_str

                for i in range(h):
                    for j in range(w):
                        rect_str += str(Rectangle.print_symbol)

                    if i != h - 1:
                        rect_str += '\n'

                return rect_str

            @staticmethod
            def bigger_or_equal(rect_1, rect_2):
                """
                Compares the biggest or equal area value between two Rectangles.

                Args:
                    rect_1 (Rectangle): The first Rectangle to compare.
                    rect_2 (Rectangle): The second Rectangle to compare.

                Returns:
                    Rectangle: The biggest Rectangle, or `rect_1` if the
                    two Rectangles have the same area value.

                Raises:
                    TypeError: If `rect_1` or `rect_2` aren't an instance
                    of the Rectangle class.

                """

                if not isinstance(rect_1, Rectangle):
                    raise TypeError('rect_1 must be an instance of Rectangle')

                if not isinstance(rect_2, Rectangle):
                    raise TypeError('rect_2 must be an instance of Rectangle')

                rct1_area = rect_1.area()
                rct2_area = rect_2.area()

                if rct1_area >= rct2_area:
                    return rect_1

                return rect_2

            def __str__(self):
                """
                Returns a string with the representation of the Rectangle.

                """

                return self.__draw_rectangle()

            def __repr__(self):
                """
                Returns the representation of the Rectangle.

                """

                w = str(eval('self.width'))
                h = str(eval('self.height'))
                return 'Rectangle(' + w + ', ' + h + ')'

