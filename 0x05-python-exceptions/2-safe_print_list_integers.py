#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    first_elm = 0

    for i in range(x):
        try:
            if type(my_list[i]) is int and first_elm != x:
                print('{:d}'.format(my_list[i]), end='')
                first_elm += 1
        except TypeError:
            continue

    print()

    return first_elm
