#!/usr/bin/python3
"""
function that returns True if the obj is an instance of, or if the ob
is an instance of a class that inheited from, the specified class
otherwise false
"""


def is_kind_of_class(obj, a_class):
    """function that satisfirs the requirement"""
    return isinstance((obj), a_class)
