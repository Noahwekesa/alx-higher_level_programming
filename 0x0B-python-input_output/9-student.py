#!/usr/bin/python3
"""create a class called student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
