#!/usr/bin/python3
def magic_calculation_102(a, b):
    from magiccalculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for numbers in range(4, 6):
            c = add(c, numbers)
            return (c)
        else:
            return (sub(a, b))
