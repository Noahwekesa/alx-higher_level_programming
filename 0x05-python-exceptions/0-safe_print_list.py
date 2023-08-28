#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    list = 0
    for items in range(x):
        try:
            print("{}".format(my_list[items]), end="")
            list += 1
        except:
            break
    print()
    return list