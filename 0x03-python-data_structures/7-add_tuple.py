#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    element_1 = tuple_a[0] + tuple_b[0]
    element_2 = tuple_a[1] + tuple_b[1]
    sum_tuple = (element_1, element_2)
    return sum_tuple
