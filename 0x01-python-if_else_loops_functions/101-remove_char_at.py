#!/usr/bin/python3
'''This program create a copy of a string without a char at index n'''


def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
