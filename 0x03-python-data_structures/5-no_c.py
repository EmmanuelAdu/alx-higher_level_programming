#!/usr/bin/python3
'''This function removes c and C characters from a string'''


def no_c(my_string):
    i = 0
    str_len = len(my_string)

    for i in range(0, str_len):
        if my_string[i] == 'c' or my_string[i] == 'C':
            my_new_string = my_string[:i] + my_string[i + 1:]
            return (my_new_string)
