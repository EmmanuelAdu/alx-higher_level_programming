#!/usr/bin/python3
'''This function prints the elements contained in a list'''


def print_list_integer(my_list=[]):
    i = 0
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
