#!/usr/bin/python3
"""
a class that inherits from a list
"""


class MyList(list):
    """
    class named my list
    """

    def print_sorted(self):
        """
        function that pritns the list but in ascending sort
        """
        sorted_list = sorted(self)
        print(sorted_list)
