#!/usr/bin/python3
"""python module that defines a class"""


class student:
    """class student"""
    def __init__(self, first_name, last_name, age) :
        """function with public instances of a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """rep of a student instance"""
        return self.__dict__
