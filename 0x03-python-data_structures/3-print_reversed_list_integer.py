#!/usr/bin/python3
'''This function prints elements of a list in reverse order'''


def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    for i in range(a - 1, -1, -1):
        print("{:d}".format(my_list[i]))