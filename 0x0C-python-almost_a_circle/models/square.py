#!/usr/bin/python3
'''Module  class for square.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''function Constructor.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''returns the size of the square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''function that updates via */**args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''updates attributes with no keyword argument.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''returns dict of the square.'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}