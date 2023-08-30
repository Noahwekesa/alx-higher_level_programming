#!/usr/bin/python3
"""
a class Square that defines a square by: (based on 5-square.py)
"""


class Square:
    """creates a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a given size and position."""
        self.size = size
        self.position = position

    def __str__(self):
        """Return a string representation of the square."""
        return self.pos_print()

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    def pos_print(self):
        """Generate the string representation of the square with position."""
        elm = ""
        if self.size == 0:
            return "\n"
        for _ in range(self.position[1]):
            elm += "\n"
        for _ in range(self.size):
            for _ in range(self.position[0]):
                elm += " "
            for _ in range(self.size):
                elm += "#"
            elm += "\n"
        return elm

    def my_print(self):
        """Print the string representation of the square with position."""
        print(self.pos_print(), end='')
