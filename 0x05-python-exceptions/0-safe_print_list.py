#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    safe_list = 0
    for items in range(x):
        try:
            print("{}".format(my_list[items]), end=" ")
            safe_list += 1
        except:
            break
    print()
    return safe_list
