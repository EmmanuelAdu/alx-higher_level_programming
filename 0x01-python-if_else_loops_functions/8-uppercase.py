#!/usr/bin/python3
''' This function that prints a string in uppercase'''


def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - ord('a') + ord('A'))
        print("{}".format(char), end="")
    print("")
