#!/usr/bin/python3
'''This function prints the elements contained in a list'''


def print_list_integer(my_list=[]):
    a = 0
    for a in range(len(my_list)):
        print("{:d}".format(my_list[a]))
