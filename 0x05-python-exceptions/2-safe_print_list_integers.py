#!/usr/bin/python3
'''This function prints x elements of a list int'''


def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (TypeError, ValueError):
            pass
    print("")
    return num
