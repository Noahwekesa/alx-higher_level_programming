#!/usr/bin/python3
"""
class definition
"""


class Student:
    """class called student"""

    def __init__(self, first_name, last_name, age):
        """function implementation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            output_result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    output_result[attr] = getattr(self, attr)
            return output_result
