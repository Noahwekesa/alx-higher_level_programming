#!/usr/bin/python3
"""class calld student based on 10-student.py"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """function implementation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
        def to_json(self, attrs=None):
            """json function method"""
            if attrs is None:
                return self.__dict__
            else:
                 return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
            
            def reload_from_json(self, json):
                """reload from json method"""
                for attr, value in json.items():
                    setattr(self, attr, value)
