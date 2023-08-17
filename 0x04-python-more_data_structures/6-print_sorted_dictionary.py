#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    strings = sorted(a_dictionary)
    for j in strings:
        print("{}: {}".format(j, a_dictionary[j]))