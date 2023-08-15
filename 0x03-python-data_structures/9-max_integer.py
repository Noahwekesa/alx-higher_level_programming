#!/usr/bin/python
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_num = my_list[0]
    for num in my_list:
        if num > max_num:
            max_val = num
    return max_val