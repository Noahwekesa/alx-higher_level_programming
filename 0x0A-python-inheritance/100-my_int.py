#!/usr/bin/python3
"""
a class MyInt that inherits from int: 
"""


class MyInt(int):
    """
a class MyInt that inherits from int:
    """

    def __eq__(self, other):
        """Function"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """function implementation"""
        return not super().__ne__(other)
