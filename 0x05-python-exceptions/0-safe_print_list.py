#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    safe_list = 0
    for elm in range(x):
        try:
            print("{}".format(my_list[elm]), end=" ")
            safe_list += 1
        except ValueError:
            break
    print()
    return safe_list
